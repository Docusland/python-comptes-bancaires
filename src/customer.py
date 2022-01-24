from src.account import CurrentAccount, SavingsAccount
from src.bank import Bank


class Customer():
    def __init__(self, name):
        """ default constructor """
        self.name = name
        Bank.__init__(self)
        CurrentAccount(self)
        SavingsAccount(self)

   ## def inner_transfer(self, account_from, target_account_uuid):