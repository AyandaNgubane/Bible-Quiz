"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "../../../lib/supabaseClient";
import {
  getQuestionById,
  timeForDifficulty,
  computeSecondsLeft,
} from "../../../lib/questions";
import { pauseRoom, resumeRoom } from "../../../lib/pause";
import { useBackGuard } from "../../../lib/useBackGuard";
import TimerRing from "../../../components/TimerRing";
import LeaderboardStrip from "../../../components/Leaderboard";
import ConfirmQuitModal from "../../../components/ConfirmQuitModal";

export default function PlayPage({ params }) {
  const code = params.code.toUpperCase();
  const router = useRouter();

  const [identity, setIdentity] = useState(null);
  const [checkedStorage, setCheckedStorage] = useState(false);
  const [joinName, setJoinName] = useState("");
  const [joinBusy, setJoinBusy] = useState(false);
  const [joinError, setJoinError] = useState("");

  const [room, setRoom] = useState(undefined);
  const [players, setPlayers] = useState([]);
  const [secondsLeft, setSecondsLeft] = useState(null);
  const [myAnswer, setMyAnswer] = useState({ index: null, forQuestion: null });

  const tickRef = useRef(null);

  // ---------- back-button / quit guard ----------
  const guardEnabled =
    !!identity && !!room && (room.status === "lobby" || room.status === "playing");
  const { showConfirm, dismiss } = useBackGuard(guardEnabled);

  useEffect(() => {
    if (showConfirm && room?.status === "playing") {
      pauseRoom(code);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [showConfirm]);

  async function handleKeepPlaying() {
    dismiss();
    if (room?.paused) await resumeRoom(room);
  }

  useEffect(() => {
    const raw = localStorage.getItem(`bb_${code}`);
    if (raw) setIdentity(JSON.parse(raw));
    setCheckedStorage(true);
  }, [code]);

  useEffect(() => {
    if (!identity) return;
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
        .order("joined_at", { ascending: true });
      if (active) setPlayers(p || []);
    }
    load();

    const channel = supabase
      .channel(`play-room-${code}-${identity.playerId}`)
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "rooms", filter: `code=eq.${code}` },
        (payload) => {
          if (payload.eventType === "DELETE") setRoom(null);
          else setRoom(payload.new);
        }
      )
      .on(
        "postgres_changes",
        { event: "*", schema: "public", table: "players", filter: `room_code=eq.${code}` },
        () => {
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
  }, [code, identity]);

  // countdown display — pauses in lockstep with the host when room.paused
  useEffect(() => {
    clearInterval(tickRef.current);
    if (!room || room.status !== "playing" || room.current_answer_revealed) return;
    const q = getQuestionById(room.question_order[room.current_index]);
    if (!q) return;
    const limit = timeForDifficulty(q.difficulty);

    if (room.paused) {
      setSecondsLeft(computeSecondsLeft(room, limit));
      return;
    }

    tickRef.current = setInterval(() => {
      setSecondsLeft(computeSecondsLeft(room, limit));
    }, 250);
    return () => clearInterval(tickRef.current);
  }, [
    room?.status,
    room?.current_index,
    room?.current_answer_revealed,
    room?.paused,
    room?.pause_offset_seconds,
  ]);

  async function handleJoinSubmit(e) {
    e.preventDefault();
    if (!joinName.trim()) return;
    setJoinBusy(true);
    setJoinError("");
    try {
      const { data: r, error: roomErr } = await supabase
        .from("rooms")
        .select("*")
        .eq("code", code)
        .maybeSingle();
      if (roomErr) throw roomErr;
      if (!r) throw new Error("No game found with that code.");
      if (r.status !== "lobby") throw new Error("That game has already started.");

      const { data: player, error: playerErr } = await supabase
        .from("players")
        .insert({ room_code: code, name: joinName.trim(), is_host: false })
        .select()
        .single();
      if (playerErr) throw playerErr;

      const newIdentity = { playerId: player.id, name: player.name, isHost: false };
      localStorage.setItem(`bb_${code}`, JSON.stringify(newIdentity));
      setIdentity(newIdentity);
    } catch (err) {
      setJoinError(err.message || "Something went wrong.");
    } finally {
      setJoinBusy(false);
    }
  }

  async function handleAnswer(i) {
    if (!room || room.paused || myAnswer.forQuestion === room.current_index) return;
    setMyAnswer({ index: i, forQuestion: room.current_index });

    const q = getQuestionById(room.question_order[room.current_index]);
    const isCorrect = i === q.correct_index;

    const { data: won } = await supabase.rpc("submit_answer", {
      p_room_code: code,
      p_question_index: room.current_index,
      p_player_id: identity.playerId,
      p_option_index: i,
      p_is_correct: isCorrect,
    });

    if (won) {
      await supabase
        .from("rooms")
        .update({
          current_answer_revealed: true,
          current_winner_player_id: identity.playerId,
        })
        .eq("code", code)
        .eq("current_index", room.current_index)
        .eq("current_answer_revealed", false);
    }
  }

  async function handleQuit() {
    if (identity?.playerId) {
      await supabase
        .from("players")
        .update({ left_at: new Date().toISOString() })
        .eq("id", identity.playerId);
    }
    if (room?.paused) {
      await resumeRoom(room);
    }
    localStorage.removeItem(`bb_${code}`);
    router.replace("/");
  }

  if (!checkedStorage) return null;

  const modal = (
    <ConfirmQuitModal
      open={showConfirm}
      paused={room?.paused}
      onKeepPlaying={handleKeepPlaying}
      onQuit={handleQuit}
    />
  );

  // ---------- need to join first ----------
  if (!identity) {
    return (
      <main className="page">
        <div className="wrap">
          <div className="brand" style={{ justifyContent: "center" }}>
            <span className="brand-flame">🔥</span>
            <h1>Scripture Buzzer</h1>
          </div>
          <form className="panel" onSubmit={handleJoinSubmit}>
            <div className="section-label">Joining game {code}</div>
            <div className="field">
              <label>Your name</label>
              <input
                autoFocus
                value={joinName}
                onChange={(e) => setJoinName(e.target.value)}
                placeholder="e.g. Thandiwe"
                maxLength={24}
              />
            </div>
            {joinError && <div className="error-text">{joinError}</div>}
            <button className="btn btn-primary" disabled={joinBusy || !joinName.trim()}>
              {joinBusy ? "Joining…" : "Join game"}
            </button>
          </form>
        </div>
      </main>
    );
  }

  if (room === undefined) return null;

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

  // ---------- LOBBY ----------
  if (room.status === "lobby") {
    return (
      <>
        <main className="page">
          <div className="wrap">
            <div className="brand" style={{ justifyContent: "center" }}>
              <span className="brand-flame">🔥</span>
              <h1>You're in!</h1>
            </div>
            <div className="panel">
              <p className="center-note" style={{ marginTop: 0 }}>
                <span className="waiting-pulse" />
                Waiting for the host to start the game…
              </p>
              <div className="section-label">
                Players ({players.filter((p) => !p.left_at).length})
              </div>
              <ul className="player-list">
                {players
                  .filter((p) => !p.left_at)
                  .map((p) => (
                    <li className="player-row" key={p.id}>
                      <span className="player-name">
                        {p.name}
                        {p.id === identity.playerId ? " (you)" : ""}
                        {p.is_host ? " — host" : ""}
                      </span>
                    </li>
                  ))}
              </ul>
            </div>
            <button className="btn btn-quit" onClick={handleQuit}>
              Quit
            </button>
          </div>
        </main>
        {modal}
      </>
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
                <div
                  className={`podium-row ${i === 0 ? "first" : ""}`}
                  key={p.id}
                  style={{
                    outline:
                      p.id === identity.playerId ? "1px solid var(--flame)" : "none",
                  }}
                >
                  <div className="podium-rank">{i + 1}</div>
                  <div className="podium-name">
                    {p.name}
                    {p.id === identity.playerId ? " (you)" : ""}
                  </div>
                  <div className="podium-score">{p.score}</div>
                </div>
              ))}
            </div>
          </div>
          <p className="center-note">Waiting to see if the host starts another round…</p>
          <button className="btn btn-quit" onClick={handleQuit}>
            Quit to home
          </button>
        </div>
      </main>
    );
  }

  // ---------- PLAYING ----------
  const q = getQuestionById(room.question_order[room.current_index]);
  if (!q) return null;
  const limit = timeForDifficulty(q.difficulty);
  const winner = players.find((p) => p.id === room.current_winner_player_id);
  const alreadyAnswered = myAnswer.forQuestion === room.current_index;
  const iWon = room.current_winner_player_id === identity.playerId;

  return (
    <>
      <main className="game-shell">
        <div className="game-top">
          <span className="round-pill">
            Question {room.current_index + 1} of {room.total_rounds}
          </span>
          <span className={`difficulty-pill difficulty-${q.difficulty}`}>
            {q.difficulty}
          </span>
          {room.paused ? (
            <span className="paused-pill">⏸ Paused</span>
          ) : !room.current_answer_revealed ? (
            <TimerRing secondsLeft={secondsLeft ?? limit} totalSeconds={limit} />
          ) : (
            <div style={{ width: 64 }} />
          )}
        </div>

        <div className="question-card">
          <div className="question-category">{q.category}</div>
          <div className="question-text">{q.question}</div>
        </div>

        <div className="options-grid">
          {q.options.map((opt, i) => {
            let cls = "option-btn";
            if (room.current_answer_revealed) {
              if (i === q.correct_index) cls += " correct";
              else if (i === myAnswer.index) cls += " wrong";
            } else if (alreadyAnswered && i === myAnswer.index) {
              cls += " picked";
            }
            return (
              <button
                key={i}
                className={cls}
                disabled={alreadyAnswered || room.current_answer_revealed || room.paused}
                onClick={() => handleAnswer(i)}
              >
                {opt}
              </button>
            );
          })}
        </div>

        {room.paused ? (
          <div className="paused-overlay-note">
            Game paused — someone stepped away. It'll pick back up right where it left
            off.
          </div>
        ) : room.current_answer_revealed ? (
          <div className={`reveal-banner ${winner ? "reveal-win" : "reveal-none"}`}>
            {winner
              ? iWon
                ? "You buzzed in first! +1 point"
                : `${winner.name} buzzed in first`
              : "Time's up — no one scored"}
          </div>
        ) : alreadyAnswered ? (
          <p className="center-note">
            <span className="waiting-pulse" />
            Answer locked in — waiting on the others…
          </p>
        ) : null}

        <LeaderboardStrip players={players} />

        <div style={{ marginTop: 30, width: "100%", maxWidth: 900 }}>
          <button className="btn btn-quit" onClick={handleQuit}>
            Quit
          </button>
        </div>
      </main>
      {modal}
    </>
  );
}
