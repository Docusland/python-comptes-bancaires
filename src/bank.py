from src.account import Account
from src.customer import Customer


class Bank():
    """
        Bank
        Contain name and customers
    """

    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def remove_customer(self, customer: Customer):
        self.customers.remove(customer)

    def find_customer_by_account_uuid(self, account_uuid):
        client = None
        for customer in self.customers:
            for account in customer.listAccount:
                if (account.numero_compte == account_uuid):
                    client = customer
        return client

    def find_customer_by_customer_name(self, name):
        client = None
        for customer in self.customers:
            if customer.name == name:
                client = customer
        return client

    def inner_transfert(self, account_from: Account, account_to: Account, montant):
        if account_from.account_balance >= montant:
            account_from.money_withdraw(100, True)
            account_to.money_transfer(100)
            return True
        else:
            return False
