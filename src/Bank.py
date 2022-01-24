from src.Customer import Customer
from src.account import Account


class Bank:
    def __repr__(self):
        return 'represent a bank'

    def __init__(self, bank_name: str):
        self.__name: str = bank_name
        self.__customers: list[Customer] = []

    def get_name(self) -> str:
        return self.__name

    def get_customers(self) -> list:
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

    def find_customer_by_name(self, name: str) -> bool | Customer:
        if len(self.__customers) > 0:
            for customer in self.__customers:
                if customer.get_name() == name:
                    return customer
        return False

    def find_customer_by_account_uuid(self, account_uuid: str) -> bool | Customer:
        """
        find customer by uuid number

        :param account_uuid:
        :return bool | Customer:
        """
        if len(self.__customers) > 0:
            for customer in self.__customers:
                if len(customer.get_accounts()) > 0:
                    for account in customer.get_accounts():
                        if account.numero_compte == account_uuid:
                            return customer
        return False

    @classmethod
    def inner_transfer(cls, account_from: Account, account_to: Account, amount: int):
        """
        perform transfer from an account to another
        """
        amount = account_from.money_withdraw(amount=amount)
        account_to.money_transfer(montant=amount)
