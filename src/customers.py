from src.account import Account


class Customer:
    """
       Abstract class Customer
    """

    def __init__(self, name, bank_name):
        """ default constructor """
        self.name = name
        self.accounts = []
        self.bank = bank_name

    def create_account(self, account_name):
        self.accounts.append(Account(account_name))