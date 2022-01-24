from src.customer import Customer


class Bank:
    def __init__(self, name: str):
        """ default constructor """
        self.name = name
        self.customers = []

    def add_customer(self, customer: Customer) -> bool:
        self.customers.append(customer)
        return True
