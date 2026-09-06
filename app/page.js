"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "../lib/supabaseClient";

const CODE_CHARS = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; // no 0/O/1/I

function randomCode(len = 5) {
  let s = "";
  for (let i = 0; i < len; i++) {
    s += CODE_CHARS[Math.floor(Math.random() * CODE_CHARS.length)];
  }
  return s;
}

export default function HomePage() {
  const router = useRouter();
  const [mode, setMode] = useState("choose"); // choose | create | join
  const [hostName, setHostName] = useState("");
  const [joinCode, setJoinCode] = useState("");
  const [joinName, setJoinName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  async function handleCreate(e) {
    e.preventDefault();
    if (!hostName.trim()) return;
    setBusy(true);
    setError("");
    try {
      let code = randomCode();
      let attempts = 0;
      let room = null;
      while (attempts < 5 && !room) {
        const { data, error: insErr } = await supabase
          .from("rooms")
          .insert({ code })
          .select()
          .single();
        if (!insErr) {
          room = data;
        } else if (insErr.code === "23505") {
          code = randomCode();
          attempts++;
        } else {
          throw insErr;
        }
      }
      if (!room) throw new Error("Could not create a room. Please try again.");

      const { data: player, error: playerErr } = await supabase
        .from("players")
        .insert({ room_code: room.code, name: hostName.trim(), is_host: true })
        .select()
        .single();
      if (playerErr) throw playerErr;

      localStorage.setItem(
        `bb_${room.code}`,
        JSON.stringify({
          playerId: player.id,
          name: player.name,
          isHost: true,
          hostSecret: room.host_secret,
        })
      );
      router.push(`/host/${room.code}`);
    } catch (err) {
      setError(err.message || "Something went wrong.");
      setBusy(false);
    }
  }

  async function handleJoin(e) {
    e.preventDefault();
    const code = joinCode.trim().toUpperCase();
    if (!code || !joinName.trim()) return;
    setBusy(true);
    setError("");
    try {
      const { data: room, error: roomErr } = await supabase
        .from("rooms")
        .select("*")
        .eq("code", code)
        .maybeSingle();
      if (roomErr) throw roomErr;
      if (!room) throw new Error("No game found with that code.");
      if (room.status !== "lobby") {
        throw new Error("That game has already started.");
      }

      const { data: player, error: playerErr } = await supabase
        .from("players")
        .insert({ room_code: code, name: joinName.trim(), is_host: false })
        .select()
        .single();
      if (playerErr) throw playerErr;

      localStorage.setItem(
        `bb_${code}`,
        JSON.stringify({
          playerId: player.id,
          name: player.name,
          isHost: false,
        })
      );
      router.push(`/play/${code}`);
    } catch (err) {
      setError(err.message || "Something went wrong.");
      setBusy(false);
    }
  }

  return (
    <main className="page">
      <div className="wrap">
        <div className="brand" style={{ justifyContent: "center" }}>
          <span className="brand-flame">🔥</span>
          <h1>Scripture Buzzer</h1>
        </div>
        <p className="tagline">
          A live, multiplayer Bible trivia game. First to buzz in with the
          right answer takes the point.
        </p>

        {mode === "choose" && (
          <div className="panel">
            <div className="btn-row" style={{ flexDirection: "column" }}>
              <button className="btn btn-primary" onClick={() => setMode("create")}>
                Host a new game
              </button>
              <div style={{ height: 12 }} />
              <button className="btn btn-secondary" onClick={() => setMode("join")}>
                Join a game
              </button>
            </div>
          </div>
        )}

        {mode === "create" && (
          <form className="panel" onSubmit={handleCreate}>
            <div className="field">
              <label>Your name (as the host)</label>
              <input
                autoFocus
                value={hostName}
                onChange={(e) => setHostName(e.target.value)}
                placeholder="e.g. Pastor Ayanda"
                maxLength={24}
              />
            </div>
            {error && <div className="error-text">{error}</div>}
            <button className="btn btn-primary" disabled={busy || !hostName.trim()}>
              {busy ? "Creating room…" : "Create room"}
            </button>
            <div style={{ height: 10 }} />
            <button
              type="button"
              className="link-btn"
              onClick={() => {
                setMode("choose");
                setError("");
              }}
            >
              Back
            </button>
          </form>
        )}

        {mode === "join" && (
          <form className="panel" onSubmit={handleJoin}>
            <div className="field">
              <label>Game code</label>
              <input
                autoFocus
                value={joinCode}
                onChange={(e) => setJoinCode(e.target.value.toUpperCase())}
                placeholder="e.g. F7K2Q"
                maxLength={6}
                style={{ letterSpacing: "0.15em", fontWeight: 700 }}
              />
            </div>
            <div className="field">
              <label>Your name</label>
              <input
                value={joinName}
                onChange={(e) => setJoinName(e.target.value)}
                placeholder="e.g. Thandiwe"
                maxLength={24}
              />
            </div>
            {error && <div className="error-text">{error}</div>}
            <button
              className="btn btn-primary"
              disabled={busy || !joinCode.trim() || !joinName.trim()}
            >
              {busy ? "Joining…" : "Join game"}
            </button>
            <div style={{ height: 10 }} />
            <button
              type="button"
              className="link-btn"
              onClick={() => {
                setMode("choose");
                setError("");
              }}
            >
              Back
            </button>
          </form>
        )}
      </div>
    </main>
  );
}
