from account import CurrentAccount, SavingsAccount
from banks import Bank


class Customer:
    """
       Abstract class Customer
    """

    def __init__(self, name):
        """ default constructor """
        self.name = name
        self.bank = Bank
        self.current_account = CurrentAccount
        self.savings_account = SavingsAccount


