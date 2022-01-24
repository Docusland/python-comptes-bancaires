from abc import ABC

class Bank(ABC):

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def set_name(self):
        

