from src.account import CurrentAccount, SavingsAccount, Account


class Customer:
    def __init__(self, name: str, accounts: list[Account]):
        self.__name = name
        self.__accounts = accounts

    def inner_transfer(self, account_from: Account, target_account_id: str):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def accounts(self):
        return self.__accounts
