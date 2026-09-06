import random
random.seed(47)

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

LISTS = {
    "plagues": {
        "members": ["Blood", "Frogs", "Lice", "Flies", "Livestock disease", "Boils",
                    "Hail", "Locusts", "Darkness", "Death of the firstborn"],
        "not_members": ["Earthquake", "Famine of forty years", "Fire from heaven on Sodom", "A great flood"],
        "count": 10, "name": "the plagues God sent on Egypt",
    },
    "tribes": {
        "members": ["Reuben", "Simeon", "Levi", "Judah", "Dan", "Naphtali", "Gad",
                    "Asher", "Issachar", "Zebulun", "Ephraim", "Manasseh", "Benjamin"],
        "not_members": ["Moab", "Edom", "Midian", "Philistia"],
        "count": 12, "name": "the tribes of Israel",
    },
    "commandments": {
        "members": ["No other gods before Me", "No graven images", "Honour thy father and mother",
                    "Thou shalt not kill", "Thou shalt not commit adultery", "Thou shalt not steal",
                    "Thou shalt not bear false witness", "Remember the sabbath day", "Thou shalt not covet"],
        "not_members": ["Love thy neighbour as thyself (as one of the ten)", "Tithe ten percent of thine increase",
                        "Be baptized in water", "Speak in tongues"],
        "count": 10, "name": "the Ten Commandments",
    },
    "fruit": {
        "members": ["Love", "Joy", "Peace", "Longsuffering", "Gentleness", "Goodness",
                    "Faith", "Meekness", "Temperance"],
        "not_members": ["Wisdom", "Prophecy", "Healing", "Tongues"],
        "count": 9, "name": "the fruit of the Spirit listed in Galatians 5",
    },
    "giftsofspirit": {
        "members": ["Word of wisdom", "Word of knowledge", "Faith", "Gifts of healing",
                    "Working of miracles", "Prophecy", "Discerning of spirits",
                    "Divers kinds of tongues", "Interpretation of tongues"],
        "not_members": ["Apostleship (as one of the nine)", "Giving", "Mercy", "Teaching (as one of the nine)"],
        "count": 9, "name": "the gifts of the Spirit listed in 1 Corinthians 12",
    },
    "beatitudes": {
        "members": ["Blessed are the poor in spirit", "Blessed are they that mourn",
                    "Blessed are the meek", "Blessed are they which do hunger and thirst after righteousness",
                    "Blessed are the merciful", "Blessed are the pure in heart",
                    "Blessed are the peacemakers", "Blessed are they which are persecuted for righteousness' sake"],
        "not_members": ["Blessed are the rich", "Blessed are the proud", "Blessed are the mighty"],
        "count": 8, "name": "the Beatitudes in the Sermon on the Mount",
    },
    "churches": {
        "members": ["Ephesus", "Smyrna", "Pergamos", "Thyatira", "Sardis", "Philadelphia", "Laodicea"],
        "not_members": ["Corinth", "Rome", "Antioch", "Colosse"],
        "count": 7, "name": "the churches addressed in Revelation chapters 2 and 3",
    },
    "armor": {
        "members": ["Belt of truth", "Breastplate of righteousness", "Shoes of the gospel of peace",
                    "Shield of faith", "Helmet of salvation", "Sword of the Spirit"],
        "not_members": ["Crown of glory", "Robe of righteousness", "Staff of authority"],
        "count": 6, "name": "the armour of God in Ephesians 6",
    },
    "fivefold": {
        "members": ["Apostles", "Prophets", "Evangelists", "Pastors", "Teachers"],
        "not_members": ["Deacons (as one of the five)", "Elders (as one of the five)", "Bishops (as one of the five)"],
        "count": 5, "name": "the fivefold ministry gifts listed in Ephesians 4",
    },
}

