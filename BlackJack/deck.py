from card import *
from random import randint


class Deck:
    """This class represents a standard deck of (playing) cards"""

    def __init__(self):
        """creates a deck of 52 cards"""
        self.__cards = []
        for value in range(1, 14):
            for suit in range(1, 5):
                self.__cards.append(Card(value, suit))

    @property
    def numCards(self):
        """returns the number of cards in the deck"""
        return len(self.__cards)

    @property
    def isEmpty(self):
        """returns true when the deck has no more cards and false otherwise"""
        return len(self.__cards) == 0

    def deal(self):
        """returns the top card in the deck or None when the deck is empty"""
        if not self.isEmpty:
            c = self.__cards.pop(0)
            return c
        else:
            return None

    def shuffle(self):
        """shuffles the cards in the deck"""
        for i in range(self.numCards):
            rndIndex = randint(0, self.numCards - 1)
            self.__cards[i], self.__cards[rndIndex] = self.__cards[rndIndex], self.__cards[i]

    def __str__(self):
        """creates a string representation of the cards in the deck"""
        output = f"Deck["
        for c in self.__cards:
            output += f"{c} "
        output += "]\n"
        return output

    def __getitem__(self, item):
        """Allows a programmer to [] to peek at a card in the deck"""
        if isinstance(item, int):
            return self.__cards[item]
        else:
            raise TypeError(f"Index must an int {type(item)}  {item}")

