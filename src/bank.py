from src.customer import Customer


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
