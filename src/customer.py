from .bank import Bank
from .account import Account, CurrentAccount, SavingsAccount
class Customer():
    """
        Customer
        Object representing a classical customer of bank
    """
    def __init__(self,name, bank: Bank, listAccount):
        self.name = name
        self.bank = bank
        self.listAccount = listAccount

    #def inner_transfert(self, from_account, target_account_uuid):

