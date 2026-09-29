import random
random.seed(43)

UNITED = ["Saul", "David", "Solomon"]
ISRAEL = ["Jeroboam I", "Nadab", "Baasha", "Elah", "Zimri", "Omri", "Ahab", "Ahaziah",
          "Jehoram", "Jehu", "Jehoahaz", "Jehoash", "Jeroboam II", "Zechariah",
          "Shallum", "Menahem", "Pekahiah", "Pekah", "Hoshea"]
JUDAH = ["Rehoboam", "Abijah", "Asa", "Jehoshaphat", "Jehoram of Judah", "Ahaziah of Judah",
         "Athaliah", "Joash", "Amaziah", "Uzziah", "Jotham", "Ahaz", "Hezekiah",
         "Manasseh", "Amon", "Josiah", "Jehoahaz of Judah", "Jehoiakim", "Jehoiachin", "Zedekiah"]

ALL_KINGDOMS = (
    [(k, "the united Kingdom of Israel") for k in UNITED] +
    [(k, "the northern Kingdom of Israel") for k in ISRAEL] +
    [(k, "the southern Kingdom of Judah") for k in JUDAH]
)
KINGDOM_OPTIONS = ["the united Kingdom of Israel", "the northern Kingdom of Israel",
                   "the southern Kingdom of Judah", "the empire of Assyria"]

FACTS = [
    ("David", "Which king was described as \"a man after God's own heart\" and killed the giant Goliath as a young man?"),
    ("Solomon", "Which king asked God for wisdom and built the first Temple in Jerusalem?"),
    ("Saul", "Which king was Israel's first king, later consulted a medium at Endor, and lost the kingdom through disobedience?"),
    ("Ahab", "Which king of Israel married Jezebel and was confronted by the prophet Elijah over Baal worship?"),
    ("Hezekiah", "Which king of Judah had his life extended by fifteen years after praying, and removed the high places of idol worship?"),
    ("Josiah", "Which young king of Judah found the Book of the Law in the Temple and led a great religious reform?"),
    ("Manasseh", "Which king of Judah was carried away captive to Babylon, humbled himself, and was later restored to his throne?"),
    ("Rehoboam", "Under which king did the united kingdom of Israel split into two kingdoms?"),
    ("Jehu", "Which king of Israel was known for driving his chariot furiously and wiped out the house of Ahab?"),
    ("Uzziah", "Which king of Judah was struck with leprosy after unlawfully burning incense in the Temple?"),
    ("Nebuchadnezzar", "Which Babylonian king had the dream of a great statue and later ate grass like an ox as judgment for his pride?"),
    ("Belshazzar", "Which king saw a mysterious hand write on the wall of his palace during a great feast?"),
    ("Zedekiah", "Which was the last king of Judah before the Babylonian captivity began?"),
    ("Herod", "Which ruler ordered the massacre of infant boys in Bethlehem after Jesus was born?"),
    ("Jehoshaphat", "Which king of Judah sent out singers ahead of his army and won a battle without fighting?"),
]

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def build():
    qs = []
    for king, kingdom in ALL_KINGDOMS:
        opts, idx = make_options(kingdom, KINGDOM_OPTIONS)
        display = king.replace(" of Judah", "")
        qs.append({
            "question": f"King {display} reigned over which kingdom?",
            "options": opts, "correct_index": idx,
            "difficulty": "medium" if king in UNITED else "hard",
            "category": "Kings of Israel & Judah",
        })

    name_pool = [k for k, _ in ALL_KINGDOMS] + ["Nebuchadnezzar", "Belshazzar", "Herod", "Cyrus", "Darius"]
    for correct, question in FACTS:
        opts, idx = make_options(correct, list(set(name_pool)))
        qs.append({
            "question": question,
            "options": opts, "correct_index": idx,
            "difficulty": "medium",
            "category": "Kings of Israel & Judah",
        })
    return qs

if __name__ == "__main__":
    d = build()
    print(len(d))
