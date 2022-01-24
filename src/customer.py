from abc import ABC

from src.account import Account


class Customer(ABC):
    def __init__(self, name, bank, accounts: []):
        self.name = name
        self.bank = bank
        self.accounts = accounts

    def add_account(self, account: Account):
        pass

    def remove_account(self, account: Account):
        pass

    def can_be_remove(self):
        pass
