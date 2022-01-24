from src.account import Account
from src.customer import Customer

class Bank:

    def __init__(self, name, customers):
        self.name = name
        self.customers = []

    # def inner_transfer(self, Account to, Account from):


    def find_customer_by_account_uuid(self, account_uuid):
        customer = ''
        for i in len(self.customers):
            if self.customers[i] == account_uuid:
                customer = self.customers[i]
        return customer

    def find_customer_by_customer_name(self, name):
        customer = ''
        for i in len(self.customers):
            if self.customers[i] == name:
                customer = self.customers[i]
        return customer

    def add_customer(self, Customer):
        self.customers.append(Customer.name)
        return self.customers

    def remove_customer(self, Customer):
        self.customers.remove(Customer.name)
        return self.customers

