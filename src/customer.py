from src.account import CurrentAccount, SavingsAccount


class Customer:
    def __init__(self, name: str, current_acount: CurrentAccount, savings_acount: SavingsAccount):
        self.__name = name
        self.__current_acount = current_acount
        self.__savings_acount = savings_acount

    def inner_transfer(self, account_from : CurrentAccount, target_acount_id : str):
        pass
