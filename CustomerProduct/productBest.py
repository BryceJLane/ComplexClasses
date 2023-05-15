class Product:
    def __init__(self, id, code, description, price, quantity):
        self.__id = id
        self.__code = code
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def __str__(self):
        return f"Product[{self.__id}, {self.__code}, {self.__description}, {self.__price}, {self.__quantity}]"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.__code == other.__code
        return False
