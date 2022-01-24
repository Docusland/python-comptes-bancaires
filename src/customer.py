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

    def add_account(self, account: Account):
        self.__accounts.append(account)

    def remove_account(self, account_to_delete: Account):
        for account in self.__accounts:
            if type(account) == type(account_to_delete):
                del account
                return

    def can_be_removed(self, account_to_remove: Account):
        if account_to_remove.account_balance == 0:
            return True
        else:
            return False
