from deck import *


def testConstructor():
    d = Deck()
    print(f"Testing constructor.  Expect deck of 52 cards. {d}")
    print(f"Expect numCards property to be 52. {d.numCards}")
    print(f"Expect isEmpty property to be false. {d.isEmpty}")


def testShuffle():
    d = Deck()
    d.shuffle()
    print(f"Testing shuffle.  Expect deck of 52 cards. {d}")
    print(f"Expect numCards property to be 52. {d.numCards}")
    print(f"Expect isEmpty property to be false. {d.isEmpty}")


def testDeal():
    d = Deck()
    print(f"Testing deal.  Expect deck of 52 cards. {d}")
    print(f"Expect numCards property to be 52. {d.numCards}")
    print(f"Expect isEmpty property to be false. {d.isEmpty}")
    c = d.deal()
    print(f"after call to deal.  Expect deck of 51 cards. {d}")
    print(f"Expect numCards property to be 51. {d.numCards}")
    print(f"Expect isEmpty property to be false. {d.isEmpty}")
    print(f"Expect dealt card to be Ace of Clubs. {c}")
    for i in range(d.numCards):
        c = d.deal()
    print(f"Dealt the remaining cards.  Expect empty deck. {d}")
    print(f"Expect numCards property to be 0. {d.numCards}")
    print(f"Expect isEmpty property to be true. {d.isEmpty}")


def testGetItem():
    d = Deck()
    print(f"Testing deal.  Expect deck of 52 cards. {d}")
    print(f"Expect numCards property to be 52. {d.numCards}")
    print(f"Expect isEmpty property to be false. {d.isEmpty}")
    c = d[51]
    print(f"used [51].  Expect deck to remain the same. {d}")
    print(f"Expect numCards property to be 52. {d.numCards}")
    print(f"Expect isEmpty property to be false. {d.isEmpty}")
    print(f"Expect last card to be King of Spades. {c}")


def testIn():
    d = Deck()
    c1 = d.deal()
    print(f"Testing in.  Current unshuffled deck without Ace of Clubs. {d}")
    c2 = d[4]
    print(f"Is Ace of Clubs in the deck?  Expect false  {c1 in d}")
    print(f"Is 2 of Clubs in the deck?  Expect true  {c2 in d}")


def testForLoop():
    d = Deck()
    print(f"Testing for loop.")
    print(f"Iterating through the deck with for in.  Expect 52 individual cards")
    for c in d:
        print(c)
