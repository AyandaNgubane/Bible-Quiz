import random
random.seed(54)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="Pentecostal Doctrine"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

# --- Godhead / Trinity ---
add("What term is commonly used for God existing as Father, Son, and Holy Ghost, three in one?", "The Godhead (Trinity)", ["Polytheism", "A created being", "An angelic order"], "easy")
add("At Jesus' baptism, which persons of the Godhead were all present and active?", "The Father spoke, the Son was baptized, and the Spirit descended as a dove", ["Only the Son appeared", "Only the Spirit appeared", "None were present"], "medium")
add("According to Matthew 28:19, believers are baptized in the name of the Father, the Son, and whom else?", "The Holy Ghost", ["The angels", "The apostles", "The prophets"], "easy")
add("Which title describes Jesus as being fully God and fully man?", "Immanuel, God with us", ["A created angel", "A prophet only", "A good moral teacher only"], "medium")
add("According to John 1:1, who was in the beginning with God and was God?", "The Word (Jesus Christ)", ["Moses", "The archangel Gabriel", "Adam"], "medium")

# --- Second Coming / End Times ---
add("Which New Testament epistle describes believers being \"caught up together... in the clouds, to meet the Lord in the air\"?", "1 Thessalonians", ["Galatians", "Titus", "Philemon"], "medium")
add("What common term describes believers being suddenly gathered to meet the Lord at His return?", "The rapture", ["The tribulation", "The millennium", "The exodus"], "medium")
add("According to Pentecostal end-times teaching, who alone knows the exact day and hour of Christ's return?", "God the Father", ["The apostles", "Church leaders", "The book of Daniel explicitly states it"], "medium")
add("What event does the book of Revelation describe as a thousand-year reign of Christ on earth?", "The millennium", ["The rapture", "The great tribulation", "The day of Pentecost"], "hard")
add("According to Revelation, what is the final judgment scene called, where the dead are judged out of the books?", "The great white throne judgment", ["The judgment seat of Moses", "The Passover judgment", "The Jubilee"], "hard")
add("What phrase describes Christians eagerly awaiting and preparing for Christ's return, a common Pentecostal emphasis?", "Watching and being ready, as the Bridegroom's return is imminent", ["Predicting the exact date of His return", "Ignoring prophecy altogether", "Assuming He will never return"], "medium")
add("According to 1 Thessalonians 4:16, what will occur first when the Lord descends from heaven with a shout?", "The dead in Christ shall rise first", ["Living believers rise first", "The earth is destroyed by fire", "All nations are instantly judged"], "hard")
add("Which book of the Bible contains the vision of a new heaven and a new earth, and a city called New Jerusalem?", "Revelation", ["Daniel", "Ezekiel", "Isaiah"], "medium")

# --- Church, Ministry, Giving ---
add("Ephesians 4 lists what are commonly called the \"fivefold ministry\" gifts for equipping the church; which of these is one of them?", "Evangelist", ["Deacon", "Elder", "Bishop"], "medium")
add("According to Ephesians 4:12, the fivefold ministry gifts are given for the perfecting of the saints and for the work of what?", "The ministry, for the edifying of the body of Christ", ["Political influence", "Financial accumulation", "Cultural entertainment"], "medium")
add("What term describes giving a tenth of one's income to support the work of God, taught from Malachi 3?", "Tithing", ["Alms only", "Indulgence", "Sacrifice of atonement"], "easy")
add("According to Malachi 3:10, believers are invited to \"bring ye all the tithes into the storehouse\" so that God may do what?", "Open the windows of heaven and pour out a blessing", ["Remove all future trials", "Grant instant wealth to everyone", "Cancel the need for faith"], "medium")
add("What ordinance, also called the Lord's Supper, involves bread and the cup in remembrance of Christ's sacrifice?", "Communion", ["Confirmation", "Extreme unction", "Penance"], "easy")
add("According to 1 Corinthians 11, believers are told to examine themselves before doing what?", "Partaking of the Lord's Supper (communion)", ["Being baptized in water", "Speaking in tongues", "Giving an offering"], "medium")
add("What term describes a public gathering where people are prayed for individually, common in Pentecostal revival services?", "An altar call or prayer line", ["A silent retreat", "A private confession booth", "A closed synod"], "medium")
add("According to Acts 2:42, what four things did the early believers continue steadfastly in?", "The apostles' doctrine, fellowship, breaking of bread, and prayers", ["Fasting, silence, isolation, and penance", "Politics, trade, farming, and war", "Only Sabbath observance"], "hard")
add("What New Testament practice involves believers gathering to pray, often described as being of one accord?", "Corporate prayer meetings", ["Private confession to a priest", "Pilgrimage to a shrine", "Ritual animal sacrifice"], "medium")

# --- Holiness / Christian Living / Prayer & Fasting ---
add("What term describes living a life set apart for God, avoiding worldly sin, emphasized in Pentecostal holiness teaching?", "Sanctification or holy living", ["Legalism only", "Asceticism for salvation", "Monastic vows"], "medium")
add("According to 1 Peter 1:16, believers are called to be holy because God is what?", "Holy", ["Distant", "Silent", "Unknowable"], "easy")
add("What spiritual discipline involves abstaining from food for a set time to seek God earnestly, practiced by Jesus and the early church?", "Fasting", ["Tithing", "Baptism", "Ordination"], "easy")
add("Jesus fasted for how many days in the wilderness before being tempted by the devil?", "40 days", ["7 days", "3 days", "12 days"], "easy")
add("What did the early church do in Acts 13 before sending out Paul and Barnabas on their first missionary journey?", "Fasted and prayed, then laid hands on them", ["Held a public vote only", "Sent them without any preparation", "Required a written creed be signed"], "hard")
add("According to Philippians 4:6, believers should be careful for nothing, but in everything by prayer and supplication make known what to God?", "Their requests, with thanksgiving", ["Only their sins", "Only their financial needs", "Nothing at all"], "medium")
add("What does James 5:16 say is availeth much when offered by a righteous person?", "The effectual fervent prayer", ["Silence", "Wealth", "Fame"], "medium")
add("What is the Great Commission, given by Jesus in Matthew 28, primarily calling believers to do?", "Go and make disciples of all nations, baptizing and teaching them", ["Remain isolated from the world", "Focus only on personal Bible study", "Wait passively for revival"], "easy")
add("According to Mark 16:15, to whom did Jesus command the disciples to preach the gospel?", "Every creature", ["Only the Jewish nation", "Only their own household", "Only the twelve apostles"], "easy")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
