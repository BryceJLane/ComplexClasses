from domino import *
import random

class Boneyard:
    """This class represents a 'deck' of dominos"""

    def __init__(self, maxDots = 12):
        """Creates a list of dominos from 0, 0 up to and including maxDots, maxDots"""
        self.__dominos = []
        for i in range(maxDots+1):
            for j in range(i, maxDots+1):
                self.__dominos.append(Domino(i, j))

    def shuffle(self):
        """Shuffles the list of dominos"""
        random.shuffle(self.__dominos)

    @property
    def isEmpty(self):
        """Determines when the list of dominos is empty"""
        return len(self.__dominos) == 0

    @property
    def dominosRemaining(self):
        """Returns the number of dominos remaining in the list"""
        return len(self.__dominos)

    def draw(self):
        """Returns the 'top' domino in the boneyard.  Removes the domino from the list"""
        return self.__dominos.pop(0)

    def __getitem__(self, item):
        """Allows a programmer to use [] to peek at a domino in the middle of the boneyard"""
        return self.__dominos[item]

    def __str__(self):
        """Creates a string representation of the boneyard"""
        return ', '.join(str(domino) for domino in self.__dominos)

    def __contains__(self, item):
        """Allows a programmer to use in operator to see if a domino is in the boneyard"""
        return item in self.__dominos
