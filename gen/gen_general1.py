import random
random.seed(55)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="Old Testament Narratives"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("On which day of creation did God make the sun, moon, and stars?", "The fourth day", ["The first day", "The third day", "The sixth day"], "medium")
add("On which day of creation did God rest from all His work?", "The seventh day", ["The sixth day", "The first day", "The eighth day"], "easy")
add("What did God create on the sixth day of creation, according to Genesis 1?", "Land animals and mankind", ["The sun and moon", "The seas and fish", "Light and darkness"], "medium")
add("Who tempted Eve to eat the forbidden fruit in the Garden of Eden?", "The serpent", ["Cain", "An angel", "Adam"], "easy")
add("What was the name of Adam and Eve's first son, who later killed his brother?", "Cain", ["Abel", "Seth", "Enoch"], "easy")
add("Which son of Adam and Eve did Cain murder out of jealousy?", "Abel", ["Seth", "Enosh", "Noah"], "easy")
add("How many people were saved on Noah's ark?", "8", ["4", "12", "40"], "medium")
add("What sign did God give Noah as a promise never again to flood the whole earth?", "The rainbow", ["A dove", "An olive branch", "A pillar of cloud"], "easy")
add("What was the name of the tower that men built in an attempt to reach heaven, before God confused their languages?", "The Tower of Babel", ["The Tower of Babylon", "The Tower of Shinar", "The Tower of Nineveh"], "easy")
add("From which city did God call Abram (later Abraham) to go to a land He would show him?", "Ur of the Chaldees", ["Haran", "Bethel", "Nineveh"], "medium")
add("What did God change Abram's name to, meaning \"father of many nations\"?", "Abraham", ["Israel", "Isaac", "Ishmael"], "easy")
add("What did God change Sarai's name to?", "Sarah", ["Rebekah", "Rachel", "Leah"], "medium")
add("Who was Abraham's son of promise, born to him and Sarah in their old age?", "Isaac", ["Ishmael", "Jacob", "Esau"], "easy")
add("On which mountain did God test Abraham by asking him to sacrifice his son?", "Mount Moriah", ["Mount Sinai", "Mount Carmel", "Mount Ararat"], "hard")
add("Which two cities did God destroy with fire and brimstone because of their great wickedness?", "Sodom and Gomorrah", ["Nineveh and Babylon", "Jericho and Ai", "Tyre and Sidon"], "easy")
add("Who looked back at the destruction of Sodom and turned into a pillar of salt?", "Lot's wife", ["Lot's daughter", "Sarah", "Rebekah"], "easy")
add("What did Esau sell to his brother Jacob for a meal of bread and lentil stew?", "His birthright", ["His inheritance land", "His flocks", "His tent"], "medium")
add("What did Jacob dream about at Bethel involving angels?", "A ladder reaching to heaven with angels ascending and descending", ["A burning bush", "A great flood", "A fiery chariot"], "medium")
add("With whom did Jacob wrestle all night, receiving the new name Israel?", "An angel of the Lord (a man / God)", ["Esau", "Laban", "Pharaoh"], "medium")
add("How many sons did Jacob have who became the twelve tribes of Israel?", "12", ["10", "7", "13"], "easy")
add("Which of Jacob's sons was sold into slavery by his jealous brothers?", "Joseph", ["Reuben", "Judah", "Benjamin"], "easy")
add("What garment did Jacob give Joseph that made his brothers jealous?", "A coat of many colours", ["A golden crown", "A silver belt", "A linen robe"], "easy")
add("In Egypt, what position did Joseph rise to under Pharaoh after interpreting his dreams?", "Second-in-command over all Egypt", ["Chief priest", "Court musician", "Royal scribe only"], "medium")
add("Who found the baby Moses hidden in a basket among the reeds of the Nile River?", "Pharaoh's daughter", ["Miriam", "Jochebed", "An Egyptian slave"], "medium")
add("What did God appear to Moses in while calling him to deliver Israel?", "A burning bush", ["A pillar of cloud", "A whirlwind", "A rainbow"], "easy")
add("What did Moses' staff turn into as a sign before Pharaoh?", "A serpent", ["A dove", "A lamb", "A lion"], "medium")
add("What did God part so the Israelites could cross on dry ground while fleeing Egypt?", "The Red Sea", ["The Jordan River", "The Dead Sea", "The Sea of Galilee"], "easy")
add("What food did God provide daily for the Israelites in the wilderness?", "Manna", ["Quail only", "Barley bread", "Honey cakes"], "easy")
add("What did the Israelites build and worship while Moses was on Mount Sinai receiving the Law?", "A golden calf", ["A silver ox", "A bronze serpent", "A wooden altar"], "easy")
add("What structure did God instruct Moses to build as a portable place of worship in the wilderness?", "The tabernacle", ["The Temple", "The synagogue", "The altar of Solomon"], "medium")
add("What object was kept inside the Ark of the Covenant, along with Aaron's rod and a pot of manna, according to Hebrews 9?", "The tables of the covenant (the stone tablets of the Law)", ["A crown of gold", "The staff of Joseph", "A scroll of Isaiah"], "hard")
add("Who was Moses' brother, appointed as Israel's first high priest?", "Aaron", ["Joshua", "Caleb", "Nadab"], "medium")
add("Who succeeded Moses as leader of Israel and led the conquest of Canaan?", "Joshua", ["Caleb", "Aaron", "Othniel"], "easy")
add("Which two spies gave a good report of the Promised Land, urging Israel to trust God and enter it?", "Joshua and Caleb", ["Aaron and Miriam", "Nadab and Abihu", "Korah and Dathan"], "medium")
add("What happened to the walls of Jericho after Israel marched around the city seven times?", "They fell down flat", ["They caught fire", "They were never breached", "They turned to sand"], "easy")
add("Which woman in Jericho hid the Israelite spies and was spared when the city fell?", "Rahab", ["Deborah", "Ruth", "Naomi"], "medium")
add("What did God command the sun and moon to do during Joshua's battle so Israel could finish defeating their enemies?", "Stand still", ["Grow brighter", "Turn to blood", "Disappear entirely"], "hard")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
