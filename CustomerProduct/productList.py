from productBest import *


class ProductList:
    """This class represents a list of product objects """

    # region constructor
    def __init__(self):
        self.__products = []

    # endregion

    # region properties
    @property
    def count(self):
        return len(self.__products)

    # endregion

    # region methods that provide functionality similar to the built in list
    def append(self, item):
        if isinstance(item, Product):
            self.__products.append(item)
        else:
            raise TypeError(f"Object must be a valid product object {type(item)}  {item}")

    def pop(self, index=None):
        if index is None:
            return self.__products.pop()
        else:
            return self.__products.pop(index)

    def find(self, item):
        if isinstance(item, Product):
            index = 0
            for product in self.__products:
                if product == item:
                    return index
                index += 1
            return -1
        elif isinstance(item, str):
            index = 0
            for product in self.__products:
                if product.code == item:
                    return index
                index += 1
            return -1
        else:
            return -1

    def remove(self, item):
        index = self.find(item)
        if index == -1:
            raise ValueError(f"{item} is not in the product list")
        else:
            self.pop(index)

    def clear(self):
        self.__products = []

    # endregion

    # region magic or dunder methods
    def __str__(self):
        output = f"ProductList["
        for product in self.__products:
            output += product.__str__() + " "
        output += "]"
        return output

    def __len__(self):
        """Allows a programmer to use the len function to get the length of a product list"""
        return len(self.__products)

    def __getitem__(self, item):
        """Allows a programmer to [] to get an element in a product list"""
        if isinstance(item, int):
            return self.__products[item]
        elif isinstance(item, str):
            return self.__products[self.find(item)]
        else:
            raise TypeError(f"Index must an int or a 4 character string {type(item)}  {item}")

    def __setitem__(self, key, value):
        """Allows a programmer to [] to mutate an element in a product list"""
        if isinstance(key, int) and isinstance(value, Product):
            self.__products[key] = value
        elif not isinstance(key, int):
            raise TypeError(f"Index must an int {type(key)}  {key}")
        elif not isinstance(value, Product):
            raise TypeError(f"Item must a Product object {type(value)}  {value}")

    def __delitem__(self, key):
        """Allows a programmer to use del to delete an element from a product list"""
        if isinstance(key, int):
            del self.__products[key]
        else:
            raise TypeError(f"Index must an int {type(key)}  {key}")

    def __add__(self, other):
        """Allows concatenation of product lists.  Does not make a copy of the individual products"""
        if isinstance(other, ProductList):
            newList = ProductList()
            for p in self.__products:
                newList.append(p)
            for p in other.__products:
                newList.append(p)
            return newList
        else:
            raise TypeError(f"Other must a product list {type(other)}  {other}")

        ''' documentation suggests these are necessary to use in operator and for loop but testing indicates they are NOT necessary.
        I assume that's because we have written __eq__ in thee Product class and __getItem__ in ProductList
        def __contains__(self, item):
            if isinstance(item, Product):
                return self.find(item) != -1
            else:
                return False

        def __iter__(self):
            return self.__products.__iter__()

        def __next__(self):
            return self.__products.__next__()
        '''

    # endregion
