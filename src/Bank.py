from src.Customer import Customer


class Bank:
    def __repr__(self):
        return 'represent a bank'

    def __init__(self, bank_name: str):
        self.__name: str = bank_name
        self.__customers: list[Customer] = []

    def get_name(self) -> str:
        return self.__name

    def add_customer(self, customer: Customer):
        """
        add customer in the bank

        :param customer:
        """
