import random
random.seed(62)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="Tabernacle, Priesthood & Law"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("Which tribe of Israel was set apart to serve as priests and did not receive a normal land inheritance?", "Levi", ["Judah", "Benjamin", "Ephraim"], "medium")
add("Which piece of tabernacle furniture held the tablets of the Law, Aaron's rod, and a pot of manna?", "The Ark of the Covenant", ["The bronze laver", "The altar of incense", "The table of shewbread"], "medium")
add("What covered the top of the Ark of the Covenant, where God's presence was said to dwell between two cherubim?", "The mercy seat", ["The veil", "The lampstand", "The altar of burnt offering"], "hard")
add("What was placed in the Holy Place of the tabernacle along with the table of shewbread and altar of incense?", "The golden lampstand (menorah)", ["The Ark of the Covenant", "The brazen altar", "The laver"], "hard")
add("What separated the Holy Place from the Most Holy Place in the tabernacle and Temple?", "The veil", ["The outer court fence", "The bronze laver", "The altar of burnt offering"], "medium")
add("Which high priest's garment bore twelve stones representing the twelve tribes of Israel?", "The breastplate", ["The ephod alone", "The turban", "The robe"], "hard")
add("What was the primary purpose of the daily and annual sacrifices under the Law of Moses?", "Atonement for sin", ["Celebration of harvest only", "Political tribute", "Entertainment"], "medium")
add("Which mountain is associated with the giving of the Law and is also called Horeb?", "Mount Sinai", ["Mount Zion", "Mount Carmel", "Mount Nebo"], "medium")
add("From which mountain did Moses view the Promised Land before he died, being forbidden to enter it?", "Mount Nebo", ["Mount Sinai", "Mount Hermon", "Mount Gilboa"], "hard")
add("According to the Law, what was to happen every seventh year regarding the land in Israel?", "It was to rest (a sabbatical year)", ["It was to be sold", "It was to be flooded", "It was to be divided again"], "hard")
add("What special year, occurring every fifty years, involved the release of debts, freeing of slaves, and return of land?", "The Year of Jubilee", ["The sabbatical year", "The Day of Atonement", "The Feast of Trumpets"], "hard")
add("What did God command Israel to build to keep His presence among them as they journeyed in the wilderness?", "The tabernacle", ["A permanent Temple", "A network of synagogues", "A royal palace"], "easy")
add("Who was commissioned with special skill by God to craft the artistic elements of the tabernacle?", "Bezaleel", ["Aaron", "Joshua", "Caleb"], "hard")
add("What sacrificial animal was central to the Passover meal, later fulfilled by Christ as \"the Lamb of God\"?", "A lamb (without blemish)", ["A goat", "A bull", "A dove"], "easy")
add("What did the Israelites mark on their doorposts so the angel of death would pass over their homes in Egypt?", "The blood of the Passover lamb", ["Ashes", "Oil", "Salt"], "easy")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
