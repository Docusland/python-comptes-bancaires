from src.customers import Customer


class Bank:
    """
       Abstract class Bank
    """

    def __init__(self, name):
        """ default constructor """
        self.name = name
        self.customers = []

    def new_customer(self, customer_name):
        self.customers.append(Customer(customer_name, self.name))

    def delete_customer(self, customer_id):
        self.customers.pop(customer_id)

