import uuid

from src import account
# from src.bank import Bank
from src.account import Account

class Customer:

    def __init__(self, name):
        self.name = name
        # self.bank = Bank
        self.accounts = []

    def add_account(self, Account):
        account_number = Account.numero_compte
        self.accounts.append(Account(account_number))

    def remove_account(self, Account):
        account_number = Account.numero_compte
        if(Customer.remove_account == 1):
            self.accounts.remove(Account(account_number))

    def can_be_remove(self):
        for i in len(self.accounts):
            if (self.accounts[i].account_balance == 0):
                return 1
            else:
                return 0