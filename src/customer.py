from src.account import Account


class Customer:
    """
       Abstract class Customer
    """

    def __init__(self, name, bank_name):
        """ default constructor """
        self.name = name
        self.accounts = Account(name)
        self.bank = bank_name
