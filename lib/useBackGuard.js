"use client";

import { useEffect, useState, useCallback } from "react";

/**
 * Intercepts back navigation (browser back button on desktop, and the
 * hardware/gesture back button on mobile — both fire the same "popstate"
 * event in a web app) and shows a confirm dialog instead of immediately
 * leaving the page.
 *
 * How it works: as soon as the guard is enabled, we push one extra history
 * entry. Pressing back consumes that entry and fires "popstate" — instead
 * of letting the browser actually navigate, we immediately push another
 * entry right back (cancelling the navigation) and flip `showConfirm` to
 * true so the caller can render a modal. If the person confirms they want
 * to quit, the caller is responsible for actually navigating away (e.g.
 * router.replace("/")); if they cancel, we just close the modal and stay
 * exactly where we were.
 */
export function useBackGuard(enabled) {
  const [showConfirm, setShowConfirm] = useState(false);

  useEffect(() => {
    if (!enabled) return;

    window.history.pushState({ bbGuard: true }, "");

    function onPopState() {
      window.history.pushState({ bbGuard: true }, "");
      setShowConfirm(true);
    }

    window.addEventListener("popstate", onPopState);
    return () => window.removeEventListener("popstate", onPopState);
  }, [enabled]);

  const dismiss = useCallback(() => setShowConfirm(false), []);

  return { showConfirm, dismiss };
}
