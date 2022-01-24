from abc import ABC

from src.account import Account
from src.customer import Customer


class Bank(ABC):
    def __init__(self, bank, customers):
        self.bank = bank
        self.customers = customers

    def inner_transfer(self, account: Account, to: Account):
        pass

    def find_customer_by_account_uuid(self, account_uuid):
        pass

    def find_customer_by_customer_name(self, name):
        pass

    def add_customer(self, customer: Customer):
        pass

    def remove_customer(self, customer: Customer):
        pass
