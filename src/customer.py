from .bank import Bank
from .account import CurrentAccount, SavingsAccount
class Customer():
    """
        Customer
        Object representing a classical customer of bank
    """
    def __init__(self,name, bank: Bank, currentAccount: CurrentAccount, savingAccount: SavingsAccount):
        self.name = name
        self.bank = bank
        self.current_account = currentAccount
        self.saving_account = savingAccount
