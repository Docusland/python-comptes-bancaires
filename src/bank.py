from src.account import CurrentAccount, Account
from src.customer import Customer


class Bank:
    def __init__(self, name: str, customers: list[Customer]):
        self.__name = name
        self.__customers = customers

    def inner_tranfer(self, account_from: Account, account_to: Account):
        account_to.money_transfer(account_from.account_balance)
        account_from.money_withdraw(account_from.account_balance)

    @property
    def name(self):
        return self.__name

    @property
    def customers(self):
        return self.__customers

    # FIXME problème d'import ciculaire
    def find_customer_by_account_uuid(self, uuid: str):
        return "jean"

    def find_customer_by_customer_name(self, name: str):
        for customer in self.customers:
            if customer.name == name:
                return customer.name

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def remove_customer(self, name: str):
        for i in range(len(self.customers)):
            if self.customers[i].name == name:
                del self.customers[i]
