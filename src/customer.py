from src import account
from src.account import Account
from src.bank import Bank

accounts = []


class Customer(Bank):

    def __init__(self, name, bank):
        """ default constructor """
        self.name = name
        Bank = bank

    def add_account(Account):
        """ add an account to a customer """
        accounts.append(Account)

    def remove_account(Account):
        """ remove an account to a customer"""
        accounts.remove(Account)
