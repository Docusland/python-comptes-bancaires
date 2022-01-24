from .customer import Customer
class Bank():
    """
        Bank
        Contain customers
    """
    customers = list[Customer]

    def __init__(self, name):
        self.name = name

    def add_customer(self,customer:Customer):
        self.customers.append(customer)
