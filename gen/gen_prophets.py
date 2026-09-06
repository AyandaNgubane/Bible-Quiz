import random
random.seed(46)

MAJOR = ["Isaiah", "Jeremiah", "Ezekiel", "Daniel"]
MINOR = ["Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum",
         "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"]
ALL_PROPHETS = MAJOR + MINOR

FACTS = [
    ("Isaiah", "Which prophet foretold that a virgin would conceive and bear a son called Immanuel?", "medium"),
    ("Isaiah", "Which prophet wrote the \"suffering servant\" chapter describing one wounded for our transgressions?", "medium"),
    ("Jeremiah", "Which prophet, known as \"the weeping prophet,\" was thrown into a muddy cistern for his message?", "medium"),
    ("Jeremiah", "Which prophet foretold that Judah's captivity in Babylon would last seventy years?", "hard"),
    ("Ezekiel", "Which prophet saw a vision of a valley of dry bones coming to life?", "medium"),
    ("Ezekiel", "Which prophet, exiled in Babylon, saw visions of strange wheels and living creatures by the river Chebar?", "hard"),
    ("Daniel", "Which prophet was thrown into a den of lions for praying to God?", "easy"),
    ("Daniel", "Which prophet interpreted King Nebuchadnezzar's dream of a great statue made of different metals?", "medium"),
    ("Daniel", "Which prophet read the handwriting on the wall for King Belshazzar?", "medium"),
    ("Hosea", "Which prophet was told by God to marry an unfaithful woman as a picture of Israel's unfaithfulness?", "hard"),
    ("Joel", "Which prophet's words about God pouring out His Spirit on all flesh were quoted by Peter at Pentecost?", "medium"),
    ("Amos", "Which prophet was a shepherd from Tekoa who preached strongly against social injustice?", "hard"),
    ("Obadiah", "Which prophet wrote the shortest book in the Old Testament, a message of judgment against Edom?", "hard"),
    ("Jonah", "Which reluctant prophet was swallowed by a great fish after fleeing from God's call?", "easy"),
    ("Jonah", "Which prophet was sent to preach repentance to the wicked city of Nineveh?", "easy"),
    ("Micah", "Which prophet foretold that the Messiah would be born in Bethlehem?", "medium"),
    ("Nahum", "Which prophet pronounced judgment on the city of Nineveh a second time, foretelling its fall?", "hard"),
    ("Habakkuk", "Which prophet wrote the well-known phrase \"the just shall live by his faith\"?", "medium"),
    ("Zephaniah", "Which prophet warned of a coming \"day of the LORD\" of judgment during the reign of Josiah?", "hard"),
    ("Haggai", "Which prophet urged the returned exiles to stop delaying and finish rebuilding the Temple?", "hard"),
    ("Zechariah", "Which prophet foresaw the Messiah riding into Jerusalem on a donkey and being sold for thirty pieces of silver?", "hard"),
    ("Malachi", "Which is the last book of the Old Testament, addressing tithes and promising Elijah before the day of the LORD?", "medium"),
    ("Elijah", "Which Old Testament prophet challenged the prophets of Baal to a contest of fire on Mount Carmel?", "easy"),
    ("Elijah", "Which prophet was taken up to heaven in a whirlwind by a chariot of fire?", "medium"),
    ("Elisha", "Which prophet asked for a double portion of his master Elijah's spirit and later parted the Jordan River?", "hard"),
    ("Elisha", "Which prophet made a floating axe head rise from the water?", "hard"),
    ("Samuel", "Which prophet, dedicated to the Lord from childhood, anointed both Saul and David as king?", "medium"),
    ("Nathan", "Which prophet confronted King David about his sin with Bathsheba using a parable of a stolen lamb?", "hard"),
]

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def build():
    qs = []
    for name in ALL_PROPHETS:
        correct = "Major Prophet" if name in MAJOR else "Minor Prophet"
        opts, idx = make_options(correct, ["Major Prophet", "Minor Prophet", "Judge", "Apostle"])
        qs.append({
            "question": f"Is {name} classified among the Major Prophets or the Minor Prophets?",
            "options": opts, "correct_index": idx,
            "difficulty": "easy" if name in MAJOR else "medium",
            "category": "Prophets",
        })
    name_pool = ALL_PROPHETS + ["Elijah", "Elisha", "Samuel", "Nathan"]
    for correct, question, diff in FACTS:
        opts, idx = make_options(correct, list(set(name_pool)))
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Prophets",
        })
    return qs

if __name__ == "__main__":
    print(len(build()))
