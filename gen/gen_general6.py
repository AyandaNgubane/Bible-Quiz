import random
random.seed(61)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="Who Said It?"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("Who said, \"Am I my brother's keeper?\" after being questioned about his brother's whereabouts?", "Cain", ["Abel", "Seth", "Esau"], "medium")
add("Who said, \"Here am I; send me,\" in response to God's call in a Temple vision?", "Isaiah", ["Jeremiah", "Ezekiel", "Samuel"], "medium")
add("Who said, \"Speak, LORD; for thy servant heareth,\" as a boy in the tabernacle?", "Samuel", ["David", "Josiah", "Isaiah"], "medium")
add("Who said, \"Whither thou goest, I will go; and where thou lodgest, I will lodge\"?", "Ruth", ["Naomi", "Esther", "Deborah"], "medium")
add("Who said, \"If I perish, I perish,\" before approaching the king uninvited to save her people?", "Esther", ["Ruth", "Abigail", "Deborah"], "medium")
add("Who said, \"Get thee behind me, Satan,\" rebuking a temptation to avoid the cross?", "Jesus (to Peter)", ["Peter", "Paul", "John the Baptist"], "medium")
add("Who said, \"Lord, to whom shall we go? thou hast the words of eternal life\"?", "Peter", ["John", "Thomas", "Andrew"], "medium")
add("Who said, \"My Lord and my God,\" upon seeing the risen Jesus' wounds?", "Thomas", ["Peter", "John", "Philip"], "easy")
add("Who said, \"Lord, remember me when thou comest into thy kingdom,\" while dying next to Jesus?", "The repentant thief on the cross", ["Barabbas", "Simon of Cyrene", "The centurion"], "medium")
add("Who cried out, \"Father, forgive them; for they know not what they do\" while being crucified?", "Jesus", ["Stephen", "Peter", "Paul"], "easy")
add("Who prayed, \"Lord, lay not this sin to their charge,\" while being stoned to death?", "Stephen", ["Peter", "James", "Paul"], "hard")
add("Who said, \"I have fought a good fight, I have finished my course, I have kept the faith\"?", "Paul", ["Peter", "James", "John"], "medium")
add("Who said, \"For to me to live is Christ, and to die is gain\"?", "Paul", ["Peter", "Timothy", "Silas"], "medium")
add("Who said to Jesus, \"Depart from me; for I am a sinful man, O Lord,\" after a miraculous catch of fish?", "Peter", ["Andrew", "James", "John"], "medium")
add("Who said, \"Behold the handmaid of the Lord; be it unto me according to thy word\"?", "Mary, the mother of Jesus", ["Elizabeth", "Anna", "Martha"], "easy")
add("Who said, \"Blessed art thou among women, and blessed is the fruit of thy womb\" to Mary?", "Elizabeth", ["Anna the prophetess", "Martha", "Mary Magdalene"], "medium")
add("Who said, \"Lord, if thou hadst been here, my brother had not died\"?", "Martha (and also Mary)", ["Mary Magdalene", "Salome", "Joanna"], "medium")
add("Who said, \"I believe; help thou mine unbelief,\" asking Jesus to heal his son?", "The father of a demon-possessed boy", ["A synagogue ruler", "A centurion", "A Pharisee"], "hard")
add("Who said, \"Thy will be done,\" while praying in great anguish the night before His crucifixion?", "Jesus", ["Peter", "John", "Judas"], "easy")
add("Who declared at Jesus' baptism, \"This is my beloved Son, in whom I am well pleased\"?", "God the Father (a voice from heaven)", ["John the Baptist", "An angel", "Moses"], "easy")
add("Who said, \"Choose you this day whom ye will serve...but as for me and my house, we will serve the LORD\"?", "Joshua", ["Moses", "Samuel", "Caleb"], "medium")
add("Who said, \"The LORD gave, and the LORD hath taken away; blessed be the name of the LORD\"?", "Job", ["Abraham", "David", "Solomon"], "medium")
add("Who said, \"Is there not a cause?\" before facing Goliath?", "David", ["Saul", "Jonathan", "Samuel"], "hard")
add("Who said, \"Thou art the man!\" confronting a king about his sin?", "Nathan the prophet", ["Samuel", "Elijah", "Isaiah"], "medium")
add("Who said, \"Let my people go,\" as God's demand delivered to Pharaoh?", "Moses", ["Aaron", "Joshua", "Joseph"], "easy")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
