from customer import Customer


class Bank():
    def __init__(self, name, customerList=None):
        if customerList is None:
            customerList = []
        self.name = name
        self.customers = customerList

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
