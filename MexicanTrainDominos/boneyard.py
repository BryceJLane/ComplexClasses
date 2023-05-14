from domino import *

class Boneyard:
    """This class represents a 'deck' of dominos"""

    def __init__(self, maxDots = 12):
        """Creates a list of dominos from 0, 0 up to and including maxDots, maxDots"""
        self.__dominos = []
        self.__dominos.append(Domino(1, 1))

    def shuffle(self):
        """Shuffles the list of dominos"""

    @property
    def isEmpty(self):
        """Determines when the list of dominos is empty"""

    @property
    def dominosRemaining(self):
        """Returns the number of dominos remaining in the list"""

    def draw(self):
        """Returns the 'top' domino in the boneyard.  Removes the domino from the list"""

    def __getitem__(self, item):
        """Allows a programmer to use [] to peek at a domino in the middle of the boneyard"""

    def __str__(self):
        """Creates a string representation of the boneyard"""




