import uuid
from abc import ABC
from src.account import *
from src.bank import *


class Customer:

    def __init__(self,
                 name: str,
                 bank: str = "TheBank",
                 accounts: list = []
                 ):
        self.name = name
        self.bank = bank
        self.accounts = []

    def inner_transfer(self, from_account: CurrentAccount, target_account_uuid: str):
        pass

    def add_accounts(self, accounts: list[Account, ...]):
        for account in accounts:
            self.accounts.append(account)

    def delete_account(self, account: Account):
        for acc in self.accounts:
            if acc == account:
                self.accounts.remove(account)

    def can_be_removed(self) -> bool:
        total_account: int = 0
        for account in self.accounts:
            total_account += account.account_balance
        return total_account == 0
