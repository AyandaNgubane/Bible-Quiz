import random
random.seed(60)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="Pentecostal Doctrine"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("According to Ephesians 6:12, believers wrestle not against flesh and blood but against what?", "Principalities, powers, and spiritual wickedness in high places", ["Only human enemies", "Sickness alone", "Poverty alone"], "medium")
add("What piece of the armour of God is described as being able to quench \"all the fiery darts of the wicked\"?", "The shield of faith", ["The helmet of salvation", "The breastplate of righteousness", "The belt of truth"], "medium")
add("In deliverance ministry, what authority did Jesus give His disciples over unclean spirits, according to the Gospels?", "Power to cast them out", ["No authority; only Jesus could do this", "Authority only after His resurrection", "Authority only over the twelve's own household"], "medium")
add("What did Jesus say His followers would do in His name, according to the Great Commission in Mark 16?", "Cast out devils and speak with new tongues", ["Perform political reforms", "Build large temples", "Avoid all confrontation with evil"], "medium")
add("What common Charismatic term describes lifting hands, singing, and shouting in exuberant praise to God?", "Praise and worship", ["Liturgy", "Meditation only", "Silent contemplation only"], "easy")
add("According to Psalm 150, with what instruments and actions are believers encouraged to praise the Lord?", "Trumpet, timbrel, dance, stringed instruments, and cymbals", ["Only silence", "Only spoken word", "Only written prayers"], "medium")
add("What Hebrew word, common in Pentecostal worship, means \"praise\" and is the root of \"hallelujah\"?", "Halal", ["Selah", "Shalom", "Amen"], "hard")
add("According to 1 Thessalonians 5:19-20, believers are told not to quench the Spirit and not to do what to prophesyings?", "Despise them", ["Encourage them constantly without testing", "Write them down as scripture", "Ignore the Spirit entirely"], "medium")
add("According to 1 Thessalonians 5:21, what should believers do with all things, including prophetic words?", "Prove (test) all things and hold fast to what is good", ["Accept everything without question", "Reject everything automatically", "Ignore anything unfamiliar"], "hard")
add("What term describes a believer sensing God speaking directly to their heart or through others, common in Charismatic practice?", "A prophetic word or leading of the Spirit", ["A creed", "A dogma", "A liturgy"], "medium")
add("According to Acts 2:17, in the last days God said He would pour out His Spirit, and sons and daughters would do what?", "Prophesy", ["Only remain silent", "Only fast", "Only build temples"], "medium")
add("What is commonly called the \"laying on of hands,\" practiced for healing, impartation, and commissioning in ministry?", "Laying on of hands", ["Anointing of kings only", "Excommunication", "Genuflection"], "easy")
add("According to Acts 13:2-3, what did the church at Antioch do before sending Paul and Barnabas out as missionaries?", "Fasted, prayed, and laid hands on them", ["Voted by ballot only", "Sent them with no preparation", "Required years of seminary training first"], "medium")
add("What does the term \"anointing\" commonly refer to in Pentecostal/Charismatic teaching?", "The empowering presence of the Holy Spirit for ministry", ["A formal university degree", "A title given only to bishops", "A tax exemption"], "medium")
add("Which Old Testament practice of pouring oil on someone's head to set them apart for God's service is echoed in the term \"anointing\"?", "Anointing with oil for kings, priests, and prophets", ["Circumcision", "Tithing", "Sabbath rest"], "medium")
add("According to James 5:16, believers are encouraged to confess their faults one to another and to do what for one another?", "Pray for one another, that they may be healed", ["Judge one another harshly", "Avoid one another", "Report one another to authorities"], "medium")
add("What New Testament word describes gathering together regularly for worship, teaching, and fellowship, warned not to be forsaken in Hebrews 10:25?", "Assembling together", ["Isolation", "Silence", "Fasting alone"], "medium")
add("According to Hebrews 10:25, believers should not forsake the assembling of themselves together, but exhort one another, especially as they see what approaching?", "The day (of the Lord) approaching", ["The end of the harvest", "A new moon festival", "A census"], "hard")
add("What term describes the belief that supernatural spiritual gifts, including healing and tongues, continue to operate in the church today?", "Continuationism (a core Pentecostal/Charismatic belief)", ["Cessationism", "Deism", "Universalism"], "hard")
add("According to Pentecostal missions emphasis, what did Jesus promise would accompany the preaching of the gospel, per Mark 16:20?", "The Lord working with them, confirming the word with signs following", ["Immediate wealth for all preachers", "Freedom from all opposition", "Instant conversion of entire nations"], "medium")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
