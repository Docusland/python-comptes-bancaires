from src.account import Account


class Customer:
    def __init__(self, name: str, accounts: list):
        """ default constructor """
        self.name = name
        self.accounts = accounts
