from src.account import CurrentAccount


class Bank:
    def __init__(self, name):
        self.name = name

    def inner_tranfer(self, account_from: CurrentAccount, account_to: CurrentAccount):
        pass