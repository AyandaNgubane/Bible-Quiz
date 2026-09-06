import random
random.seed(58)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

C = "Animals & Objects in the Bible"
add("Which animal did God use to speak to the prophet Balaam and rebuke him?", "A donkey", ["A raven", "A serpent", "A lion"], "medium", C)
add("Which bird did Noah send out from the ark that did not return, having found dry land?", "A raven", ["A dove", "An eagle", "A sparrow"], "medium", C)
add("Which bird returned to Noah's ark carrying an olive leaf, showing the waters had receded?", "A dove", ["A raven", "A pigeon", "A swallow"], "easy", C)
add("Which creature swallowed the prophet Jonah when he fled from God's call?", "A great fish", ["A whale specifically named", "A sea serpent", "A crocodile"], "easy", C)
add("Which birds fed the prophet Elijah bread and meat while he hid by the brook Cherith?", "Ravens", ["Doves", "Eagles", "Sparrows"], "medium", C)
add("What kind of animals did Daniel face after being thrown into a den for praying to God?", "Lions", ["Wolves", "Bears", "Serpents"], "easy", C)
add("What creature bit Paul's hand after a shipwreck on Malta, though he suffered no harm?", "A venomous viper", ["A scorpion", "A wasp", "A spider"], "medium", C)
add("What insect plague, one of the ten plagues on Egypt, devoured all the crops?", "Locusts", ["Flies", "Lice", "Frogs"], "easy", C)
add("What animal did Abraham find caught in a thicket to sacrifice instead of his son Isaac?", "A ram", ["A goat", "A lamb", "A bull"], "medium", C)
add("According to Numbers 22, what was unusual about the donkey Balaam was riding?", "It spoke with a human voice", ["It could fly", "It never needed to eat", "It turned to stone"], "easy", C)

C2 = "Numbers, Family & Genealogy"
add("According to Matthew's genealogy, Jesus is described as the son of David and the son of whom?", "Abraham", ["Isaac", "Jacob", "Moses"], "medium", C2)
add("Who was Isaac's wife, chosen for him by Abraham's servant at a well?", "Rebekah", ["Rachel", "Leah", "Sarah"], "easy", C2)
add("Who were the twin sons of Isaac and Rebekah, one hairy and one smooth?", "Esau and Jacob", ["Cain and Abel", "Perez and Zerah", "Ephraim and Manasseh"], "medium", C2)
add("Who was Joseph's father among the twelve patriarchs?", "Jacob", ["Isaac", "Abraham", "Judah"], "easy", C2)
add("How many years did Joseph serve in Egypt, from being sold into slavery until reuniting with his father, roughly?", "About 22 years", ["About 5 years", "About 40 years", "About 70 years"], "hard", C2)
add("Who was the mother of John the Baptist?", "Elizabeth", ["Mary", "Anna", "Salome"], "medium", C2)
add("Who was the father of John the Baptist, a priest who was struck mute for doubting an angel's message?", "Zacharias (Zechariah)", ["Zebedee", "Joseph", "Simeon"], "medium", C2)
add("Which two of Jesus' apostles were brothers who were fishermen, sons of Zebedee?", "James and John", ["Peter and Andrew", "Philip and Bartholomew", "James and Judas"], "medium", C2)
add("Which two of Jesus' apostles were brothers, sons of Jonah/John, also fishermen?", "Peter and Andrew", ["James and John", "Matthew and Thomas", "Simon and Judas"], "medium", C2)
add("What was the relationship between Mary the mother of Jesus and Elizabeth the mother of John the Baptist?", "They were relatives (cousins)", ["They were sisters", "They were mother and daughter", "They were unrelated"], "medium", C2)

C3 = "Wisdom Literature"
add("Which book of wisdom literature begins, \"The fear of the LORD is the beginning of knowledge\"?", "Proverbs", ["Ecclesiastes", "Job", "Song of Solomon"], "medium", C3)
add("Which book says, \"Vanity of vanities; all is vanity,\" reflecting on the meaninglessness of life without God?", "Ecclesiastes", ["Proverbs", "Job", "Lamentations"], "medium", C3)
add("Which book records a righteous man's suffering and dialogue with friends about why the innocent suffer?", "Job", ["Ecclesiastes", "Lamentations", "Proverbs"], "medium", C3)
add("Which wisdom book is largely a poetic celebration of love between a husband and wife?", "Song of Solomon", ["Proverbs", "Ecclesiastes", "Psalms"], "medium", C3)
add("Traditionally, who is credited with writing most of the book of Proverbs?", "Solomon", ["David", "Moses", "Ezra"], "easy", C3)
add("At the end of the book of Job, what did God do for Job after his time of suffering and testing?", "Restored his fortunes twofold", ["Left him in poverty", "Took his life", "Sent him into exile"], "medium", C3)
add("Which book of Psalms-like poetry expresses deep grief over the destruction of Jerusalem?", "Lamentations", ["Ecclesiastes", "Job", "Habakkuk"], "hard", C3)
add("According to Proverbs, what is described as \"the beginning of wisdom\"?", "The fear of the LORD", ["Great wealth", "Many years of age", "Political power"], "medium", C3)
add("Which book of the Bible has the most chapters?", "Psalms", ["Isaiah", "Genesis", "Jeremiah"], "hard", C3)
add("Which is the shortest chapter in the entire Bible?", "Psalm 117", ["Psalm 119", "Psalm 23", "Obadiah 1"], "hard", C3)

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
