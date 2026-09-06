import random
random.seed(49)

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

PARABLES = [
    "The Prodigal Son", "The Good Samaritan", "The Sower", "The Mustard Seed",
    "The Lost Sheep", "The Lost Coin", "The Ten Virgins", "The Talents",
    "The Wheat and the Tares", "The Rich Man and Lazarus", "The Rich Fool",
    "The Pharisee and the Tax Collector", "The Unforgiving Servant",
    "The Labourers in the Vineyard", "The Wicked Husbandmen", "The Great Supper",
    "The Persistent Widow and the Unjust Judge", "The Two Sons", "The Leaven",
    "The Hidden Treasure", "The Pearl of Great Price", "The Net",
    "The Growing Seed", "The Lamp Under a Bushel", "The Wise and Foolish Builders",
    "The New Wine in Old Wineskins", "The Friend at Midnight", "The Good Shepherd",
    "The Barren Fig Tree", "The Sheep and the Goats",
]

FACT_QS = [
    ("The Prodigal Son", "In which parable does a wayward son squander his inheritance and is welcomed home by his forgiving father?", "medium", "easy"),
    ("The Good Samaritan", "In which parable does a man beaten by robbers get ignored by religious leaders but helped by an unlikely stranger?", "medium", "easy"),
    ("The Sower", "In which parable does seed fall on different types of ground: the wayside, rocky ground, thorns, and good soil?", "medium", "medium"),
    ("The Mustard Seed", "In which parable does the kingdom of heaven start as the smallest seed but grow into a large tree?", "medium", "medium"),
    ("The Lost Sheep", "In which parable does a shepherd leave ninety-nine sheep to search for one that is lost?", "medium", "medium"),
    ("The Lost Coin", "In which parable does a woman sweep her house diligently to find one lost piece of silver?", "medium", "hard"),
    ("The Ten Virgins", "In which parable do five wise and five foolish young women wait for a bridegroom with lamps of oil?", "medium", "medium"),
    ("The Talents", "In which parable does a master entrust his servants with money before going on a journey, and later judges how they used it?", "medium", "medium"),
    ("The Wheat and the Tares", "In which parable does an enemy sow weeds among good wheat, and both are left to grow until harvest?", "medium", "hard"),
    ("The Rich Man and Lazarus", "In which parable does a poor beggar covered in sores end up in Abraham's bosom while a rich man suffers in torment?", "medium", "medium"),
    ("The Rich Fool", "In which parable does a man build bigger barns to store his crops, only to die that very night?", "medium", "hard"),
    ("The Pharisee and the Tax Collector", "In which parable does a self-righteous man boast in prayer while another simply asks for mercy?", "medium", "medium"),
    ("The Unforgiving Servant", "In which parable is a servant forgiven a huge debt but then refuses to forgive a much smaller debt owed to him?", "medium", "medium"),
    ("The Labourers in the Vineyard", "In which parable do workers hired at the end of the day receive the same wage as those hired at dawn?", "medium", "hard"),
    ("The Wicked Husbandmen", "In which parable do tenant farmers kill the vineyard owner's servants and finally his son?", "medium", "hard"),
    ("The Great Supper", "In which parable do invited guests make excuses, so the host invites the poor and outcast to the feast instead?", "medium", "hard"),
    ("The Persistent Widow and the Unjust Judge", "In which parable does a widow's persistence finally wear down an uncaring judge?", "medium", "hard"),
    ("The Two Sons", "In which parable does one son say he will not work but does, while the other agrees but does not go?", "medium", "hard"),
    ("The Leaven", "In which parable is the kingdom of heaven compared to yeast that a woman mixes into a large batch of flour?", "medium", "hard"),
    ("The Hidden Treasure", "In which parable does a man sell everything he owns to buy a field containing hidden treasure?", "medium", "medium"),
    ("The Pearl of Great Price", "In which parable does a merchant sell all he has to buy one pearl of great value?", "medium", "medium"),
    ("The Net", "In which parable is the kingdom of heaven compared to a net that gathers both good and bad fish?", "medium", "hard"),
    ("The Wise and Foolish Builders", "In which parable does one man build his house on rock and another on sand?", "medium", "easy"),
    ("The Good Shepherd", "In which teaching does Jesus say He lays down His life for the sheep and knows them by name?", "medium", "medium"),
    ("The Barren Fig Tree", "In which parable does a gardener ask for one more year to fertilize a fruitless fig tree before it is cut down?", "medium", "hard"),
    ("The Sheep and the Goats", "In which teaching does the Son of Man separate the nations as a shepherd divides sheep from goats?", "medium", "medium"),
]

def build():
    qs = []
    for name, question, _diff, real_diff in FACT_QS:
        opts, idx = make_options(name, PARABLES)
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": real_diff, "category": "Parables of Jesus",
        })

    # main-point style questions
    LESSONS = [
        ("The Good Samaritan", "Which parable primarily teaches that we should show mercy to anyone in need, even those different from us?", "easy"),
        ("The Prodigal Son", "Which parable primarily teaches about a father's overflowing forgiveness for a repentant child?", "easy"),
        ("The Unforgiving Servant", "Which parable primarily teaches that we must forgive others as God has forgiven us?", "medium"),
        ("The Sower", "Which parable primarily teaches about how different hearts respond to the preached word of God?", "medium"),
        ("The Ten Virgins", "Which parable primarily teaches believers to stay spiritually ready and watchful for Christ's return?", "medium"),
        ("The Talents", "Which parable primarily teaches about being faithful stewards of what God has entrusted to us?", "medium"),
        ("The Lost Sheep", "Which parable primarily teaches that heaven rejoices over one sinner who repents?", "medium"),
        ("The Rich Fool", "Which parable primarily warns against greed and trusting in earthly riches instead of God?", "medium"),
        ("The Pharisee and the Tax Collector", "Which parable primarily teaches that humility before God matters more than self-righteous pride?", "medium"),
        ("The Wise and Foolish Builders", "Which parable primarily teaches that hearing God's word is not enough; we must also obey it?", "easy"),
    ]
    for name, question, diff in LESSONS:
        opts, idx = make_options(name, PARABLES)
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Parables of Jesus",
        })
    return qs

if __name__ == "__main__":
    print(len(build()))