def build():
    qs = []
    for key, d in LISTS.items():
        # how many
        opts, idx = make_options(str(d["count"]), [str(x) for x in [d["count"]-2, d["count"]-1, d["count"], d["count"]+1, d["count"]+2]][:4])
        qs.append({
            "question": f"How many are listed among {d['name']}?",
            "options": opts, "correct_index": idx,
            "difficulty": "medium", "category": "Bible Lists & Numbers",
        })
        # which IS a member
        member_pick = d["members"][0]
        opts, idx = make_options(member_pick, [member_pick] + d["not_members"][:3])
        qs.append({
            "question": f"Which of these IS one of {d['name']}?",
            "options": opts, "correct_index": idx,
            "difficulty": "medium", "category": "Bible Lists & Numbers",
        })
        # which is NOT a member (rotate through a couple of members as correct distractor set)
        for i, notm in enumerate(d["not_members"][:2]):
            sample_members = d["members"][i*2:i*2+3] if len(d["members"]) >= i*2+3 else d["members"][:3]
            opts, idx = make_options(notm, sample_members + [notm])
            qs.append({
                "question": f"Which of these is NOT one of {d['name']}?",
                "options": opts, "correct_index": idx,
                "difficulty": "hard", "category": "Bible Lists & Numbers",
            })

    # standalone number facts
    STANDALONE = [
        ("How many books are in the entire Bible (Old and New Testaments combined)?", "66", ["39", "27", "73"], "easy"),
        ("How many books are in the Old Testament?", "39", ["27", "66", "46"], "medium"),
        ("How many books are in the New Testament?", "27", ["39", "66", "21"], "medium"),
        ("How many Gospels are there in the New Testament?", "4", ["3", "5", "12"], "easy"),
        ("How many original apostles did Jesus choose?", "12", ["10", "70", "7"], "easy"),
        ("How many days and nights did it rain during the flood of Noah?", "40", ["7", "100", "14"], "easy"),
        ("How many years did the Israelites wander in the wilderness?", "40", ["7", "70", "100"], "easy"),
        ("How many days did Jesus fast in the wilderness before being tempted by the devil?", "40", ["3", "7", "12"], "easy"),
        ("How many days did Jesus remain on earth after His resurrection before ascending to heaven?", "40", ["3", "50", "10"], "medium"),
        ("How many years, according to a common count, did the Israelites live in Egypt?", "430", ["40", "400", "70"], "hard"),
        ("How many days was Lazarus in the tomb before Jesus raised him?", "4", ["3", "7", "1"], "medium"),
        ("How many years did Solomon take to build the first Temple?", "7", ["3", "40", "12"], "hard"),
        ("How many disciples did Jesus send out in pairs in Luke chapter 10, in addition to the twelve?", "70", ["12", "24", "144"], "hard"),
        ("According to the Bible, how many wise men are specifically numbered as visiting the infant Jesus?", "The Bible does not give a number", ["Three", "Twelve", "Two"], "hard"),
        ("How many times did Peter deny knowing Jesus before the rooster crowed?", "3", ["1", "7", "12"], "easy"),
        ("How many pieces of silver did Judas receive for betraying Jesus?", "30", ["10", "40", "12"], "medium"),
        ("How many lepers did Jesus heal who then returned to thank Him, out of ten?", "1", ["3", "10", "0"], "medium"),
        ("How many loaves and fishes fed the five thousand?", "5 loaves and 2 fishes", ["7 loaves and 2 fishes", "5 loaves and 7 fishes", "2 loaves and 5 fishes"], "medium"),
        ("How many baskets of leftovers were gathered after Jesus fed the five thousand?", "12", ["5", "7", "10"], "medium"),
        ("How many baskets of leftovers were gathered after Jesus fed the four thousand?", "7", ["12", "5", "4"], "hard"),
        ("How many years of famine did Joseph predict in Egypt, matched by seven years of plenty?", "7", ["3", "40", "10"], "medium"),
        ("How many sons did Jacob have, who became the fathers of the twelve tribes?", "12", ["10", "7", "13"], "easy"),
        ("How many chapters are in the book of Psalms?", "150", ["100", "119", "176"], "hard"),
        ("Which is the longest chapter in the Bible?", "Psalm 119", ["Psalm 150", "Genesis 1", "Revelation 1"], "hard"),
        ("How many days of creation are described in Genesis chapter 1?", "6 days of creation, resting on the 7th", ["7 days of creation", "5 days of creation", "3 days of creation"], "easy"),
    ]
    for q, correct, distractors, diff in STANDALONE:
        opts, idx = make_options(correct, [correct] + distractors)
        qs.append({
            "question": q, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Bible Lists & Numbers",
        })

    return qs

if __name__ == "__main__":
    print(len(build()))
