"use client";

export default function TimerRing({ secondsLeft, totalSeconds }) {
  const size = 64;
  const stroke = 5;
  const r = (size - stroke) / 2;
  const circumference = 2 * Math.PI * r;
  const pct = Math.max(0, Math.min(1, secondsLeft / totalSeconds));
  const offset = circumference * (1 - pct);
  const color =
    secondsLeft <= 3
      ? "var(--bad)"
      : secondsLeft <= totalSeconds * 0.4
      ? "var(--flame)"
      : "var(--good-bright)";

  return (
    <div className="timer-ring-wrap">
      <svg width={size} height={size}>
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke="var(--hairline)"
          strokeWidth={stroke}
        />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke={color}
          strokeWidth={stroke}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
          style={{ transition: "stroke-dashoffset 0.9s linear, stroke 0.3s" }}
        />
      </svg>
      <div className="timer-ring-num">{Math.max(0, secondsLeft)}</div>
    </div>
  );
}
