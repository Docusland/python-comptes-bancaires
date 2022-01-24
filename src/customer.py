from src.bank import Bank
from src.account import Account


class Customer:
    def __init__(self, name: str, bank: Bank):
        self._name = name
        self._bank = bank
        self._accounts = []

    def add_account(self, account: Account):
        pass

    def remove_account(self, account: Account):
        pass

    def can_be_removed(self) -> bool:
        pass

    @property
    def name(self) -> str:
        return self._name
