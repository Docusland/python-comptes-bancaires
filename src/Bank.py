from src.customer import Customer

class Bank:
    def __init__(self, bank_name: str):
        self.__name: str = bank_name
        self.__customers: list = []

    def get_customers(self):
        return self.__customers

    def get_name(self) -> str:
        return self.__name

    def add_customer(self, customer):
        """
        :param customer:
        """
        self.__customers.append(customer)

    def remove_customer(self, customer):
        """
        :param customer:
        """
        self.__customers.remove(customer)
