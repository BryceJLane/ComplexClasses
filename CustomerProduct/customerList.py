from customer import Customer

class CustomerList:
    """This class represents a list of customer objects """

    # region constructor
    def __init__(self):
        self.__customers = []

    # endregion

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

    def find_by_email(self, email):
        for index, customer in enumerate(self.__customers):
            if customer.email == email:
                return index
        return -1
    # endregion
    # region methods for updating and deleting customers
    def update_customer(self, index, new_customer):
        if isinstance(new_customer, Customer):
            if 0 <= index < self.count:
                self.__customers[index] = new_customer
            else:
                raise IndexError("Customer index out of range")
        else:
            raise TypeError(f"Object must be a valid customer object {type(new_customer)}  {new_customer}")

    def delete_customer(self, index):
        if 0 <= index < self.count:
            del self.__customers[index]
        else:
            raise IndexError("Customer index out of range")
    # endregion
    # region methods for searching customers
    def search_customer_by_name(self, name):
        return [customer for customer in self.__customers if customer.name == name]

    def search_customer_by_email(self, email):
        return [customer for customer in self.__customers if customer.email == email]
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
