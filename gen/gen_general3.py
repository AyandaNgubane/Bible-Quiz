import random
random.seed(57)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

C = "Feasts & Covenants"
add("Which Jewish feast commemorates Israel's deliverance from the final plague on Egypt and the exodus?", "Passover", ["Pentecost", "The Feast of Tabernacles", "The Day of Atonement"], "easy", C)
add("Which feast, fifty days after Passover, became the occasion for the outpouring of the Holy Spirit?", "Pentecost (the Feast of Weeks)", ["The Feast of Trumpets", "Passover", "The Day of Atonement"], "medium", C)
add("Which feast commemorates Israel's forty years of wilderness wandering, involving living in temporary shelters?", "The Feast of Tabernacles (Booths)", ["Passover", "Pentecost", "The Day of Atonement"], "hard", C)
add("On which annual day did the Old Testament high priest enter the Most Holy Place to make atonement for the nation's sins?", "The Day of Atonement (Yom Kippur)", ["The Day of Trumpets", "The Sabbath", "Passover"], "hard", C)
add("What was the sign of God's covenant with Abraham given to every male descendant?", "Circumcision", ["Fasting", "Sacrifice of a lamb", "Wearing special garments"], "medium", C)
add("What covenant sign did God give Noah, promising never again to destroy the earth by flood?", "The rainbow", ["Circumcision", "The Sabbath", "The Passover lamb"], "easy", C)
add("Which meal, instituted by Jesus at the Last Supper, points to the New Covenant in His blood?", "Communion (the Lord's Supper)", ["Passover alone, unchanged", "The Feast of Trumpets", "A sin offering"], "medium", C)
add("According to Jeremiah 31, God promised to make a New Covenant with the houses of Israel and Judah, writing His law where?", "On their hearts", ["On stone tablets only", "On the Temple gates", "On scrolls kept by priests"], "hard", C)

C2 = "Famous Verses & Sayings"
add("Which verse begins, \"For God so loved the world, that he gave his only begotten Son\"?", "John 3:16", ["Romans 8:28", "Psalm 23:1", "Philippians 4:13"], "easy", C2)
add("Which Psalm begins, \"The LORD is my shepherd; I shall not want\"?", "Psalm 23", ["Psalm 91", "Psalm 100", "Psalm 119"], "easy", C2)
add("Which verse says, \"I can do all things through Christ which strengtheneth me\"?", "Philippians 4:13", ["Romans 8:28", "Galatians 2:20", "2 Timothy 1:7"], "medium", C2)
add("Which verse says, \"And we know that all things work together for good to them that love God\"?", "Romans 8:28", ["Jeremiah 29:11", "Proverbs 3:5", "Isaiah 40:31"], "medium", C2)
add("Which verse says, \"Trust in the LORD with all thine heart; and lean not unto thine own understanding\"?", "Proverbs 3:5", ["Psalm 37:4", "Isaiah 41:10", "Joshua 1:9"], "medium", C2)
add("Which verse says, \"For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil\"?", "Jeremiah 29:11", ["Isaiah 55:8", "Psalm 139:14", "Romans 12:2"], "medium", C2)
add("Which verse says, \"But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles\"?", "Isaiah 40:31", ["Psalm 40:1", "Habakkuk 3:19", "Isaiah 53:5"], "hard", C2)
add("Which shortest verse in the Bible simply says \"Jesus wept\"?", "John 11:35", ["John 3:16", "Luke 19:41", "Matthew 5:4"], "medium", C2)
add("Where in the Bible is the well-known \"love chapter\" found, describing charity as patient and kind?", "1 Corinthians 13", ["Romans 5", "Galatians 5", "1 John 4"], "medium", C2)
add("Which prayer, taught by Jesus to His disciples, begins \"Our Father which art in heaven\"?", "The Lord's Prayer", ["The Sinner's Prayer", "The Aaronic Blessing", "The Shema"], "easy", C2)
add("Which Old Testament blessing, given by priests, says \"The LORD bless thee, and keep thee\"?", "The Aaronic (priestly) Blessing", ["The Lord's Prayer", "The Beatitudes", "The Ten Commandments"], "hard", C2)
add("Which verse says, \"Be strong and of a good courage; be not afraid...for the LORD thy God is with thee\"?", "Joshua 1:9", ["Deuteronomy 31:6", "Psalm 27:1", "2 Chronicles 20:15"], "medium", C2)
add("Which verse commands, \"Be still, and know that I am God\"?", "Psalm 46:10", ["Psalm 23:1", "Psalm 100:1", "Psalm 121:1"], "medium", C2)
add("Which verse in Genesis records God's first recorded words in creation, \"Let there be light\"?", "Genesis 1:3", ["Genesis 1:1", "Genesis 2:7", "Genesis 1:26"], "medium", C2)

C3 = "New Testament Epistles"
add("Which epistle emphasizes justification by faith and not by works of the law, addressed to a church in Italy's capital?", "Romans", ["Galatians", "Hebrews", "James"], "medium", C3)
add("Which epistle corrects disorder and division in a Greek church, including teaching on the Lord's Supper and spiritual gifts?", "1 Corinthians", ["Philippians", "Colossians", "2 Thessalonians"], "medium", C3)
add("Which epistle strongly defends salvation by grace through faith against those requiring circumcision for salvation?", "Galatians", ["Ephesians", "Titus", "Hebrews"], "medium", C3)
add("Which epistle, written from prison, is often called the \"epistle of joy\"?", "Philippians", ["Colossians", "Philemon", "2 Timothy"], "medium", C3)
add("Which short epistle is Paul's personal appeal on behalf of a runaway slave named Onesimus?", "Philemon", ["Titus", "Jude", "3 John"], "hard", C3)
add("Which epistle teaches extensively about the superiority of Christ over angels, Moses, and the old priesthood?", "Hebrews", ["James", "1 Peter", "Romans"], "hard", C3)
add("Which epistle famously teaches that \"faith without works is dead\"?", "James", ["Romans", "Galatians", "1 John"], "medium", C3)
add("Which epistle was written to encourage persecuted believers scattered abroad, calling Christ a \"living stone\"?", "1 Peter", ["2 Peter", "1 John", "Jude"], "hard", C3)
add("Which epistle warns strongly against false teachers who had crept in unawares among believers?", "Jude", ["Titus", "Philemon", "2 John"], "hard", C3)
add("Which epistle teaches extensively about walking in the light and God's love, saying \"God is love\"?", "1 John", ["2 John", "3 John", "James"], "medium", C3)
add("Which epistle addresses a church described as \"lukewarm, neither cold nor hot,\" recorded in Revelation?", "The letter to the church in Laodicea", ["The letter to the church in Ephesus", "The letter to the church in Smyrna", "The letter to the church in Philadelphia"], "hard", C3)
add("Which of Paul's epistles was written to a young pastor and includes instructions on qualifications for elders and deacons?", "1 Timothy", ["Titus", "Philemon", "2 Thessalonians"], "medium", C3)
add("Which epistle contains Paul's final words before his execution, saying \"I have fought a good fight\"?", "2 Timothy", ["1 Timothy", "Titus", "Philippians"], "hard", C3)

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
