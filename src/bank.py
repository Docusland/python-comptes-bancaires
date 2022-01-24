from abc import ABC


class Bank(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, name, isAdmin):
        """ default constructor """
        self.name = name
        self.isAdmin = isAdmin

