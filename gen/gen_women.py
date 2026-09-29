import random
random.seed(50)

def make_options(correct, pool, n=4):
    distractors = [x for x in pool if x != correct]
    random.shuffle(distractors)
    opts = [correct] + distractors[:n-1]
    random.shuffle(opts)
    return opts, opts.index(correct)

NAMES = ["Eve", "Sarah", "Hagar", "Rebekah", "Rachel", "Leah", "Miriam", "Deborah",
         "Ruth", "Naomi", "Hannah", "Abigail", "Bathsheba", "Esther", "Jezebel",
         "Delilah", "Mary the mother of Jesus", "Elizabeth", "Mary Magdalene",
         "Martha", "Mary of Bethany", "The Samaritan woman at the well",
         "Lydia", "Priscilla", "Dorcas", "Anna the prophetess", "Rahab", "Vashti"]

FACTS = [
    ("Eve", "Who was the first woman, formed from Adam's rib in the garden of Eden?", "easy"),
    ("Sarah", "Which woman, Abraham's wife, laughed when told she would bear a son in her old age?", "medium"),
    ("Hagar", "Which woman, Sarah's handmaid, bore Abraham a son named Ishmael?", "medium"),
    ("Rebekah", "Which woman was chosen at a well to become Isaac's wife?", "medium"),
    ("Rachel", "Which of Jacob's wives did he love and work fourteen years for, dying while giving birth to Benjamin?", "medium"),
    ("Leah", "Which of Jacob's wives was given to him in place of her sister on his wedding night?", "hard"),
    ("Miriam", "Which woman, sister of Moses and Aaron, led the women of Israel in song after crossing the Red Sea?", "medium"),
    ("Deborah", "Which woman judged Israel and was also a prophetess?", "medium"),
    ("Ruth", "Which Moabite woman said, \"whither thou goest, I will go,\" to her mother-in-law?", "medium"),
    ("Naomi", "Which woman lost her husband and two sons in Moab before returning to Bethlehem with Ruth?", "hard"),
    ("Hannah", "Which woman wept and prayed for a son, later dedicating him, Samuel, to the Lord's service?", "medium"),
    ("Abigail", "Which wise woman prevented David from taking violent revenge on her foolish husband Nabal?", "hard"),
    ("Bathsheba", "Which woman, wife of Uriah the Hittite, became King David's wife and the mother of Solomon?", "medium"),
    ("Esther", "Which Jewish queen risked her life to save her people from Haman's plot?", "easy"),
    ("Jezebel", "Which wicked queen, wife of Ahab, persecuted the prophets of God and was later thrown from a window?", "medium"),
    ("Delilah", "Which woman repeatedly pressed Samson to reveal the secret of his strength?", "easy"),
    ("Mary the mother of Jesus", "Which woman was told by the angel Gabriel that she would conceive and bear the Son of God?", "easy"),
    ("Elizabeth", "Which woman, mother of John the Baptist, was a relative of Mary and also conceived in her old age?", "medium"),
    ("Mary Magdalene", "Which woman, delivered of seven devils, was the first to see the risen Jesus at the tomb?", "medium"),
    ("Martha", "Which woman was busy with household tasks while her sister sat listening at Jesus' feet?", "medium"),
    ("Mary of Bethany", "Which woman anointed Jesus' feet with expensive perfume and wiped them with her hair?", "medium"),
    ("The Samaritan woman at the well", "Which woman spoke with Jesus at Jacob's well and then told her whole town about the Messiah?", "medium"),
    ("Lydia", "Which businesswoman, a seller of purple, became one of the first converts in Europe after hearing Paul preach?", "hard"),
    ("Priscilla", "Which woman, along with her husband Aquila, helped teach and correct the preacher Apollos?", "hard"),
    ("Dorcas", "Which woman, also called Tabitha, was known for good works and charity and was raised from the dead by Peter?", "hard"),
    ("Anna the prophetess", "Which elderly prophetess recognized the infant Jesus in the Temple and gave thanks to God?", "hard"),
    ("Rahab", "Which woman hid the Israelite spies in Jericho and was later listed in the genealogy of Jesus?", "medium"),
    ("Vashti", "Which queen refused King Ahasuerus' command to appear before his guests, leading to her removal?", "hard"),
]

def build():
    qs = []
    for correct, question, diff in FACTS:
        opts, idx = make_options(correct, NAMES)
        qs.append({
            "question": question, "options": opts, "correct_index": idx,
            "difficulty": diff, "category": "Women of the Bible",
        })
    return qs

if __name__ == "__main__":
    print(len(build()))
