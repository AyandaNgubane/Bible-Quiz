"use client";

export default function ConfirmQuitModal({ open, paused, onKeepPlaying, onQuit }) {
  if (!open) return null;

  return (
    <div className="modal-overlay" role="dialog" aria-modal="true">
      <div className="modal-panel">
        <div className="modal-flame">🔥</div>
        <h2 className="modal-title">Leaving so soon?</h2>
        <p className="modal-body">
          {paused
            ? "The game is paused for everyone while you decide. Quitting now will end your part in it — the others can keep going without you."
            : "Going back will quit the game. Want to keep playing instead?"}
        </p>
        <div className="modal-actions">
          <button className="btn btn-primary" onClick={onKeepPlaying}>
            Keep playing
          </button>
          <button className="btn btn-quit" onClick={onQuit}>
            Quit game
          </button>
        </div>
      </div>
    </div>
  );
}
