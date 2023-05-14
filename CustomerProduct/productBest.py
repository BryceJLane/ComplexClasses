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
    def id(self, id):
        self.__id = id

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return f"Product[{self.id}, {self.code}, {self.description}, {self.price}, {self.quantity}]"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.code == other.code
        return False
