from account import CurrentAccount, SavingsAccount
from bank import Bank


class Customer:
    """
       Abstract class Customer
    """

    def __init__(self):
        """ default constructor """
        self.name = ""
        self.bank = Bank
        self.current_account = CurrentAccount
        self.savings_account = SavingsAccount


