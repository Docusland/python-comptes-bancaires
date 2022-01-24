from abc import ABC


class Customer(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, name):
        """ default constructor """
        self.name = name
