from src.account import Account
from src.customer import Customer


class Bank():
    """
        Bank
        Contain name and customers
    """

    def __init__(self, name):
        """Constructor."""
        self.name = name
        self.customers = []

    def add_customer(self, customer: Customer):
        """Add customer in list of customers"""
        self.customers.append(customer)

    def remove_customer(self, customer: Customer):
        """Remove customer in list of customers"""
        self.customers.remove(customer)

    def find_customer_by_account_uuid(self, account_uuid):
        """Find customer with account uuid in list of customers"""
        client = None
        for customer in self.customers:
            for account in customer.listAccount:
                if (account.numero_compte == account_uuid):
                    client = customer
        return client

    def find_customer_by_customer_name(self, name):
        """Find customer with customer name in list of customers"""
        client = None
        for customer in self.customers:
            if customer.name == name:
                client = customer
        return client

    def inner_transfert(self, account_from: Account, account_to: Account, montant):
        """
        Verify if account_from can transfert ammount and Transfert money from account_from to account_to with ammount
        return true if passed
        """
        if account_from.account_balance >= montant:
            account_from.money_transfer(100)
            account_to.money_transfer(100)
            return True
        else:
            return False
