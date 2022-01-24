from src.customer import Customer


class Bank:
    def __init__(self, name: str):
        """ default constructor """
        self.name = name
        self.customers = []

    def add_customer(self, customer: Customer) -> bool:
        self.customers.append(customer)
        return True

    def remove_customer(self, customer: Customer) -> bool:
        if customer in self.customers:
            self.customers.remove(customer)
            return True
        else:
            raise Exception(str(customer.name) + ' is not a customer of the bank')
