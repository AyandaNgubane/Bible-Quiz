import random
random.seed(48)

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

MIRACLES = [
    "Turning water into wine at Cana",
    "Feeding the five thousand",
    "Feeding the four thousand",
    "Walking on water",
    "Calming the storm on the Sea of Galilee",
    "Raising Lazarus from the dead",
    "Raising Jairus' daughter from the dead",
    "Raising the widow of Nain's son",
    "Healing the man born blind",
    "Healing blind Bartimaeus",
    "Healing the paralyzed man lowered through the roof",
    "Cleansing ten lepers",
    "Healing the woman with the issue of blood",
    "Healing the man with the withered hand",
    "Casting demons into a herd of swine",
    "Healing the deaf and mute man",
    "Healing the invalid at the pool of Bethesda",
    "Cursing the fig tree so it withered",
    "Healing Malchus' severed ear",
    "The miraculous catch of fish after the resurrection",
    "Healing the Canaanite woman's daughter",
    "Healing the centurion's servant",
    "Healing Peter's mother-in-law of a fever",
    "Providing a coin in a fish's mouth to pay the Temple tax",
    "Turning the disciples' empty nets into a great catch of fish",
]

FACT_QS = [
    ("Turning water into wine at Cana", "At which event did Jesus perform His first recorded miracle, turning water into wine?", "A wedding at Cana", ["A funeral in Bethany", "The feast of Pentecost", "A meal at Simon the Pharisee's house"], "medium"),
    ("Raising Lazarus from the dead", "Which miracle did Jesus perform after Lazarus had already been in the tomb four days?", "Raising Lazarus from the dead", ["Raising Jairus' daughter", "Healing the centurion's servant", "Calming the storm"], "medium"),
    ("Walking on water", "Which miracle involved Peter briefly walking toward Jesus before beginning to sink?", "Jesus walking on water", ["Jesus calming the storm", "The catch of fish", "Feeding the five thousand"], "medium"),
    ("Healing the man born blind", "In which miracle did Jesus make clay with spittle and put it on a man's eyes?", "Healing the man born blind", ["Healing blind Bartimaeus", "Healing the paralytic", "Healing the deaf and mute man"], "hard"),
    ("Healing the woman with the issue of blood", "Which woman was healed after secretly touching the hem of Jesus' garment in a crowd?", "The woman with the issue of blood", ["The Canaanite woman", "The widow of Nain", "The Samaritan woman at the well"], "medium"),
    ("Healing the paralyzed man lowered through the roof", "In which miracle did friends dig through a roof to lower a sick man down to Jesus?", "Healing the paralyzed man lowered through the roof", ["Healing the man with the withered hand", "Healing the invalid at Bethesda", "Healing the centurion's servant"], "medium"),
    ("Casting demons into a herd of swine", "In which miracle did Jesus send unclean spirits called \"Legion\" into a herd of pigs?", "Casting demons into a herd of swine", ["Healing the deaf and mute man", "Healing the epileptic boy", "Raising Lazarus"], "medium"),
    ("Healing the invalid at the pool of Bethesda", "Which man, sick for thirty-eight years, was healed by Jesus at a pool in Jerusalem?", "The invalid at the pool of Bethesda", ["Blind Bartimaeus", "The man with the withered hand", "The paralytic lowered through the roof"], "hard"),
    ("Feeding the five thousand", "Which miracle used five loaves and two small fishes to feed a great multitude?", "Feeding the five thousand", ["Feeding the four thousand", "The last supper", "The wedding at Cana"], "easy"),
    ("Providing a coin in a fish's mouth to pay the Temple tax", "In which miracle did Peter find a coin inside a fish's mouth?", "The coin in the fish's mouth for the Temple tax", ["The miraculous catch of fish", "Feeding the five thousand", "Turning water into wine"], "hard"),
    ("Healing Malchus' severed ear", "Whose ear, cut off by Peter in the garden of Gethsemane, did Jesus heal?", "Malchus, the servant of the high priest", ["Judas Iscariot", "Caiaphas the high priest", "Barabbas"], "hard"),
    ("Healing the centurion's servant", "Which miracle did Jesus perform from a distance after a Roman officer said, \"speak the word only\"?", "Healing the centurion's servant", ["Healing the nobleman's son", "Healing the Canaanite woman's daughter", "Raising the widow of Nain's son"], "medium"),
    ("Cursing the fig tree so it withered", "Which miracle did Jesus perform on a tree that had leaves but no fruit?", "Cursing the fig tree", ["The parable of the barren fig tree", "Cleansing the Temple", "Calming the storm"], "hard"),
    ("Raising the widow of Nain's son", "In which miracle did Jesus stop a funeral procession and raise a widow's only son to life?", "Raising the widow of Nain's son", ["Raising Lazarus", "Raising Jairus' daughter", "Healing the centurion's servant"], "hard"),
]

def build():
    qs = []
    for correct, question, right_answer, wrongs, diff in FACT_QS:
        opts, idx = make_options(right_answer, [right_answer] + wrongs)
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Miracles of Jesus",
        })
    # "Which miracle" style questions matching a short description to the miracle name
    descs = [
        ("Turning water into wine at Cana", "Jesus turns water into wine"),
        ("Feeding the five thousand", "A boy's small lunch feeds a huge crowd with baskets left over"),
        ("Calming the storm on the Sea of Galilee", "Jesus rebukes the wind and waves and there is a great calm"),
        ("Cleansing ten lepers", "Ten men with leprosy are healed, but only one returns to give thanks"),
        ("Healing the man with the withered hand", "A man's shriveled hand is restored on the sabbath day"),
        ("Healing the deaf and mute man", "Jesus puts His fingers in a man's ears and touches his tongue to heal him"),
        ("The miraculous catch of fish after the resurrection", "The risen Jesus tells the disciples to cast their net on the right side of the boat"),
        ("Healing Peter's mother-in-law of a fever", "Jesus heals a fever simply by touching the sick woman's hand"),
        ("Healing the Canaanite woman's daughter", "A Gentile mother's persistent faith leads Jesus to heal her daughter from a distance"),
        ("Feeding the four thousand", "Seven loaves and a few small fishes feed a great crowd, with seven baskets left over"),
    ]
    for name, desc in descs:
        opts, idx = make_options(name, MIRACLES)
        qs.append({
            "question": f"Which miracle of Jesus is this: {desc}?",
            "options": opts, "correct_index": idx,
            "difficulty": "medium", "category": "Miracles of Jesus",
        })
    return qs

if __name__ == "__main__":
    print(len(build()))
