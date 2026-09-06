# Scripture Buzzer

A live, multiplayer Bible trivia buzzer game. The host puts up a question on
their screen (or shares the room code), everyone else answers on their own
phone, and whoever taps the correct answer first takes the point. Built with
Next.js + Supabase Realtime — no server to run yourself.

- **1,005 original multiple-choice questions**, hand-organized across 25
  categories (books of the Bible, kings, disciples, judges, prophets,
  miracles, parables, women of the Bible, places, Pentecostal/Charismatic
  doctrine, and more), balanced across easy/medium/hard difficulty.
- Every game randomly draws a fresh, non-repeating set of questions.
- Configurable rounds (10 / 15 / 20 / 30, or a custom number).
- Real-time buzzer scoring: the first correct answer is recorded atomically
  in the database, so it's fair even if two people tap within milliseconds
  of each other.
- Quit buttons for both host and players.

## How it works for players

This is **not** a peer-to-peer LAN game — it works like Kahoot: everyone
(host and players) just needs to be online and open the same web link.
"Connecting via wifi" in practice means: the host shows the room code (or a
QR code), and everyone on the same wifi (or any internet connection) opens
the join link on their own phone and types the code in.

## One-time setup (no command line needed)

### 1. Create a Supabase project
1. Go to [supabase.com](https://supabase.com) → New project.
2. Once it's created, open **SQL Editor** → paste in the entire contents of
   `supabase/schema.sql` from this project → **Run**.
3. Go to **Project Settings → API**. Copy the **Project URL** and the
   **anon public** key — you'll need both in step 3 below.

### 2. Push this project to GitHub
1. Create a new repository on GitHub (e.g. `scripture-buzzer`).
2. Use GitHub's web uploader ("Add file → Upload files") to upload every
   file and folder in this project, keeping the folder structure intact
   (`app/`, `lib/`, `components/`, `data/`, `supabase/`, `package.json`,
   etc). Do not upload `node_modules` (there isn't one yet — that's normal).

### 3. Deploy to Vercel
1. Go to [vercel.com](https://vercel.com) → **Add New → Project** → import
   the GitHub repo you just created.
2. Before deploying, open **Environment Variables** and add:
   - `NEXT_PUBLIC_SUPABASE_URL` → your Supabase Project URL
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY` → your Supabase anon public key
3. Click **Deploy**. Vercel will install dependencies and build it for you.
4. Once deployed, open the live URL — that's the link/QR code the host
   shares with players.

That's it — no terminal, no local installs required.

## Playing a game

1. Host opens the site → **Host a new game** → enters their name.
2. The host's screen shows a room code and QR code, and a rounds selector
   (10/15/20/30 or custom).
3. Players open the same site on their own phones → **Join a game** → enter
   the code and their name (or just scan the QR code, which links straight
   to the join page).
4. Host taps **Start game**. Each question appears on every screen at the
   same moment with a countdown ring (10–18 seconds depending on
   difficulty). Whoever taps the correct multiple-choice answer first wins
   the point — ties are broken automatically by the database, down to the
   millisecond.
5. After the configured number of rounds, a final leaderboard appears. The
   host can start a fresh game with the same group (scores reset) or quit.

## Project structure

```
app/
  page.js              landing page (create/join)
  host/[code]/page.js  host lobby, live game screen, results
  play/[code]/page.js  player join, live gameplay, results
  layout.js, globals.css
components/
  TimerRing.js, Leaderboard.js
lib/
  supabaseClient.js    Supabase client (reads env vars)
  questions.js         shuffling / round-building helpers
data/
  questions.json       the 1,005-question bank
supabase/
  schema.sql           run this once in Supabase's SQL editor
gen/
  the Python scripts used to generate data/questions.json — kept for
  reference if you ever want to add more questions later; not needed to
  run the app itself.
```

## Adding more questions later

Each entry in `data/questions.json` looks like this:

```json
{
  "question": "Which book of the Bible comes immediately after Malachi?",
  "options": ["Matthew", "Mark", "Luke", "John"],
  "correct_index": 0,
  "difficulty": "medium",
  "category": "Bible Books",
  "id": "q_0123_ab12cd34"
}
```

You can hand-edit this file directly (any text/JSON editor works), or reuse
the pattern in the `gen/` scripts and re-run `python3 gen/build_all.py` to
regenerate it with de-duplication built in.
