"use client";

export default function LeaderboardStrip({ players }) {
  const sorted = [...players].sort((a, b) => b.score - a.score);
  return (
    <div className="leaderboard-strip">
      {sorted.map((p) => (
        <div className="lb-chip" key={p.id}>
          <span>{p.name}</span>
          <span className="lb-score">{p.score}</span>
        </div>
      ))}
    </div>
  );
}
