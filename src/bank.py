from customer import Customer
from account import Account


class Bank():
    def __init__(self, name, customerList: Customer):
        if customerList is None:
            customerList = []
        self.name = name
        self.customers = customerList

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def inner_transfer(self, account_from: Account, account_number_to: Account, amount: int):
        for i in range(len(self.customers)):
            if account_number_to.numero_compte == self.customers[i]:
                account_from.money_withdraw(amount)
                account_number_to.account_balance(amount)

    def find_customer_by_account_uuid(self, account_uuid: str) -> Customer:
        customer = None
        for i in range(len(self.customers)):
            if self.customers[i] == account_uuid:
                customer = self.customers[i]
        return customer

    def find_customer_by_customer_name(self, customer_name: str) -> Customer:
        customer = None
        for i in range(len(self.customers)):
            if self.customers.name[i] == customer_name:
                customer = self.customers[i]
        return customer
