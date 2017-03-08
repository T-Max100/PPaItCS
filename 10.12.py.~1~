from random import choice, randint

# card.py
#    Class that represents playing cards


class Card:

    def __init__(self, rank, suit):
        self.rank = int(rank)
        self.suit = str(suit)

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        if self.rank > 9:
            return 10
        else:
            return self.rank

    def __str__(self):
        name = ""
        suit = ""
        rank = int(1)

        if self.suit == "d":
            suit = "Diamonds"
        elif self.suit == "c":
            suit = "Clubs"
        elif self.suit == "h":
            suit = "Hearts"
        elif self.suit == "s":
            suit = "Spades"

        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 2:
            rank = "Two"
        elif self.rank == 3:
            rank = "Three"
        elif self.rank == 4:
            rank = "Four"
        elif self.rank == 5:
            rank = "Five"
        elif self.rank == 6:
            rank = "Six"
        elif self.rank == 7:
            rank = "Seven"
        elif self.rank == 8:
            rank = "Eight"
        elif self.rank == 9:
            rank = "Nine"
        elif self.rank == 10:
            rank = "Ten"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"

        name = "{} of {}".format(rank, suit)

        return name


def main():
    suits = ["d", "c", "h", "s"]
    for i in range(int(input("Supply a whole number: "))):
        c = Card(randint(1, 13), choice(suits))
        print(c)
        print(c.BJValue())


if __name__ == "__main__":
    main()
