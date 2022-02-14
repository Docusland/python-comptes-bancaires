from account import *


class Customer():
    def __init__(self, name, bank, accountList: Account):
        if accountList is None:
            accountList = []
        self.name = name
        self.bank = bank
        self.accounts = accountList

    def add_account(self, account: Account):
        self.accounts.append(account)

    def remove_account(self, account: Account):
        if self.can_be_remove():
            self.accounts.remove(account)

    def can_be_remove(self):
        for i in range(len(self.accounts)):
            account = self.accounts
            if account.account_balance == 0:
                return True
            else:
                print("Argent toujours présent sur le compte")
                return False
