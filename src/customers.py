from account import Account


class Customer:
    """
       Abstract class Customer
    """

    def __init__(self, name):
        """ default constructor """
        self.name = name
        self.accounts = Account(name)


