from src.customer import Customer

class Bank:
    def __init__(self, bank_name: str):
        self.__name: str = bank_name
        self._customers: list = []

    def get_customers(self):
        return self._customers

    def get_name(self) -> str:
        return self.__name

    def add_customer(self, customer):
        """
        :param customer:
        """
        self._customers.append(customer)

    def remove_customer(self, customer):
        """
        :param customer:
        """
        self._customers.remove(customer)
