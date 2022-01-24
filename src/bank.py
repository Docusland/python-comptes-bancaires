from src.account import Account
from src.customer import Customer

class Bank:

    def __init__(self, name, customers):
        self.name = name
        self.customers = []

    # def inner_transfer(self, Account from, Account to):
    #
    # def find_customer_by_account_uuid(self):
    #
    def find_customer_by_customer_name(self, name):
        customer = ''
        for i in len(self.customers):
            if(self.customers[i] == name):
                customer = self.customers[i]
        return customer

    def add_customer(self, Customer):
        self.customers.append(Customer.name)
        return self.customers

    def remove_customer(self, Customer):
        self.customers.remove(Customer.name)
        return self.customers

