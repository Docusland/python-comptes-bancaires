class Customer:

    def __init__(self, customer_name, customer_new_account):
        self.__name: str = customer_name
        self.__new_account: str = customer_new_account

    def get_name(self) -> str:
        return self.__name

    def get_new_account(self) -> str:
        return self.__new_account
