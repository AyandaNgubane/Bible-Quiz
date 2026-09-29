import random
from books_data import BOOKS, CATEGORIES, AUTHOR_POOL

random.seed(42)

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def build():
    qs = []
    names = [b[0] for b in BOOKS]

    # T1: Old Testament or New Testament (easy)
    for name, testament, cat, author in BOOKS:
        correct = "Old Testament" if testament == "OT" else "New Testament"
        opts, idx = make_options(correct, ["Old Testament", "New Testament", "Apocrypha", "The Torah only"])
        qs.append({
            "question": f"Is the book of {name} found in the Old Testament or the New Testament?",
            "options": opts, "correct_index": idx,
            "difficulty": "easy", "category": "Bible Books",
        })

    # T2: category (medium)
    for name, testament, cat, author in BOOKS:
        opts, idx = make_options(cat, CATEGORIES)
        qs.append({
            "question": f"Which of these best describes the book of {name}?",
            "options": opts, "correct_index": idx,
            "difficulty": "medium", "category": "Bible Books",
        })

    # T3: traditional author (medium/hard)
    famous = {"Genesis", "Exodus", "Psalms", "Proverbs", "Isaiah", "Matthew", "Mark", "Luke",
              "John", "Acts", "Romans", "Revelation", "Daniel", "Jonah"}
    for name, testament, cat, author in BOOKS:
        opts, idx = make_options(author, AUTHOR_POOL)
        diff = "medium" if name in famous else "hard"
        qs.append({
            "question": f"Who is traditionally credited as the author of the book of {name}?",
            "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Bible Books",
        })

    # T4: which book comes right after X (hard) - skip last book
    for i in range(len(BOOKS) - 1):
        name = BOOKS[i][0]
        nxt = BOOKS[i+1][0]
        opts, idx = make_options(nxt, names)
        qs.append({
            "question": f"Which book of the Bible comes immediately after {name}?",
            "options": opts, "correct_index": idx,
            "difficulty": "hard", "category": "Bible Books",
        })

    return qs

if __name__ == "__main__":
    import json
    data = build()
    print(len(data))
    print(json.dumps(data[:3], indent=2))
