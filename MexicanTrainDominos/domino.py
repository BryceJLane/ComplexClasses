class Domino:
    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2

    @property
    def side1(self):
        return self.__side1

    @side1.setter
    def side1(self, side1):
        if not 0 <= side1 <= 12:
            raise ValueError("Side value must be between 0 and 12")
        self.__side1 = side1

    @property
    def side2(self):
        return self.__side2

    @side2.setter
    def side2(self, side2):
        if not 0 <= side2 <= 12:
            raise ValueError("Side value must be between 0 and 12")
        self.__side2 = side2

    def flip(self):
        self.__side1, self.__side2 = self.__side2, self.__side1

    def is_double(self):
        return self.__side1 == self.__side2

    def __str__(self):
        return f"[{self.__side1}|{self.__side2}]"

    def __eq__(self, other):
        if isinstance(other, Domino):
            return (self.__side1, self.__side2) == (other.side1, other.side2) or (self.__side1, self.__side2) == (other.side2, other.side1)
        else:
            return False
