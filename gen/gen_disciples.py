import random
random.seed(44)

NAMES = ["Peter", "Andrew", "James son of Zebedee", "John", "Philip", "Bartholomew",
         "Thomas", "Matthew", "James son of Alphaeus", "Thaddaeus", "Simon the Zealot",
         "Judas Iscariot", "Matthias", "Paul", "Barnabas", "Nathanael"]

FACTS = [
    ("Peter", "Which apostle was originally named Simon, a fisherman, and denied knowing Jesus three times before the rooster crowed?", "medium"),
    ("Peter", "Which apostle preached the sermon at Pentecost after which about three thousand souls were saved?", "medium"),
    ("Andrew", "Which apostle was Peter's brother and first brought him to meet Jesus?", "medium"),
    ("James son of Zebedee", "Which apostle, brother of John, was the first of the twelve to be martyred, beheaded by King Herod?", "hard"),
    ("John", "Which apostle was known as the disciple whom Jesus loved and later wrote a Gospel and the book of Revelation?", "medium"),
    ("John", "Which apostle was exiled to the island of Patmos when he received the visions recorded in Revelation?", "medium"),
    ("Philip", "Which apostle brought Nathanael to meet Jesus, saying \"Come and see\"?", "hard"),
    ("Philip", "Which apostle asked Jesus, \"Lord, shew us the Father, and it sufficeth us\"?", "hard"),
    ("Bartholomew", "Nathanael is commonly identified with which apostle in the list of the twelve?", "hard"),
    ("Nathanael", "Which apostle did Jesus describe as \"an Israelite indeed, in whom is no guile\"?", "hard"),
    ("Thomas", "Which apostle is remembered for doubting the resurrection until he could see and touch Jesus' wounds?", "easy"),
    ("Matthew", "Which apostle was a tax collector before Jesus called him to follow Him, and later wrote a Gospel?", "medium"),
    ("James son of Alphaeus", "Which apostle is often called \"James the Less\" to distinguish him from James the brother of John?", "hard"),
    ("Thaddaeus", "Which apostle is also called \"Judas the son of James\" and is not to be confused with Judas Iscariot?", "hard"),
    ("Simon the Zealot", "Which apostle is identified in the Gospels by the political title \"the Zealot\"?", "hard"),
    ("Judas Iscariot", "Which of the twelve apostles betrayed Jesus for thirty pieces of silver?", "easy"),
    ("Judas Iscariot", "Which apostle served as treasurer for Jesus and the twelve, keeping the money bag?", "hard"),
    ("Matthias", "Which man was chosen by casting lots to replace Judas Iscariot among the twelve apostles?", "hard"),
    ("Paul", "Which apostle, formerly named Saul, was converted after seeing a bright light on the road to Damascus?", "easy"),
    ("Paul", "Which apostle wrote the majority of the New Testament epistles, including Romans and Galatians?", "medium"),
    ("Paul", "Which apostle described himself as having a \"thorn in the flesh\" given to keep him humble?", "hard"),
    ("Paul", "Which apostle was shipwrecked on the way to stand trial in Rome, as recorded in Acts?", "hard"),
    ("Barnabas", "Which man, whose name means \"son of encouragement,\" traveled with Paul on his first missionary journey?", "medium"),
]

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def build():
    qs = []
    for correct, question, diff in FACTS:
        opts, idx = make_options(correct, NAMES)
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Disciples & Apostles",
        })
    return qs

if __name__ == "__main__":
    print(len(build()))
