from .account import Account, CurrentAccount, SavingsAccount
class Customer():
    """
        Customer
        Object representing a classical customer of bank
        Contain name, bank and list of account
    """
    def __init__(self,name, listAccount):
        self.name = name
        self.listAccount = listAccount


