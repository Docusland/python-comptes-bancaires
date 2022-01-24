from src.customer import Customer


class Bank:
    def __init__(self, name: str):
        """ default constructor """
        self.name = name
        self.customers = []
