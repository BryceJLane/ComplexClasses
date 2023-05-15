from customer import Customer

class CustomerList:
    """This class represents a list of customer objects """

    # region constructor
    def __init__(self):
        self.__customers = []

    # region properties
    @property
    def count(self):
        return len(self.__customers)

    # endregion

    # region methods that provide functionality similar to the built-in list
    def append(self, customer):
        if isinstance(customer, Customer):
            self.__customers.append(customer)
        else:
            raise TypeError(f"Object must be a valid customer object {type(customer)}  {customer}")

    def pop(self, index=None):
        if index is None:
            return self.__customers.pop()
        else:
            return self.__customers.pop(index)

    def remove(self, customer):
        self.__customers.remove(customer)

    # endregion

    # region methods for updating customers
    def update_customer(self, index, new_customer):
        if isinstance(new_customer, Customer):
            if 0 <= index < self.count:
                self.__customers[index] = new_customer
            else:
                raise IndexError("Customer index out of range")
        else:
            raise TypeError(f"Object must be a valid customer object {type(new_customer)}  {new_customer}")

    # endregion

    # region methods for searching customers
    def search_customer_by_name(self, name):
        return [customer for customer in self.__customers if customer.name == name]

    def search_customer_by_email(self, email):
        return [customer for customer in self.__customers if customer.email == email]

    # endregion

    # region magic methods for list-like behavior
    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if 0 <= index < self.count:
            return self.__customers[index]
        else:
            raise IndexError("Customer index out of range")

    def __setitem__(self, index, value):
        if isinstance(value, Customer):
            if 0 <= index < self.count:
                self.__customers[index] = value
            else:
                raise IndexError("Customer index out of range")
        else:
            raise TypeError(f"Object must be a valid customer object {type(value)}  {value}")

    def __contains__(self, item):
        return item in self.__customers

    def __iter__(self):
        return iter(self.__customers)

    def __str__(self):
        return "\n".join(str(customer) for customer in self.__customers)
    # endregion



if __name__ == "__main__":
    customer_list = CustomerList()
    customer1 = Customer("John Doe", "johndoe@example.com")
    customer2 = Customer("Jane Doe", "janedoe@example.com")
    customer_list.add_customer(customer1)
    customer_list.add_customer(customer2)
    print(customer_list.count)
    print(customer_list.search_customer_by_name("John Doe"))
    print(customer_list.search_customer_by_email("janedoe@example.com"))
