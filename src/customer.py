import uuid
from abc import ABC
from src.account import CurrentAccount

class Customer(ABC):
    """
        Abstract class Compte
    """
    def __init__(self, name, bank):
        """default constructor"""
        self.name = name
        self.bank = bank
        self.current_account = CurrentAccount()
        self.savings_account = SavingAccount()

    def inner_transfer(self, account_from, target_account_uuid):
