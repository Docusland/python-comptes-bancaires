from src.bank import Bank


class Customer:

    def __init__(self, name: str, bank: Bank):
        """ default constructor """
        self._name = name
        self._bank = bank

    @property
    def name(self):
        return self.name

    @property
    def bank(self):
        return self.bank
