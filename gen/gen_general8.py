import random
random.seed(63)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="General Bible Knowledge"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("Which Persian king issued the decree allowing the Jewish exiles to return and rebuild the Temple?", "Cyrus", ["Darius", "Xerxes (Ahasuerus)", "Artaxerxes"], "hard")
add("Which Persian king, also called Ahasuerus, made Esther his queen?", "Xerxes (Ahasuerus)", ["Cyrus", "Darius", "Nebuchadnezzar"], "medium")
add("Which Babylonian king had a golden statue built and threw three men into a fiery furnace for refusing to bow to it?", "Nebuchadnezzar", ["Belshazzar", "Cyrus", "Darius"], "medium")
add("Which three young Hebrew men were thrown into the fiery furnace for refusing to worship an idol?", "Shadrach, Meshach, and Abednego", ["Daniel and his two friends only", "Hananiah, Mishael, and Azariah using their birth names", "Ezra, Nehemiah, and Zerubbabel"], "medium")
add("Which Persian official signed a decree making it illegal to pray to anyone but the king, leading to Daniel's punishment?", "King Darius (pressured by his officials)", ["Cyrus", "Xerxes", "Nebuchadnezzar"], "hard")
add("Who was the Jewish cupbearer to a Persian king who was sent to rebuild the walls of Jerusalem?", "Nehemiah", ["Ezra", "Zerubbabel", "Mordecai"], "medium")
add("Who was the priest and scribe who led a return of exiles to Jerusalem and taught the Law to the people?", "Ezra", ["Nehemiah", "Haggai", "Zechariah"], "medium")
add("Who led the first group of exiles back to Jerusalem to begin rebuilding the Temple's foundation?", "Zerubbabel", ["Ezra", "Nehemiah", "Joshua the high priest"], "hard")
add("Which Jewish woman became queen of Persia and used her position to save her people from genocide?", "Esther", ["Ruth", "Rahab", "Deborah"], "easy")
add("Who was Esther's cousin and guardian who refused to bow to Haman and uncovered his plot?", "Mordecai", ["Haman", "Ahasuerus", "Memucan"], "medium")
add("Which official plotted to destroy the Jewish people in the book of Esther, but was hanged on his own gallows?", "Haman", ["Mordecai", "Memucan", "Bigthan"], "medium")

add("Which two apostles were sent by the Jerusalem church to check on the new Gentile believers in Antioch?", "Barnabas (who then fetched Paul/Saul)", ["Peter and John", "James and Jude", "Silas and Timothy"], "hard")
add("Which apostle had a rooftop vision of a great sheet with unclean animals, teaching him not to call any man common or unclean?", "Peter", ["Paul", "James", "John"], "medium")
add("Which council in Acts 15 decided that Gentile believers did not need to be circumcised to be saved?", "The Jerusalem Council", ["The Sanhedrin", "The Council of Nicaea", "The Council of Ephesus"], "hard")
add("Who accompanied Paul on his missionary journeys after a dispute caused Paul and Barnabas to separate?", "Silas", ["Timothy", "Titus", "Luke"], "hard")
add("Which physician and companion of Paul is traditionally credited with writing a Gospel and the book of Acts?", "Luke", ["Mark", "Timothy", "Titus"], "medium")
add("Which young man went with Paul and Barnabas partway on the first missionary journey, then left and returned home?", "John Mark", ["Timothy", "Silas", "Titus"], "hard")
add("Which coppersmith is mentioned by Paul as having done him much harm?", "Alexander the coppersmith", ["Demetrius", "Elymas", "Simon Magus"], "hard")
add("Which woman was a deaconess or servant of the church at Cenchrea, commended by Paul in Romans 16?", "Phebe", ["Priscilla", "Lydia", "Junia"], "hard")
add("Which married couple, tentmakers like Paul, hosted a church in their home and taught Apollos more accurately?", "Aquila and Priscilla", ["Ananias and Sapphira", "Andronicus and Junia", "Philemon and Apphia"], "medium")
add("Which husband and wife lied to the Holy Spirit about the price of land they sold, and died as a result?", "Ananias and Sapphira", ["Aquila and Priscilla", "Zacharias and Elizabeth", "Philemon and Apphia"], "medium")

add("Which prophet's message to Nineveh led to the entire city, including the king, repenting in sackcloth and ashes?", "Jonah", ["Nahum", "Amos", "Obadiah"], "easy")
add("Which prophet confronted King David through a parable about a rich man stealing a poor man's only lamb?", "Nathan", ["Gad", "Samuel", "Elijah"], "medium")
add("Which prophet anointed young David as future king while he was still tending sheep?", "Samuel", ["Nathan", "Gad", "Elijah"], "medium")
add("Which prophet was fed by ravens and later called down fire from heaven on Mount Carmel?", "Elijah", ["Elisha", "Isaiah", "Ezekiel"], "medium")
add("Which prophet's mantle fell to Elisha after being taken up to heaven?", "Elijah", ["Moses", "Samuel", "Isaiah"], "medium")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
