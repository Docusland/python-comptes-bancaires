from account import *


class Customer():
    def __init__(self, name, bank, accountList=None):
        if accountList is None:
            accountList = []
        self.name = name
        self.bank = bank
        self.accounts = accountList

    def add_account(self, account: Account):
        self.accounts.append(account)

    def remove_account(self, account: Account):
        if self.can_be_remove(account):
            self.accounts.remove(account)

    def can_be_remove(self, account: Account):
        if account.account_balance == 0:
            return True
        else:
            print("Argent toujours présent sur le compte")
            return False
