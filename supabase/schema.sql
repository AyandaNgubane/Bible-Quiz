-- ============================================================
-- Bible Buzzer — Supabase schema
-- Run this once in your Supabase project's SQL Editor.
-- ============================================================

create extension if not exists "pgcrypto";

-- ---------- ROOMS ----------
create table if not exists rooms (
  code text primary key,                 -- short join code, e.g. "AB12"
  status text not null default 'lobby',  -- lobby | playing | finished
  total_rounds int not null default 15,
  question_order jsonb not null default '[]'::jsonb, -- array of question ids, shuffled, no repeats
  current_index int not null default 0,
  current_question_started_at timestamptz,
  current_answer_revealed boolean not null default false,
  current_winner_player_id uuid,
  host_secret uuid not null default gen_random_uuid(), -- host proves ownership with this
  created_at timestamptz not null default now()
);

alter table rooms enable row level security;
create policy "rooms are readable by anyone" on rooms for select using (true);
create policy "rooms are insertable by anyone" on rooms for insert with check (true);
create policy "rooms are updatable by anyone" on rooms for update using (true);

-- ---------- PLAYERS ----------
create table if not exists players (
  id uuid primary key default gen_random_uuid(),
  room_code text not null references rooms(code) on delete cascade,
  name text not null,
  score int not null default 0,
  is_host boolean not null default false,
  left_at timestamptz,
  joined_at timestamptz not null default now()
);

alter table players enable row level security;
create policy "players are readable by anyone" on players for select using (true);
create policy "players are insertable by anyone" on players for insert with check (true);
create policy "players are updatable by anyone" on players for update using (true);

create index if not exists players_room_idx on players(room_code);

-- ---------- ANSWERS ----------
-- Only ONE correct answer per (room, question_index) can ever be recorded,
-- enforced by a partial unique index. This is what makes "first correct
-- answer wins the point" race-safe even with concurrent submissions.
create table if not exists answers (
  id uuid primary key default gen_random_uuid(),
  room_code text not null references rooms(code) on delete cascade,
  question_index int not null,
  player_id uuid not null references players(id) on delete cascade,
  option_index int not null,
  is_correct boolean not null,
  answered_at timestamptz not null default now()
);

create unique index if not exists one_winner_per_question
  on answers(room_code, question_index)
  where is_correct;

-- a player can only answer a given question once
create unique index if not exists one_answer_per_player_per_question
  on answers(room_code, question_index, player_id);

alter table answers enable row level security;
create policy "answers are readable by anyone" on answers for select using (true);
create policy "answers are insertable by anyone" on answers for insert with check (true);

-- ---------- RPC: submit_answer ----------
-- Atomically records an answer and, if correct AND first, awards the point.
-- Returns whether this submission was the winning one.
create or replace function submit_answer(
  p_room_code text,
  p_question_index int,
  p_player_id uuid,
  p_option_index int,
  p_is_correct boolean
) returns boolean
language plpgsql
as $$
declare
  won boolean := false;
begin
  begin
    insert into answers (room_code, question_index, player_id, option_index, is_correct)
    values (p_room_code, p_question_index, p_player_id, p_option_index, p_is_correct);
  exception when unique_violation then
    -- either this player already answered, or someone already won this question
    return false;
  end;

  if p_is_correct then
    -- did our insert win the unique "one_winner_per_question" slot?
    if exists (
      select 1 from answers
      where room_code = p_room_code
        and question_index = p_question_index
        and player_id = p_player_id
        and is_correct
    ) then
      update players set score = score + 1 where id = p_player_id;
      won := true;
    end if;
  end if;

  return won;
end;
$$;

-- Enable realtime on the tables the clients subscribe to.
-- Wrapped so this whole file is safe to re-run even if already applied.
do $$
begin
  begin
    execute 'alter publication supabase_realtime add table rooms';
  exception when duplicate_object then null;
  end;
  begin
    execute 'alter publication supabase_realtime add table players';
  exception when duplicate_object then null;
  end;
  begin
    execute 'alter publication supabase_realtime add table answers';
  exception when duplicate_object then null;
  end;
end $$;

-- ============================================================
-- Migration: pause support (back-button "quit?" confirmation)
-- Safe to re-run — adds columns only if they don't already exist.
-- ============================================================
alter table rooms add column if not exists paused boolean not null default false;
alter table rooms add column if not exists paused_at timestamptz;
alter table rooms add column if not exists pause_offset_seconds numeric not null default 0;

