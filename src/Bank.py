from src.Customer import Customer


class Bank:
    def __repr__(self):
        return 'represent a bank'

    def __init__(self, bank_name: str):
        self.__name: str = bank_name
        self.__customers: list[Customer] = []

    def get_name(self) -> str:
        return self.__name

    def get_customers(self):
        return self.__customers

    def add_customer(self, customer: Customer):
        """
        add customer in the bank

        :param customer:
        """
        self.__customers.append(customer)

    def remove_customer(self, customer: Customer):
        """
        remove customer from the bank
        """
        for tested_customer in self.__customers:
            if tested_customer == customer:
                if tested_customer.can_be_removed():
                    self.__customers.remove(tested_customer)
                    break
