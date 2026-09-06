import random
random.seed(64)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="Bible Basics"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("Who built a large boat to save his family and the animals from a great flood?", "Noah", ["Abraham", "Moses", "Job"], "easy")
add("Who led the Israelites out of slavery in Egypt?", "Moses", ["Joshua", "Aaron", "Abraham"], "easy")
add("Who was thrown into a den of lions but was not harmed?", "Daniel", ["Joseph", "David", "Samson"], "easy")
add("Who defeated the giant Goliath with a sling and a stone?", "David", ["Saul", "Samson", "Gideon"], "easy")
add("Who was known for his incredible strength, given by God?", "Samson", ["David", "Goliath", "Gideon"], "easy")
add("Who was sold into slavery by his brothers but later saved his family from famine?", "Joseph", ["Benjamin", "Reuben", "Judah"], "easy")
add("Which baby was placed in a basket on the Nile River to keep him safe?", "Moses", ["Samuel", "Joseph", "Isaac"], "easy")
add("Who was the mother of Jesus?", "Mary", ["Elizabeth", "Martha", "Anna"], "easy")
add("Where was Jesus born?", "Bethlehem", ["Nazareth", "Jerusalem", "Capernaum"], "easy")
add("What was Jesus' earthly father's name, who was a carpenter?", "Joseph", ["Zacharias", "Simeon", "Nicodemus"], "easy")
add("How many disciples did Jesus choose to be His closest followers?", "12", ["10", "7", "70"], "easy")
add("Who denied knowing Jesus three times but later became a bold preacher?", "Peter", ["Judas", "Thomas", "John"], "easy")
add("Who betrayed Jesus to the religious leaders?", "Judas Iscariot", ["Peter", "Thomas", "Pilate"], "easy")
add("On what did Jesus die for the sins of the world?", "The cross", ["A mountain", "A boat", "In prison"], "easy")
add("What happened to Jesus three days after He died?", "He rose from the dead", ["He disappeared forever", "He became an angel", "Nothing happened"], "easy")
add("What is the first book of the Bible?", "Genesis", ["Exodus", "Matthew", "Psalms"], "easy")
add("What is the last book of the Bible?", "Revelation", ["Malachi", "Jude", "Acts"], "easy")
add("What is the first book of the New Testament?", "Matthew", ["Mark", "Acts", "Romans"], "easy")
add("Who was the strongest man in the Bible, whose secret strength was in his uncut hair?", "Samson", ["David", "Goliath", "Saul"], "easy")
add("Who was swallowed by a big fish for three days after running away from God?", "Jonah", ["Noah", "Jeremiah", "Elijah"], "easy")
add("Which garden did Adam and Eve live in before they sinned?", "The Garden of Eden", ["The Garden of Gethsemane", "The Garden of Bethany", "The Garden of Jericho"], "easy")
add("What did God use to create light on the very first day, according to Genesis?", "His spoken word (\"Let there be light\")", ["The sun", "Fire", "Stars"], "easy")
add("Who was the first man God created?", "Adam", ["Cain", "Noah", "Abraham"], "easy")
add("Who was the first woman God created?", "Eve", ["Sarah", "Rebekah", "Rachel"], "easy")
add("What did God ask Abraham to offer as a sacrifice, before providing a ram instead?", "His son Isaac", ["A lamb", "A dove", "His servant"], "easy")
add("Which sea did God part so Moses and the Israelites could escape from Pharaoh's army?", "The Red Sea", ["The Dead Sea", "The Sea of Galilee", "The Mediterranean Sea"], "easy")
add("What did God give Moses on Mount Sinai, written on stone tablets?", "The Ten Commandments", ["The Psalms", "The Proverbs", "The Beatitudes"], "easy")
add("Who was the wife of Abraham who gave birth to Isaac in her old age?", "Sarah", ["Rebekah", "Hagar", "Rachel"], "easy")
add("Who was known as a very wise king who built the first Temple in Jerusalem?", "Solomon", ["David", "Saul", "Hezekiah"], "easy")
add("Who was David's best friend, the son of King Saul?", "Jonathan", ["Samuel", "Nathan", "Absalom"], "medium")
add("What job did David have as a young boy before he became king?", "A shepherd", ["A fisherman", "A carpenter", "A soldier"], "easy")
add("Which apostle was a fisherman before Jesus called him to \"follow me\"?", "Peter", ["Matthew", "Nicodemus", "Paul"], "easy")
add("What did Jesus turn into wine at a wedding in Cana?", "Water", ["Milk", "Grape juice", "Tea"], "easy")
add("How many loaves of bread and fish did the boy offer Jesus before the feeding of the five thousand?", "5 loaves and 2 fish", ["2 loaves and 5 fish", "7 loaves and 2 fish", "3 loaves and 3 fish"], "easy")
add("Who was thrown into a pit by his jealous brothers and later became a ruler in Egypt?", "Joseph", ["Benjamin", "Reuben", "Judah"], "easy")
add("Which prophet was taken up to heaven in a whirlwind, watched by his follower Elisha?", "Elijah", ["Isaiah", "Jeremiah", "Ezekiel"], "medium")
add("Who was the Old Testament woman who saved her people from destruction by approaching the king?", "Esther", ["Ruth", "Deborah", "Rahab"], "medium")
add("What was the name of the boat Noah built to survive the flood?", "The ark", ["The ship of Tarshish", "The vessel of Jonah", "The barge"], "easy")
add("Which two disciples were told by Jesus to go and prepare the Passover meal (the Last Supper)?", "Peter and John", ["James and John", "Peter and Andrew", "Matthew and Thomas"], "hard")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
