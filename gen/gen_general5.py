import random
random.seed(59)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="People Jesus Encountered"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("Which Pharisee visited Jesus by night and was told he must be born again?", "Nicodemus", ["Joseph of Arimathea", "Gamaliel", "Simon the Pharisee"], "medium")
add("Which short tax collector climbed a sycamore tree to see Jesus passing by?", "Zacchaeus", ["Matthew", "Levi", "Nicodemus"], "easy")
add("What did Zacchaeus promise to do after Jesus came to his house?", "Give half his goods to the poor and restore fourfold anything he had taken by fraud", ["Become a priest", "Move to Jerusalem", "Sell his house"], "medium")
add("Which blind beggar called out to Jesus near Jericho, \"Thou son of David, have mercy on me\"?", "Bartimaeus", ["Zacchaeus", "Lazarus", "Simon"], "medium")
add("Which Roman centurion asked Jesus to heal his servant, saying he was not worthy for Jesus to come under his roof?", "A centurion in Capernaum", ["Cornelius", "The centurion at the cross", "Sergius Paulus"], "medium")
add("Which centurion at the cross declared, \"Truly this was the Son of God\" after Jesus died?", "The centurion overseeing the crucifixion", ["Cornelius", "The Capernaum centurion", "Julius"], "hard")
add("Which sisters of Lazarus hosted Jesus in their home in Bethany?", "Martha and Mary", ["Salome and Joanna", "Elizabeth and Anna", "Rachel and Leah"], "medium")
add("Which man, cured of blindness by Jesus, was questioned and cast out by the Pharisees for testifying about Him?", "The man born blind (John 9)", ["Bartimaeus", "Lazarus", "The paralytic at Bethesda"], "hard")
add("Which rich young man asked Jesus what he must do to inherit eternal life, but went away sorrowful?", "The rich young ruler", ["Nicodemus", "Zacchaeus", "Joseph of Arimathea"], "medium")
add("Which Pharisee and member of the Sanhedrin helped bury Jesus, bringing myrrh and aloes?", "Nicodemus", ["Joseph of Arimathea (jointly)", "Gamaliel", "Simon the Pharisee"], "hard")
add("Who carried Jesus' cross part of the way to Golgotha after Jesus grew weak?", "Simon of Cyrene", ["Joseph of Arimathea", "Barabbas", "A Roman centurion"], "medium")
add("Which woman was caught in adultery and brought before Jesus, who said, \"Neither do I condemn thee\"?", "An unnamed woman taken in adultery", ["Mary Magdalene", "The Samaritan woman", "The woman with the issue of blood"], "medium")
add("Which teacher of the Law, respected by all the people, warned the Sanhedrin not to fight against the apostles in Acts 5?", "Gamaliel", ["Nicodemus", "Caiaphas", "Annas"], "hard")
add("Who was the high priest who presided over Jesus' trial before the Sanhedrin?", "Caiaphas", ["Annas", "Gamaliel", "Ananias"], "medium")
add("Which king mocked and questioned Jesus before sending Him back to Pilate, having long wanted to see a miracle?", "Herod Antipas", ["Herod the Great", "Herod Agrippa", "Archelaus"], "hard")
add("Which magician in Samaria tried to buy the power to give the Holy Spirit with money?", "Simon (Simon Magus)", ["Elymas", "Bar-jesus", "Demetrius"], "hard")
add("Which sorcerer opposed Paul and Barnabas before the proconsul on the island of Cyprus?", "Elymas (Bar-jesus)", ["Simon Magus", "Demetrius", "Alexander"], "hard")
add("Which silversmith in Ephesus stirred up a riot against Paul because his idol-making business was threatened?", "Demetrius", ["Elymas", "Simon Magus", "Alexander the coppersmith"], "hard")
add("Which young man fell asleep during Paul's long sermon and fell from a window, but was raised back to life?", "Eutychus", ["Timothy", "Titus", "Trophimus"], "hard")
add("Which young disciple, mentored by Paul, received two epistles giving pastoral instruction?", "Timothy", ["Titus", "Silas", "Epaphroditus"], "medium")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
