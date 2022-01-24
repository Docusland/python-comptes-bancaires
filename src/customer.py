from src.bank import Bank


class Customer(Bank):

    def __init__(self, name, bank):
        """ default constructor """
        self.name = name
        Bank = bank