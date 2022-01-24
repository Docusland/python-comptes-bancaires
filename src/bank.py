from abc import ABC

class Bank(ABC):
    def __init__(self, name):
        self.customers = []
        self.name = name




