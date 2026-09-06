import random
random.seed(51)

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

PLACES = ["The Garden of Eden", "Mount Ararat", "Ur of the Chaldees", "Canaan", "Egypt",
          "Mount Sinai", "Jericho", "Jerusalem", "Bethlehem", "Nazareth", "Bethel",
          "Bethany", "Capernaum", "The Sea of Galilee", "The Jordan River", "The Dead Sea",
          "Babylon", "Nineveh", "Damascus", "Mount Carmel", "The Mount of Olives",
          "Golgotha", "The Garden of Gethsemane", "Patmos", "Antioch", "Corinth",
          "Ephesus", "Philippi", "Tarsus", "Mount Sinai (Horeb)", "Shiloh", "Hebron"]

FACTS = [
    ("The Garden of Eden", "Where did God place Adam and Eve after creating them?", "easy"),
    ("Mount Ararat", "Where did Noah's ark come to rest after the flood?", "medium"),
    ("Ur of the Chaldees", "From which city did God call Abraham to leave his home and family?", "hard"),
    ("Mount Sinai", "At which mountain did God give Moses the Ten Commandments?", "easy"),
    ("Jericho", "Which city's walls fell down flat after the Israelites marched around it seven times?", "easy"),
    ("Bethlehem", "In which town was Jesus born, fulfilling the prophecy of Micah?", "easy"),
    ("Nazareth", "In which town did Jesus grow up, so that He was called a Nazarene?", "easy"),
    ("Capernaum", "Which town by the Sea of Galilee served as the base for much of Jesus' ministry?", "medium"),
    ("The Sea of Galilee", "On which body of water did Jesus calm the storm and walk on the waves?", "medium"),
    ("The Jordan River", "In which river was Jesus baptized by John the Baptist?", "easy"),
    ("Babylon", "To which empire were the people of Judah carried away captive under Nebuchadnezzar?", "medium"),
    ("Nineveh", "To which great city was Jonah sent to preach repentance?", "medium"),
    ("Damascus", "On the road to which city did Saul encounter a blinding light and hear the voice of Jesus?", "medium"),
    ("Mount Carmel", "On which mountain did Elijah challenge the prophets of Baal to a contest by fire?", "medium"),
    ("The Mount of Olives", "From which mountain did Jesus ascend into heaven after His resurrection?", "medium"),
    ("Golgotha", "At which place, whose name means \"the place of a skull,\" was Jesus crucified?", "medium"),
    ("The Garden of Gethsemane", "In which garden did Jesus pray in agony the night before His crucifixion?", "medium"),
    ("Patmos", "On which island was John exiled when he received the vision of Revelation?", "hard"),
    ("Antioch", "In which city were believers first called \"Christians\"?", "hard"),
    ("Corinth", "To which sinful, thriving Greek city did Paul write two well-known epistles?", "medium"),
    ("Ephesus", "In which city did Paul minister for about three years and later write an epistle named for the city?", "medium"),
    ("Tarsus", "In which city was the apostle Paul born?", "hard"),
    ("Shiloh", "Where was the tabernacle set up for many years before the Temple was built in Jerusalem?", "hard"),
    ("Hebron", "In which city did David first reign as king before later moving his throne to Jerusalem?", "hard"),
    ("Egypt", "In which land did Joseph rise to become second-in-command under Pharaoh?", "easy"),
    ("Bethany", "In which village did Jesus raise Lazarus from the dead?", "medium"),
    ("The Dead Sea", "Which extremely salty sea, where nothing can live, lies near the site of Sodom and Gomorrah?", "hard"),
    ("Bethel", "Where did Jacob dream of a ladder reaching to heaven with angels ascending and descending?", "hard"),
]

def build():
    qs = []
    for correct, question, diff in FACTS:
        opts, idx = make_options(correct, PLACES)
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Places in the Bible",
        })
    return qs

if __name__ == "__main__":
    print(len(build()))
