import random
random.seed(66)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

C = "Wisdom Literature"
add("Besides David, which worship leader and seer is credited as author of a number of the Psalms, including Psalm 73?", "Asaph", ["Ethan", "Heman", "Jeduthun"], "hard", C)
add("Which group of Levitical singers is credited with writing several Psalms, including Psalm 42?", "The sons of Korah", ["The sons of Asaph", "The sons of Aaron", "The sons of Levi"], "hard", C)
add("Which leader is credited as the author of Psalm 90, a reflection on the brevity of human life?", "Moses", ["David", "Solomon", "Asaph"], "hard", C)
add("Which king wrote Psalm 51, a prayer of repentance after his sin with Bathsheba was exposed?", "David", ["Solomon", "Saul", "Hezekiah"], "medium", C)

C2 = "Worship & Praise"
add("Which instrument, associated with David, is frequently mentioned throughout the Psalms for worship?", "The harp", ["The trumpet", "The organ", "The piano"], "easy", C2)
add("According to 1 Samuel 16, what did David play to soothe King Saul when an evil spirit troubled him?", "The harp", ["The trumpet", "The timbrel", "The flute"], "medium", C2)
add("Which instrument was blown to signal the start of battles, feasts, and the Year of Jubilee?", "The trumpet (shofar)", ["The harp", "The cymbal", "The lyre"], "medium", C2)
add("What did Miriam and the women of Israel do with timbrels after crossing the Red Sea?", "Danced and sang in celebration and worship", ["Buried them in the sand", "Offered them as sacrifices", "Sold them for provisions"], "medium", C2)
add("According to 2 Chronicles 5, what happened in the Temple when the singers and musicians praised God with one voice?", "The glory of the LORD filled the house as a cloud", ["Nothing unusual happened", "The Temple was destroyed", "The priests were struck silent"], "hard", C2)
add("What Hebrew word appears often at the end of verses in Psalms, thought to indicate a pause for reflection or musical interlude?", "Selah", ["Hallelujah", "Hosanna", "Amen"], "medium", C2)
add("What does the word \"Hosanna,\" shouted by crowds as Jesus entered Jerusalem, mean?", "\"Save now\" or \"save, we pray\"", ["\"Praise the Lord\"", "\"Peace be with you\"", "\"He is risen\""], "hard", C2)

C3 = "Pentecostal Doctrine"
add("What term describes believers gathering specifically to seek God's presence through extended, passionate prayer and worship?", "A revival or a prayer meeting", ["A liturgy reading", "A catechism class", "A silent vigil only"], "medium", C3)
add("According to Pentecostal teaching, what is the primary purpose of the gift of tongues when interpreted in a public church gathering?", "To edify the church, just as prophecy does", ["To confuse the congregation", "To replace preaching entirely", "To prove someone's salvation"], "medium", C3)
add("What term describes a season of intense, focused prayer often combined with fasting to seek breakthrough or direction from God?", "A fast (or a season of fasting and prayer)", ["A sabbatical", "A pilgrimage", "A tithe"], "easy", C3)
add("According to Joel 2 and Acts 2, the outpouring of the Spirit was promised upon whom, regardless of age, gender, or social status?", "All flesh: sons and daughters, young and old, servants and handmaidens", ["Only priests and prophets", "Only kings and rulers", "Only men over forty"], "medium", C3)
add("What does the Pentecostal movement take its name from, the event recorded in Acts chapter 2?", "The Day of Pentecost, when the Holy Spirit was poured out", ["A city named Pentecost", "A book of the Bible", "A Roman festival"], "easy", C3)
add("According to Pentecostal belief, can a believer today still be filled and refilled with the Holy Spirit after their initial baptism in the Spirit?", "Yes, believers are encouraged to be continually filled with the Spirit", ["No, it can only happen once ever", "No, only apostles could be filled", "Yes, but only once per year"], "medium", C3)
add("What is the term for the practice of speaking a blessing or declaration of faith over a situation, common in Charismatic circles?", "A declaration of faith (confession)", ["A creed recitation", "A vow of silence", "A liturgical response"], "medium", C3)

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
