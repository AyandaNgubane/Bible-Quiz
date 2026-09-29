import random
random.seed(45)

NAMES = ["Othniel", "Ehud", "Shamgar", "Deborah", "Gideon", "Tola", "Jair",
         "Jephthah", "Ibzan", "Elon", "Abdon", "Samson"]

FACTS = [
    ("Deborah", "Which judge of Israel was also a prophetess and led Barak's army to victory over Sisera?", "medium"),
    ("Gideon", "Which judge tested God's will using a fleece of wool and defeated the Midianites with only three hundred men?", "medium"),
    ("Samson", "Which judge, a Nazirite from birth, lost his great strength after Delilah had his hair cut?", "easy"),
    ("Samson", "Which judge killed a thousand Philistines with the jawbone of a donkey?", "medium"),
    ("Samson", "Which judge pulled down the pillars of the temple of Dagon, killing himself along with the Philistines inside?", "medium"),
    ("Ehud", "Which left-handed judge killed Eglon, the king of Moab, with a hidden dagger?", "hard"),
    ("Jephthah", "Which judge made a rash vow to the Lord that led to great sorrow involving his own daughter?", "hard"),
    ("Othniel", "Who was the first judge raised up by God after the death of Joshua?", "hard"),
    ("Shamgar", "Which judge killed six hundred Philistines with an ox goad?", "hard"),
    ("Barak", "Which military commander was called by Deborah to lead Israel's army against Sisera?", "medium"),
]

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def build():
    qs = []
    pool = NAMES + ["Barak"]
    for correct, question, diff in FACTS:
        opts, idx = make_options(correct, pool)
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Judges of Israel",
        })
    return qs

if __name__ == "__main__":
    print(len(build()))
