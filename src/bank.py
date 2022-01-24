import uuid
from src.customer import Customer
from src.account import *


class Bank:
    def __init__(self,
                 name: str,
                 customers: list
                 ):
        self.name: str = "TheBank"
        self.customers = []

    def inner_transfer(self,
                       from_account: Account,
                       to_account: Account,
                       amount: int
                       ):
        from_account.money_withdraw(amount)
        to_account.money_transfer(amount)

    def find_customer_by_account_uuid(self, account_uuid: int):
        name: str = "Unknown"
        for customer in self.customers:
            for account in customer.accounts:
                if account.numero_compte == account_uuid:
                    name = account.owner_name
        return name
