class Customer:
    """This class represents a customer object"""

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    #region properties
    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
    #endregion

    #region string representation
    def __str__(self):
        return f'Customer Name: {self.__name}, Email: {self.__email}'
    #endregion

    #region equality checks
    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.__name == other.name and self.__email == other.email
        return False
    #endregion
