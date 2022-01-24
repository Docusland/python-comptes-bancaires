import uuid

from src.account import Account
from src.bank import Bank


class Customer:
    def __init__(self, name, bank: Bank, current_account: Account, savings_account: Account):
        self.name = name
        self.bank = bank
        self.current_account = current_account
        self.savings_account = savings_account
