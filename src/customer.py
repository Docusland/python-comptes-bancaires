from src import account
# from src.bank import Bank
from src.account import Account

class Customer:

    def __init__(self, name):
        self.name = name
        # self.bank = Bank
        self.accounts = []

    def add_account(self, Account):
        account = Account()
        self.accounts = account

    # def remove_account(self):
    #
    # def can_be_remove(self):
