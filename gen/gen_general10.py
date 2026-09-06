import random
random.seed(65)

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
add("Which feast, also called the Feast of Trumpets, is marked by the blowing of trumpets and is a forerunner to the Jewish New Year?", "The Feast of Trumpets", ["Passover", "Pentecost", "The Day of Atonement"], "hard", C)
add("Which covenant did God make with David, promising his throne would be established forever, ultimately fulfilled in Christ?", "The Davidic Covenant", ["The Abrahamic Covenant", "The Mosaic Covenant", "The Noahic Covenant"], "hard", C)
add("Which covenant, made at Mount Sinai, gave Israel the Law through Moses?", "The Mosaic Covenant", ["The Davidic Covenant", "The Abrahamic Covenant", "The New Covenant"], "medium", C)
add("Which covenant promised Abraham that his descendants would be as numerous as the stars and that all nations would be blessed through him?", "The Abrahamic Covenant", ["The Mosaic Covenant", "The Davidic Covenant", "The New Covenant"], "medium", C)
add("Under the New Covenant, believers are told salvation is received by grace through what, rather than through animal sacrifice?", "Faith in Jesus Christ", ["Circumcision", "Temple offerings", "Ceremonial washing"], "medium", C)

C2 = "New Testament Epistles"
add("Which epistle instructs wives and husbands, parents and children, and masters and servants on household relationships, alongside the armour of God?", "Ephesians", ["Colossians", "1 Peter", "Titus"], "medium", C2)
add("Which epistle warns against being taken captive through philosophy and vain deceit, emphasizing the supremacy of Christ?", "Colossians", ["Ephesians", "Philippians", "Galatians"], "hard", C2)
add("Which epistle addresses concerns about believers who had died before Christ's return, comforting the church about the resurrection?", "1 Thessalonians", ["2 Thessalonians", "1 Corinthians", "Hebrews"], "hard", C2)
add("Which short epistle to a young co-worker outlines qualifications for elders and warns against false teachers in Crete?", "Titus", ["1 Timothy", "2 Timothy", "Philemon"], "hard", C2)
add("Which epistle contains the famous \"faith chapter,\" listing many Old Testament heroes of faith?", "Hebrews (chapter 11)", ["Romans", "James", "1 Peter"], "medium", C2)
add("Which epistle teaches about elders, humility, and casting all your care upon God because He cares for you?", "1 Peter", ["2 Peter", "James", "Jude"], "medium", C2)
add("Which epistle warns about scoffers in the last days and reminds readers that a day is like a thousand years to the Lord?", "2 Peter", ["1 Peter", "Jude", "Revelation"], "hard", C2)

C3 = "Wisdom Literature"
add("According to Ecclesiastes 3, there is a time for every purpose; what does it say there is \"a time to\" do, alongside a time to weep?", "A time to laugh", ["A time to sin", "A time to hate God", "A time to disbelieve"], "medium", C3)
add("Which wisdom book contains the phrase, \"Two are better than one... for if they fall, the one will lift up his fellow\"?", "Ecclesiastes", ["Proverbs", "Job", "Psalms"], "hard", C3)
add("According to Proverbs, what happens to plans when there is no counsel, compared to when there are many counselors?", "Plans fail without counsel but succeed with many counselors", ["Plans always succeed regardless", "Plans always fail regardless", "Counsel makes no difference"], "hard", C3)
add("Which wisdom book describes a virtuous woman whose \"price is far above rubies\"?", "Proverbs (chapter 31)", ["Song of Solomon", "Ecclesiastes", "Ruth"], "medium", C3)
add("Job's three friends came to comfort him; name one of them.", "Eliphaz (or Bildad, or Zophar)", ["Nathan", "Gad", "Ahithophel"], "hard", C3)

C4 = "Famous Verses & Sayings"
add("Which verse says, \"Fear thou not; for I am with thee: be not dismayed; for I am thy God\"?", "Isaiah 41:10", ["Joshua 1:9", "Psalm 27:1", "Deuteronomy 31:6"], "hard", C4)
add("Which verse says, \"This is the day which the LORD hath made; we will rejoice and be glad in it\"?", "Psalm 118:24", ["Psalm 23:1", "Psalm 100:1", "Psalm 91:1"], "hard", C4)
add("Which verse says, \"Draw nigh to God, and he will draw nigh to you\"?", "James 4:8", ["1 John 1:9", "Hebrews 11:6", "Psalm 34:18"], "hard", C4)
add("Which verse says, \"If we confess our sins, he is faithful and just to forgive us our sins\"?", "1 John 1:9", ["James 4:8", "Romans 10:9", "Ephesians 2:8"], "medium", C4)
add("Which verse says, \"But without faith it is impossible to please him\"?", "Hebrews 11:6", ["Romans 10:17", "Galatians 2:20", "James 2:17"], "hard", C4)

C5 = "Judges of Israel"
add("Which judge of Israel is remembered for a famous riddle he posed at his wedding feast about honey from a lion's carcass?", "Samson", ["Gideon", "Ehud", "Jephthah"], "medium", C5)
add("Which judge's mother was visited by an angel who instructed that her son should be a Nazirite from birth?", "Samson", ["Samuel", "Gideon", "Jephthah"], "medium", C5)
add("Which judge asked God to confirm his call by making dew appear on a fleece, but not on the ground around it, and then the reverse?", "Gideon", ["Samson", "Ehud", "Deborah"], "medium", C5)

C6 = "Numbers, Family & Genealogy"
add("Who was the mother of Cain and Abel?", "Eve", ["Sarah", "Rebekah", "Naamah"], "easy", C6)
add("Which patriarch had two wives, Leah and Rachel, who were sisters?", "Jacob", ["Abraham", "Isaac", "Esau"], "medium", C6)
add("Who was the father of the twelve tribal patriarchs of Israel?", "Jacob (Israel)", ["Isaac", "Abraham", "Joseph"], "easy", C6)
add("Which son of Jacob became the ancestor of the tribe from which King David and Jesus descended?", "Judah", ["Reuben", "Levi", "Benjamin"], "medium", C6)

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
