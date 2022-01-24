from account import *


class Customer():
    def __init__(self, name, bank, current_account: CurrentAccount, savings_account: SavingsAccount):
        self.name = name
        self.bank = bank
        self.current_account = current_account
        self.savings_account = savings_account
