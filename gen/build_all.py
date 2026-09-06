import json, sys, hashlib

sys.path.insert(0, ".")
from gen_books import build as b_books
from gen_kings import build as b_kings
from gen_disciples import build as b_disciples
from gen_judges import build as b_judges
from gen_prophets import build as b_prophets
from gen_numbers import build as b_numbers
from gen_miracles import build as b_miracles
from gen_parables import build as b_parables
from gen_women import build as b_women
from gen_places import build as b_places
from gen_doctrine1 import build as b_d1
from gen_doctrine2 import build as b_d2
from gen_doctrine3 import build as b_d3
from gen_doctrine4 import build as b_d4
from gen_general1 import build as b_g1
from gen_general2 import build as b_g2
from gen_general3 import build as b_g3
from gen_general4 import build as b_g4
from gen_general5 import build as b_g5
from gen_general6 import build as b_g6
from gen_general7 import build as b_g7
from gen_general8 import build as b_g8
from gen_general9 import build as b_g9
from gen_general10 import build as b_g10
from gen_general11 import build as b_g11
from gen_general12 import build as b_g12

builders = [b_books, b_kings, b_disciples, b_judges, b_prophets, b_numbers,
            b_miracles, b_parables, b_women, b_places,
            b_d1, b_d2, b_d3, b_d4,
            b_g1, b_g2, b_g3, b_g4, b_g5, b_g6, b_g7, b_g8, b_g9, b_g10, b_g11, b_g12]

all_qs = []
for b in builders:
    all_qs.extend(b())

print(f"Raw total: {len(all_qs)}")

# Validate + dedupe
seen = set()
final = []
errors = []
for q in all_qs:
    text = q["question"].strip()
    key = text.lower()
    if key in seen:
        continue
    seen.add(key)

    if not isinstance(q.get("options"), list) or len(q["options"]) != 4:
        errors.append(f"BAD OPTIONS COUNT: {text}")
        continue
    if len(set(o.strip().lower() for o in q["options"])) != 4:
        errors.append(f"DUPLICATE OPTIONS WITHIN QUESTION: {text} -> {q['options']}")
        continue
    ci = q.get("correct_index")
    if not isinstance(ci, int) or ci < 0 or ci > 3:
        errors.append(f"BAD CORRECT INDEX: {text}")
        continue
    if q.get("difficulty") not in ("easy", "medium", "hard"):
        errors.append(f"BAD DIFFICULTY: {text}")
        continue
    if not q.get("category"):
        errors.append(f"MISSING CATEGORY: {text}")
        continue

    final.append(q)

print(f"After dedupe+validation: {len(final)}")
print(f"Errors: {len(errors)}")
for e in errors[:30]:
    print(" -", e)

# assign stable ids
for i, q in enumerate(final):
    h = hashlib.sha1(q["question"].encode("utf-8")).hexdigest()[:8]
    q["id"] = f"q_{i:04d}_{h}"

# difficulty breakdown
from collections import Counter
diff_counts = Counter(q["difficulty"] for q in final)
cat_counts = Counter(q["category"] for q in final)
print("Difficulty breakdown:", dict(diff_counts))
print(f"Categories: {len(cat_counts)}")
for c, n in sorted(cat_counts.items(), key=lambda x: -x[1]):
    print(f"  {c}: {n}")

with open("../data/questions.json", "w") as f:
    json.dump(final, f, indent=1)

print(f"\nWrote {len(final)} questions to data/questions.json")
