from src.bank import Bank


class Customer:
    def __init__(self, name: str, bank: Bank):
        self.name = name
        self.bank = bank

    def add_customer_to_bank(self, bank: Bank):
        bank.add_customer(self)
