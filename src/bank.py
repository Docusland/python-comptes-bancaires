from abc import ABC

class Bank(ABC):
    def __init__(self, name):
        self.name = name
        self.customers = []

