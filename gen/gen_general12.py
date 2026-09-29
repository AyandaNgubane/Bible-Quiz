import random
random.seed(67)

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
add("What animal did God provide as a substitute sacrifice for Isaac on Mount Moriah?", "A ram", ["A lamb", "A goat", "A bull"], "medium", C)
add("Which small insect does Proverbs point to as an example of wisdom and diligence for the sluggard to consider?", "The ant", ["The bee", "The spider", "The locust"], "medium", C)
add("What kind of tree did Zacchaeus climb to see Jesus?", "A sycamore tree", ["A fig tree", "An olive tree", "A palm tree"], "medium", C)
add("What did Jesus curse that then withered from the roots because it had no fruit?", "A fig tree", ["An olive tree", "A vine", "A sycamore tree"], "medium", C)
add("Which object did the woman with the issue of blood touch in order to be healed?", "The hem (border) of Jesus' garment", ["Jesus' hand", "Jesus' sandals", "A piece of the cross"], "medium", C)
add("What did the Philistines do with the Ark of the Covenant after capturing it, before returning it due to plagues?", "Placed it in the temple of their god Dagon", ["Destroyed it completely", "Buried it in the desert", "Gave it to another nation"], "hard", C)

C2 = "Worship & Praise"
add("What does the word \"hallelujah\" mean, a word of praise used throughout the Psalms and Revelation?", "\"Praise the LORD\"", ["\"God is good\"", "\"Peace be still\"", "\"Glory be to God\""], "easy", C2)
add("According to Psalm 100, believers are told to enter God's gates with what, and His courts with praise?", "Thanksgiving", ["Silence", "Fear", "Sacrifice alone"], "medium", C2)
add("What physical posture of worship is commonly mentioned in the Psalms, such as \"O come, let us worship and bow down\"?", "Bowing down / kneeling", ["Standing perfectly still", "Sitting cross-legged", "Lying face up"], "medium", C2)

C3 = "Judges of Israel"
add("Which judge led Israel and is remembered for the palm tree of Deborah, where she held court?", "Deborah", ["Jael", "Miriam", "Huldah"], "hard", C3)
add("Which woman, not herself a judge, killed the enemy commander Sisera by driving a tent peg through his temple?", "Jael", ["Deborah", "Delilah", "Rahab"], "hard", C3)

C4 = "Numbers, Family & Genealogy"
add("Who was the father of King David?", "Jesse", ["Boaz", "Obed", "Ruth's father"], "medium", C4)
add("Who was David's grandmother, a Moabite woman who married Boaz?", "Ruth", ["Naomi", "Rahab", "Orpah"], "medium", C4)
add("Which son of David tried to steal the kingdom from his father through rebellion, and died caught by his hair in a tree?", "Absalom", ["Amnon", "Adonijah", "Solomon"], "medium", C4)
add("Who was the son of Jonathan, lame in both feet, whom David showed kindness for his father's sake?", "Mephibosheth", ["Ziba", "Ish-bosheth", "Amasa"], "hard", C4)

C5 = "Pentecostal Doctrine"
add("What does Pentecostal teaching say happens to a believer's spirit at the moment of salvation, described as being made alive?", "It is regenerated (made spiritually alive) by the Holy Spirit", ["Nothing changes until baptism in water", "It becomes divine itself", "It is replaced entirely by an angel"], "medium", C5)
add("According to 2 Corinthians 5:17, if any man be in Christ, he is what?", "A new creature (creation); old things are passed away", ["Automatically wealthy", "Free from all future trials", "Instantly perfect in behavior"], "medium", C5)
add("According to Pentecostal teaching on prayer, in whose name are believers taught to pray, based on John 14:13-14?", "The name of Jesus", ["The name of an angel", "The name of a saint", "No specific name is needed"], "easy", C5)
add("What term describes God's supernatural provision for needs, often emphasized in Pentecostal teaching on faith and giving?", "Divine provision (God as Jehovah-Jireh, our provider)", ["Karma", "Fate", "Luck"], "medium", C5)
add("According to Hebrews 11:1, what is faith described as being?", "The substance of things hoped for, the evidence of things not seen", ["A feeling of certainty about the future", "A tradition passed down from elders", "A reward for good behavior"], "medium", C5)
add("What is the term for a believer's testimony of how they came to salvation and faith in Christ, often shared publicly in Pentecostal churches?", "A personal testimony", ["A creed", "A parable", "A eulogy"], "easy", C5)

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
