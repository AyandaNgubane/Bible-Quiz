import { supabase } from "./supabaseClient";

// Pauses the shared game clock for everyone in the room. Guarded so that
// if multiple people hit back at the same instant, only the first pause
// attempt actually takes effect.
export async function pauseRoom(code) {
  await supabase
    .from("rooms")
    .update({ paused: true, paused_at: new Date().toISOString() })
    .eq("code", code)
    .eq("paused", false);
}

// Resumes the shared game clock, folding the time spent paused into
// pause_offset_seconds so no one loses (or gains) time on the current
// question's countdown.
export async function resumeRoom(room) {
  if (!room || !room.paused || !room.paused_at) return;
  const pausedMs = Date.now() - new Date(room.paused_at).getTime();
  const addedSeconds = Math.max(0, pausedMs / 1000);
  await supabase
    .from("rooms")
    .update({
      paused: false,
      paused_at: null,
      pause_offset_seconds: (room.pause_offset_seconds || 0) + addedSeconds,
    })
    .eq("code", room.code)
    .eq("paused", true);
}
