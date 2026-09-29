import random
random.seed(52)

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

Q = []

def add(question, correct, wrongs, diff, cat="Pentecostal Doctrine"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

# --- Salvation & New Birth ---
add("According to Pentecostal teaching, how is a person saved?", "By grace through faith in Jesus Christ", ["By keeping the Ten Commandments perfectly", "By being born into a Christian family", "By performing enough good works"], "easy")
add("Jesus told Nicodemus that unless a man is born again, he cannot do what?", "See the kingdom of God", ["Receive the gifts of the Spirit", "Be baptized in water", "Become a church member"], "medium")
add("What does it mean, in Pentecostal teaching, to be \"born again\"?", "To experience spiritual new birth through faith in Christ", ["To be baptized as an infant", "To join a local congregation", "To be confirmed by a bishop"], "easy")
add("According to Romans 10:9, what must a person confess and believe to be saved?", "Confess Jesus as Lord and believe God raised Him from the dead", ["Confess their sins to a priest weekly", "Believe in predestined election only", "Recite the Ten Commandments daily"], "medium")
add("What is the free gift of God, according to Romans 6:23?", "Eternal life through Jesus Christ our Lord", ["Wealth and prosperity", "Long life on earth", "Membership in a denomination"], "easy")
add("According to Ephesians 2:8-9, salvation is by grace through faith, and not of what, so that no man can boast?", "Works", ["Baptism", "Prayer", "Fasting"], "medium")
add("What is the term commonly used for the moment a person publicly responds to receive salvation during a service?", "An altar call", ["A liturgy", "A mass", "A confirmation"], "easy")
add("Who did Jesus say is the way, the truth, and the life, and that no man comes to the Father but by Him?", "Jesus Himself", ["Moses", "The Holy Spirit", "An angel of the Lord"], "easy")
add("What must happen to a believer's heart at conversion, according to Pentecostal teaching on repentance?", "A genuine turning away from sin toward God", ["Nothing changes outwardly or inwardly", "Only outward religious behavior changes", "A change recognized only after death"], "medium")
add("According to Acts 4:12, in whose name alone is there salvation?", "Jesus Christ", ["Moses", "The archangel Michael", "The church"], "medium")

# --- Holy Spirit Baptism & Tongues (core Pentecostal distinctive) ---
add("What is the distinctive Pentecostal teaching regarding baptism in the Holy Spirit?", "It is a definite experience subsequent to salvation, evidenced by speaking in tongues", ["It happens automatically and silently at salvation with no evidence", "It is reserved only for church leaders and pastors", "It replaces the need for water baptism"], "medium")
add("In Acts chapter 2, what sound and sign accompanied the outpouring of the Holy Spirit at Pentecost?", "A sound like a rushing mighty wind and cloven tongues like fire", ["A great earthquake and total darkness", "A voice from a burning bush", "A dove descending silently"], "medium")
add("On the Day of Pentecost, what began to happen to the believers as the Spirit gave them utterance?", "They spoke with other tongues", ["They fell into a deep sleep", "They fasted for forty days", "They wrote new scripture"], "easy")
add("Which Old Testament prophet foretold that God would pour out His Spirit upon all flesh, a promise quoted by Peter at Pentecost?", "Joel", ["Malachi", "Isaiah", "Amos"], "medium")
add("In Acts chapter 10, what evidence convinced Peter that Gentiles in Cornelius' house had received the Holy Spirit?", "They spoke with tongues and magnified God", ["They were baptized in water first", "They gave large financial offerings", "They fasted for three days"], "hard")
add("In Acts chapter 19, what happened when Paul laid hands on the disciples at Ephesus?", "The Holy Spirit came on them and they spoke with tongues and prophesied", ["They immediately became elders", "They were struck silent", "They saw a vision of angels"], "hard")
add("What term do Pentecostals commonly use for speaking in tongues as an initial sign of Spirit baptism?", "The initial physical evidence", ["The final act of sanctification", "The sacrament of confirmation", "The seal of ordination"], "hard")
add("According to Acts 1:8, what would the disciples receive after the Holy Spirit came upon them?", "Power to be witnesses", ["Wealth and long life", "Freedom from all future suffering", "Political authority over Rome"], "easy")
add("What did Jesus tell His disciples to wait for in Jerusalem before beginning their ministry, recorded in Acts 1?", "The promise of the Father, the baptism in the Holy Spirit", ["A letter from the Roman governor", "The rebuilding of the Temple", "A new set of written commandments"], "medium")
add("In 1 Corinthians 14, Paul teaches that tongues, when used publicly without interpretation, should be limited in the church for the sake of what?", "Edification and order in the church", ["Personal entertainment", "Political influence", "Financial giving"], "hard")
add("According to 1 Corinthians 14:2, one who speaks in an unknown tongue speaks not unto men but unto whom?", "God", ["The angels", "The congregation", "The elders"], "medium")
add("What does Pentecostal doctrine teach is the primary purpose of speaking in tongues in personal, private prayer?", "Personal edification and communion with God", ["Public entertainment", "Proof of denominational membership", "A requirement for salvation"], "medium")
add("Which New Testament book records the initial outpouring of the Holy Spirit that gave the Pentecostal movement its name?", "Acts", ["Romans", "Revelation", "Hebrews"], "easy")
add("The Jewish Feast of Pentecost, during which the Spirit was poured out in Acts 2, is also known by what Old Testament name?", "The Feast of Weeks", ["The Feast of Trumpets", "The Day of Atonement", "The Feast of Tabernacles"], "hard")
add("According to Luke 11:13, what will the heavenly Father give to those who ask Him?", "The Holy Spirit", ["Material riches", "A long earthly life", "Freedom from persecution"], "medium")
add("What did John the Baptist say Jesus would baptize believers with, in addition to water?", "The Holy Ghost and fire", ["Oil and wine", "Ashes and sackcloth", "Blood and water"], "medium")
add("How many days after the resurrection did the Holy Spirit fall on the believers at Pentecost?", "50 days (counting from Passover)", ["3 days", "40 days", "100 days"], "hard")
add("According to Acts 2:39, to whom is the promise of the Holy Spirit given?", "To believers, their children, and all who are far off, as many as the Lord shall call", ["Only to the original twelve apostles", "Only to Jewish priests", "Only to church leaders"], "medium")
add("What miraculous sign appeared over each believer's head as the Spirit was poured out at Pentecost?", "Cloven tongues like as of fire", ["A crown of thorns", "A dove of gold", "A rainbow"], "medium")
add("What common term describes believers who actively seek and practice the gifts of the Holy Spirit today, including tongues?", "Charismatic or Pentecostal believers", ["Cessationists", "Ascetics", "Monastics"], "medium")

for q in Q:
    pass

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
