import allQuestions from "../data/questions.json";

// Map for O(1) lookup by id
const byId = new Map(allQuestions.map((q) => [q.id, q]));

export function getQuestionById(id) {
  return byId.get(id);
}

export function totalQuestionCount() {
  return allQuestions.length;
}

// Fisher-Yates shuffle, returns a new array
function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Builds a randomized, non-repeating list of question ids for one game,
// with a healthy mix of difficulty levels.
export function buildQuestionOrder(count) {
  const easy = allQuestions.filter((q) => q.difficulty === "easy");
  const medium = allQuestions.filter((q) => q.difficulty === "medium");
  const hard = allQuestions.filter((q) => q.difficulty === "hard");

  // Roughly 25% easy, 45% medium, 30% hard, then top up randomly if a
  // bucket runs short.
  const nEasy = Math.round(count * 0.25);
  const nMedium = Math.round(count * 0.45);
  const nHard = count - nEasy - nMedium;

  const pick = (bucket, n) => shuffle(bucket).slice(0, n);

  let chosen = [
    ...pick(easy, nEasy),
    ...pick(medium, nMedium),
    ...pick(hard, nHard),
  ];

  if (chosen.length < count) {
    const usedIds = new Set(chosen.map((q) => q.id));
    const rest = shuffle(allQuestions.filter((q) => !usedIds.has(q.id)));
    chosen = chosen.concat(rest.slice(0, count - chosen.length));
  }

  return shuffle(chosen)
    .slice(0, count)
    .map((q) => q.id);
}

// Seconds allowed to answer, scaled by difficulty.
export function timeForDifficulty(difficulty) {
  if (difficulty === "easy") return 10;
  if (difficulty === "hard") return 18;
  return 14;
}
