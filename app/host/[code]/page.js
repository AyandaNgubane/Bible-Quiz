"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "../../../lib/supabaseClient";
import {
  buildQuestionOrder,
  getQuestionById,
  timeForDifficulty,
} from "../../../lib/questions";
import TimerRing from "../../../components/TimerRing";
import LeaderboardStrip from "../../../components/Leaderboard";

const ROUND_PRESETS = [10, 15, 20, 30];
const REVEAL_DELAY_MS = 4200;

export default function HostPage({ params }) {
  const code = params.code.toUpperCase();
  const router = useRouter();

  const [identity, setIdentity] = useState(null);
  const [room, setRoom] = useState(undefined);
  const [players, setPlayers] = useState([]);
  const [roundsChoice, setRoundsChoice] = useState(15);
  const [customRounds, setCustomRounds] = useState("");
  const [secondsLeft, setSecondsLeft] = useState(null);
  const [error, setError] = useState("");

  const tickRef = useRef(null);
  const advanceTimeoutRef = useRef(null);

  // ---------- load identity, verify host ----------
  useEffect(() => {
    const raw = localStorage.getItem(`bb_${code}`);
    if (!raw) {
      router.replace("/");
      return;
    }
    const parsed = JSON.parse(raw);
    if (!parsed.isHost) {
      router.replace(`/play/${code}`);
      return;
    }
    setIdentity(parsed);
  }, [code, router]);

  // ---------- initial fetch + realtime subscriptions ----------
  useEffect(() => {
    let active = true;

    async function load() {
      const { data: r } = await supabase
        .from("rooms")
        .select("*")
        .eq("code", code)
        .maybeSingle();
      if (active) setRoom(r || null);

      const { data: p } = await supabase
        .from("players")
        .select("*")
        .eq("room_code", code)
        .is("left_at", null)
        .order("joined_at", { ascending: true });
      if (active) setPlayers(p || []);
    }
    load();

    const channel = supabase
      .channel(`host-room-${code}`)
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "rooms", filter: `code=eq.${code}` },
        (payload) => {
          if (payload.eventType === "DELETE") {
            setRoom(null);
          } else {
            setRoom(payload.new);
          }
        }
      )
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "players", filter: `room_code=eq.${code}` },
        () => {
          // simplest correct approach: just refetch the player list
          supabase
            .from("players")
            .select("*")
            .eq("room_code", code)
            .order("joined_at", { ascending: true })
            .then(({ data }) => setPlayers(data || []));
        }
      )
      .subscribe();

    return () => {
      active = false;
      supabase.removeChannel(channel);
    };
  }, [code]);

  const activePlayers = players.filter((p) => !p.left_at);

  // ---------- start game ----------
  async function handleStart() {
    const rounds = customRounds ? parseInt(customRounds, 10) : roundsChoice;
    if (!rounds || rounds < 1) return;
    const order = buildQuestionOrder(rounds);
    await supabase
      .from("rooms")
      .update({
        status: "playing",
        total_rounds: rounds,
        question_order: order,
        current_index: 0,
        current_question_started_at: new Date().toISOString(),
        current_answer_revealed: false,
        current_winner_player_id: null,
      })
      .eq("code", code);
  }

  // ---------- reveal + advance logic (host is the sole conductor) ----------
  const revealAndScheduleAdvance = useCallback(
    async (currentRoom) => {
      if (!currentRoom || currentRoom.current_answer_revealed) return;
      await supabase
        .from("rooms")
        .update({ current_answer_revealed: true })
        .eq("code", code)
        .eq("current_index", currentRoom.current_index)
        .eq("current_answer_revealed", false);
    },
    [code]
  );

  const advanceQuestion = useCallback(
    async (currentRoom) => {
      const nextIndex = currentRoom.current_index + 1;
      if (nextIndex >= currentRoom.total_rounds) {
        await supabase.from("rooms").update({ status: "finished" }).eq("code", code);
      } else {
        await supabase
          .from("rooms")
          .update({
            current_index: nextIndex,
            current_question_started_at: new Date().toISOString(),
            current_answer_revealed: false,
            current_winner_player_id: null,
          })
          .eq("code", code);
      }
    },
    [code]
  );

  // ---------- countdown + auto-advance effect ----------
  useEffect(() => {
    clearInterval(tickRef.current);
    clearTimeout(advanceTimeoutRef.current);

    if (!room || room.status !== "playing") return;

    const q = getQuestionById(room.question_order[room.current_index]);
    if (!q) return;
    const limit = timeForDifficulty(q.difficulty);

    if (room.current_answer_revealed) {
      advanceTimeoutRef.current = setTimeout(() => {
        advanceQuestion(room);
      }, REVEAL_DELAY_MS);
      return () => clearTimeout(advanceTimeoutRef.current);
    }

    const started = new Date(room.current_question_started_at).getTime();

    tickRef.current = setInterval(() => {
      const elapsed = (Date.now() - started) / 1000;
      const left = Math.ceil(limit - elapsed);
      setSecondsLeft(left);
      if (left <= 0) {
        clearInterval(tickRef.current);
        revealAndScheduleAdvance(room);
      }
    }, 250);

    return () => clearInterval(tickRef.current);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [room?.status, room?.current_index, room?.current_answer_revealed]);

  async function handleEndGame() {
    await supabase.from("rooms").update({ status: "finished" }).eq("code", code);
  }

  async function handleNewGame() {
    await supabase
      .from("rooms")
      .update({
        status: "lobby",
        current_index: 0,
        question_order: [],
        current_answer_revealed: false,
        current_winner_player_id: null,
      })
      .eq("code", code);
    await supabase.from("players").update({ score: 0 }).eq("room_code", code);
  }

  async function handleQuit() {
    if (identity?.playerId) {
      await supabase.from("rooms").update({ status: "finished" }).eq("code", code);
    }
    localStorage.removeItem(`bb_${code}`);
    router.push("/");
  }

  if (!identity || room === undefined) return null;

  if (!room) {
    return (
      <main className="page">
        <div className="wrap panel">
          <p className="center-note">This game no longer exists.</p>
          <button className="btn btn-primary" onClick={() => router.push("/")}>
            Back home
          </button>
        </div>
      </main>
    );
  }

  const joinUrl =
    typeof window !== "undefined" ? `${window.location.origin}/play/${code}` : "";

  // ---------- LOBBY ----------
  if (room.status === "lobby") {
    return (
      <main className="page">
        <div className="wrap">
          <div className="brand" style={{ justifyContent: "center" }}>
            <span className="brand-flame">🔥</span>
            <h1>Scripture Buzzer</h1>
          </div>

          <div className="panel">
            <div className="room-code">{code}</div>
            <div className="room-code-label">
              Players join at {typeof window !== "undefined" ? window.location.origin : ""}
              /play with this code, or by scanning below
            </div>
            {joinUrl && (
              <div className="qr-box">
                <img
                  src={`https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=${encodeURIComponent(
                    joinUrl
                  )}`}
                  width={180}
                  height={180}
                  alt="QR code to join"
                />
              </div>
            )}
          </div>

          <div className="panel">
            <div className="section-label">Number of rounds</div>
            <div className="round-options">
              {ROUND_PRESETS.map((n) => (
                <div
                  key={n}
                  className={`round-chip ${
                    !customRounds && roundsChoice === n ? "active" : ""
                  }`}
                  onClick={() => {
                    setRoundsChoice(n);
                    setCustomRounds("");
                  }}
                >
                  {n}
                </div>
              ))}
            </div>
            <div className="field">
              <label>Or a custom number</label>
              <input
                type="number"
                min={1}
                max={200}
                value={customRounds}
                onChange={(e) => setCustomRounds(e.target.value)}
                placeholder="e.g. 25"
              />
            </div>
          </div>

          <div className="panel">
            <div className="section-label">
              Players in the room ({activePlayers.length})
            </div>
            {activePlayers.length === 0 ? (
              <p className="center-note" style={{ margin: 0 }}>
                <span className="waiting-pulse" />
                Waiting for players to join…
              </p>
            ) : (
              <ul className="player-list">
                {activePlayers.map((p) => (
                  <li className="player-row" key={p.id}>
                    <span className="player-name">
                      {p.name}
                      {p.is_host ? " (host)" : ""}
                    </span>
                  </li>
                ))}
              </ul>
            )}
          </div>

          <button
            className="btn btn-primary"
            onClick={handleStart}
            disabled={activePlayers.length < 1}
          >
            Start game
          </button>
          <div style={{ height: 10 }} />
          <button className="btn btn-quit" onClick={handleQuit}>
            Quit
          </button>
        </div>
      </main>
    );
  }

  // ---------- FINISHED ----------
  if (room.status === "finished") {
    const ranked = [...players].sort((a, b) => b.score - a.score);
    return (
      <main className="page">
        <div className="wrap">
          <div className="brand" style={{ justifyContent: "center" }}>
            <span className="brand-flame">🏆</span>
            <h1>Final scores</h1>
          </div>
          <div className="panel">
            <div className="final-podium">
              {ranked.map((p, i) => (
                <div className={`podium-row ${i === 0 ? "first" : ""}`} key={p.id}>
                  <div className="podium-rank">{i + 1}</div>
                  <div className="podium-name">{p.name}</div>
                  <div className="podium-score">{p.score}</div>
                </div>
              ))}
            </div>
          </div>
          <button className="btn btn-primary" onClick={handleNewGame}>
            Play again with this group
          </button>
          <div style={{ height: 10 }} />
          <button className="btn btn-quit" onClick={handleQuit}>
            Quit to home
          </button>
        </div>
      </main>
    );
  }

  // ---------- PLAYING (big-screen host view) ----------
  const q = getQuestionById(room.question_order[room.current_index]);
  if (!q) return null;
  const limit = timeForDifficulty(q.difficulty);
  const winner = players.find((p) => p.id === room.current_winner_player_id);

  return (
    <main className="game-shell">
      <div className="game-top">
        <span className="round-pill">
          Question {room.current_index + 1} of {room.total_rounds}
        </span>
        <span className={`difficulty-pill difficulty-${q.difficulty}`}>
          {q.difficulty}
        </span>
        {!room.current_answer_revealed && (
          <TimerRing secondsLeft={secondsLeft ?? limit} totalSeconds={limit} />
        )}
        {room.current_answer_revealed && <div style={{ width: 64 }} />}
      </div>

      <div className="question-card">
        <div className="question-category">{q.category}</div>
        <div className="question-text">{q.question}</div>
      </div>

      <div className="options-grid">
        {q.options.map((opt, i) => {
          let cls = "option-btn";
          if (room.current_answer_revealed) {
            cls += i === q.correct_index ? " correct" : "";
          }
          return (
            <button key={i} className={cls} disabled>
              {opt}
            </button>
          );
        })}
      </div>

      {room.current_answer_revealed && (
        <div className={`reveal-banner ${winner ? "reveal-win" : "reveal-none"}`}>
          {winner ? `${winner.name} buzzed in first! +1 point` : "Time's up — no one scored"}
        </div>
      )}

      <LeaderboardStrip players={players} />

      <div style={{ marginTop: 30, width: "100%", maxWidth: 900 }}>
        <button className="btn btn-quit" onClick={handleEndGame}>
          End game now
        </button>
      </div>
    </main>
  );
}
