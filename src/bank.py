from src.account import CurrentAccount, Account
from src.customer import Customer


class Bank:
    def __init__(self, name: str, customers: list[Customer]):
        self.__name = name
        self.__customers = customers

    def inner_tranfer(self, account_from: Account, account_to: Account):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def customers(self):
        return self.__customers
