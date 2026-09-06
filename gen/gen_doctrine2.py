import random
random.seed(53)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="Pentecostal Doctrine"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

# --- Gifts of the Spirit (1 Corinthians 12) ---
add("Which chapter of 1 Corinthians lists nine gifts of the Spirit, including prophecy and healing?", "1 Corinthians 12", ["1 Corinthians 13", "1 Corinthians 14", "Romans 12"], "medium")
add("According to 1 Corinthians 12, who divides the spiritual gifts to every believer as He wills?", "The Holy Spirit", ["The local pastor", "The apostles alone", "A church council"], "medium")
add("Which spiritual gift involves receiving supernatural insight into a fact not learned through natural means?", "The word of knowledge", ["The gift of tongues", "The gift of helps", "The gift of giving"], "medium")
add("Which spiritual gift involves speaking forth a message under the inspiration of the Holy Spirit for edification, exhortation, or comfort?", "Prophecy", ["Interpretation of tongues", "Discerning of spirits", "Word of wisdom"], "medium")
add("Which spiritual gift enables a believer to recognize whether a spirit at work is of God or not?", "Discerning of spirits", ["Word of knowledge", "Faith", "Working of miracles"], "hard")
add("Which spiritual gift is paired with tongues so that a message given in an unknown tongue can be understood by the church?", "Interpretation of tongues", ["Discerning of spirits", "Word of wisdom", "Prophecy"], "medium")
add("According to 1 Corinthians 12, are all believers expected to operate in every single gift of the Spirit?", "No, the Spirit distributes different gifts to different members as one body", ["Yes, every believer must have all nine gifts", "No gifts are given after the apostles died", "Only pastors may receive any gifts"], "hard")
add("Which chapter of 1 Corinthians, right after the gifts are listed, is often called \"the love chapter\"?", "1 Corinthians 13", ["1 Corinthians 12", "1 Corinthians 14", "Romans 8"], "medium")
add("What does 1 Corinthians 13 teach is greater than even prophecy, tongues, and knowledge?", "Charity (love)", ["Wealth", "Wisdom", "Fame"], "medium")
add("Which spiritual gift involves an unusual measure of confident trust in God for the miraculous?", "The gift of faith", ["The gift of tongues", "The gift of helps", "The gift of teaching"], "hard")
add("According to Romans 12, besides the gifts in 1 Corinthians 12, which gifts are also listed, such as giving and showing mercy?", "Motivational gifts of grace", ["Only the fivefold ministry gifts", "Only healing gifts", "Only leadership titles"], "hard")
add("What should be the governing motive behind the exercise of every spiritual gift, according to Pentecostal teaching?", "Love, for the edifying of the body of Christ", ["Personal recognition", "Financial gain", "Denominational pride"], "medium")

# --- Fruit of the Spirit (Galatians 5) ---
add("Which epistle lists the fruit of the Spirit, contrasting it with the works of the flesh?", "Galatians", ["Ephesians", "Colossians", "1 Peter"], "medium")
add("Which is the first fruit of the Spirit listed in Galatians 5:22?", "Love", ["Joy", "Peace", "Faith"], "easy")
add("According to Galatians 5, against such things as the fruit of the Spirit, there is no what?", "Law", ["Judgment", "Mercy", "Grace"], "hard")
add("Fruit of the Spirit and gifts of the Spirit differ in Pentecostal teaching mainly in what way?", "Fruit is character developed over time; gifts are supernatural abilities given for ministry", ["They are exactly the same thing", "Fruit is for unbelievers and gifts are for believers", "Gifts take years to develop while fruit is instant"], "medium")
add("Which fruit of the Spirit is often described as inward contentment that does not depend on circumstances?", "Peace", ["Longsuffering", "Temperance", "Meekness"], "medium")
add("Which fruit of the Spirit refers to self-control, especially over one's own desires and impulses?", "Temperance", ["Meekness", "Gentleness", "Goodness"], "medium")

# --- Divine Healing ---
add("Which Old Testament prophecy is commonly cited by Pentecostals to teach that healing is provided in Christ's atonement?", "Isaiah 53, \"with his stripes we are healed\"", ["Psalm 23", "Micah 5", "Jeremiah 31"], "medium")
add("According to James 5:14-15, what should the elders do for someone who is sick?", "Anoint them with oil and pray the prayer of faith over them", ["Quarantine them from the church", "Ignore the matter as purely medical", "Require they leave the congregation"], "medium")
add("Which New Testament verse says Jesus Christ is \"the same yesterday, and to day, and for ever,\" often used to support present-day healing?", "Hebrews 13:8", ["John 3:16", "Romans 8:28", "Psalm 91:1"], "hard")
add("What practical action does James 5 recommend when someone in the church is sick?", "Call for the elders of the church to pray over them", ["Wait silently without prayer", "Consult a fortune teller", "Leave the matter entirely to fate"], "medium")
add("According to Matthew 8:17, Jesus fulfilled the prophecy that He Himself took our infirmities and bore what?", "Our sicknesses", ["Our sins alone", "Our poverty", "Our enemies' punishment"], "medium")
add("Divine healing services in Pentecostal churches commonly include which practice, based on Mark 16:18?", "Laying hands on the sick", ["Reciting a fixed liturgy only", "Handling venomous snakes as a required rite", "Silent meditation only"], "medium")
add("In the Great Commission passage of Mark 16, what sign is promised to follow believers regarding the sick?", "They shall lay hands on the sick, and they shall recover", ["They shall avoid the sick entirely", "They shall only send them to physicians", "They shall fast for forty days first"], "medium")

# --- Water Baptism ---
add("What mode of water baptism is generally practiced in Pentecostal churches?", "Full immersion", ["Sprinkling only", "Pouring only for infants", "No water is used at all"], "easy")
add("At Jesus' own baptism in the Jordan River, who baptized Him?", "John the Baptist", ["Peter", "Paul", "Andrew"], "easy")
add("What happened immediately after Jesus was baptized, as recorded in Matthew 3?", "The Spirit of God descended like a dove and a voice from heaven spoke", ["The sky went completely dark", "The Jordan River dried up", "An earthquake struck the region"], "medium")
add("According to Pentecostal teaching, is water baptism generally seen as necessary to be saved, or as an act of obedience after salvation?", "An act of obedience and public testimony after believing", ["A magical act that saves apart from faith", "Something only infants should receive", "A ritual with no scriptural basis"], "medium")
add("What did the Ethiopian eunuch request after Philip explained the gospel to him in Acts 8?", "To be baptized in water", ["To be circumcised", "To return to Jerusalem first", "To receive the Law of Moses"], "medium")
add("In the Great Commission of Matthew 28:19, believers are told to baptize new disciples in what name(s)?", "The name of the Father, and of the Son, and of the Holy Ghost", ["Only the name of Moses", "Only the name of the local church", "No specific name is given"], "easy")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
