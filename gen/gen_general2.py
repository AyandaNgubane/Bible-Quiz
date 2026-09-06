import random
random.seed(56)

Q = []

def make_options(correct, wrongs, n=4):
    opts = [correct] + wrongs[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

def add(question, correct, wrongs, diff, cat="New Testament Narratives"):
    opts, idx = make_options(correct, wrongs)
    Q.append({"question": question, "options": opts, "correct_index": idx,
              "difficulty": diff, "category": cat})

add("Which angel announced to Mary that she would give birth to Jesus?", "Gabriel", ["Michael", "Raphael", "An unnamed angel"], "easy")
add("In whose house did Mary stay for three months after learning she would give birth to the Messiah?", "Elizabeth's house", ["Martha's house", "Joseph's parents' house", "The Temple"], "medium")
add("Why did Joseph and Mary travel to Bethlehem shortly before Jesus was born?", "To be registered in a Roman census", ["To visit family for Passover", "To attend the Feast of Tabernacles", "To escape persecution"], "medium")
add("Who were the first to visit the newborn Jesus after being told by angels?", "Shepherds", ["Wise men from the East", "Roman soldiers", "Pharisees"], "easy")
add("What gifts did the wise men bring to the young Jesus?", "Gold, frankincense, and myrrh", ["Silver, wine, and oil", "Bread, wine, and spices", "Wool, linen, and gold"], "easy")
add("To which country did Joseph and Mary flee with Jesus to escape King Herod?", "Egypt", ["Babylon", "Assyria", "Persia"], "medium")
add("At what age was Jesus found in the Temple discussing scripture with the teachers?", "12", ["8", "18", "30"], "medium")
add("Who baptized Jesus in the Jordan River?", "John the Baptist", ["Peter", "Andrew", "Nicodemus"], "easy")
add("What did John the Baptist eat while preaching in the wilderness?", "Locusts and wild honey", ["Bread and fish", "Manna", "Figs and olives"], "medium")
add("How did Jesus respond to each of the devil's three temptations in the wilderness?", "By quoting scripture", ["By performing a miracle", "By remaining silent", "By calling down fire"], "medium")
add("At about what age did Jesus begin His public ministry, according to Luke 3?", "About 30 years old", ["About 12 years old", "About 18 years old", "About 40 years old"], "medium")
add("On the Mount of Transfiguration, which two Old Testament figures appeared talking with Jesus?", "Moses and Elijah", ["Abraham and Isaac", "David and Solomon", "Isaiah and Jeremiah"], "medium")
add("Which three disciples witnessed the Transfiguration of Jesus?", "Peter, James, and John", ["Peter, Andrew, and Philip", "James, John, and Thomas", "Peter, Thomas, and Matthew"], "hard")
add("What did Jesus ride into Jerusalem on during what is now called the Triumphal Entry?", "A young donkey (colt)", ["A white horse", "A chariot", "A camel"], "easy")
add("What did the crowds lay on the ground and wave as Jesus entered Jerusalem?", "Palm branches and garments", ["Wheat sheaves", "Flowers", "Vine branches"], "easy")
add("What meal was Jesus sharing with His disciples when He instituted communion?", "The Passover (Last Supper)", ["The Feast of Tabernacles", "A wedding feast", "A regular Sabbath meal"], "medium")
add("In which garden did Jesus pray so intensely that His sweat became like great drops of blood?", "The Garden of Gethsemane", ["The Garden of Eden", "The garden of Joseph of Arimathea's tomb", "The garden at Bethany"], "medium")
add("Who betrayed Jesus with a kiss in the garden of Gethsemane?", "Judas Iscariot", ["Peter", "Thomas", "Barabbas"], "easy")
add("Which criminal did the crowd ask Pilate to release instead of Jesus?", "Barabbas", ["Dismas", "Malchus", "Herod"], "medium")
add("What did Pilate do to symbolically show he found no guilt in Jesus?", "Washed his hands before the crowd", ["Tore his robe", "Offered a sacrifice", "Released all prisoners"], "medium")
add("What sign did Pilate have written and placed above Jesus on the cross?", "JESUS OF NAZARETH THE KING OF THE JEWS", ["THE SON OF GOD", "KING OF ISRAEL", "THE MESSIAH HAS COME"], "medium")
add("What happened to the veil of the Temple at the moment Jesus died?", "It was torn in two from top to bottom", ["It was burned by fire", "It was removed by the priests", "Nothing happened to it"], "medium")
add("Who asked Pilate for the body of Jesus and laid it in his own new tomb?", "Joseph of Arimathea", ["Nicodemus alone", "Simon of Cyrene", "Lazarus"], "medium")
add("Who was the first person to see the risen Jesus on resurrection morning?", "Mary Magdalene", ["Peter", "John", "Thomas"], "medium")
add("On the road to which village did the risen Jesus walk and talk with two disciples who did not recognize Him?", "Emmaus", ["Bethany", "Jericho", "Capernaum"], "hard")
add("Which disciple famously said he would not believe in the resurrection unless he could touch Jesus' wounds?", "Thomas", ["Peter", "Philip", "Andrew"], "easy")
add("From which location did Jesus ascend into heaven forty days after His resurrection?", "The Mount of Olives", ["Mount Sinai", "Golgotha", "The Temple courts"], "medium")
add("On the Day of Pentecost, roughly how many people were added to the church after Peter's sermon?", "About 3,000", ["About 500", "About 12", "About 70"], "medium")
add("Who was the first Christian martyr, stoned to death while seeing a vision of Jesus standing at God's right hand?", "Stephen", ["James", "Timothy", "Barnabas"], "medium")
add("Who held the coats of those who stoned Stephen, later becoming a great apostle?", "Saul (later Paul)", ["Barnabas", "Ananias", "Cornelius"], "medium")
add("Who was the Roman centurion whose household became among the first Gentile converts, guided by Peter's vision?", "Cornelius", ["Felix", "Festus", "Cornelius' servant"], "medium")
add("On which of Paul's missionary journeys did he first visit Europe, including the city of Philippi?", "His second missionary journey", ["His first missionary journey", "His third missionary journey", "His journey to Rome"], "hard")
add("Which jailer and his household were converted after an earthquake freed Paul and Silas from prison in Philippi?", "The Philippian jailer", ["The centurion Cornelius", "The proconsul Sergius Paulus", "The magistrate of Ephesus"], "hard")
add("What did Paul and Silas do in prison at midnight that led to an earthquake and the jailer's conversion?", "Prayed and sang praises to God", ["Fasted silently", "Dug a tunnel to escape", "Wrote letters to the churches"], "medium")
add("On which island did Paul survive a deadly snake bite without harm after being shipwrecked?", "Malta", ["Cyprus", "Crete", "Patmos"], "hard")
add("Which Roman governor did Paul stand trial before, later appealing to Caesar?", "Festus (and also Felix)", ["Pontius Pilate", "Herod Antipas", "Sergius Paulus"], "hard")

def build():
    return Q

if __name__ == "__main__":
    print(len(build()))
