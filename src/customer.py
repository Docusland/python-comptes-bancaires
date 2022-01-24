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

    def add_account(self, account):
        """Add an account in listAccount"""
        self.listAccount.append(account)
        return account

    def remove_account(self, account):
        """Remove account if this account have no money and exist in listAccount"""
        if account.account_balance == 0:
            if account in self.listAccount:
                self.listAccount.remove(account)
                return True
            else:
                return False
        else:
            return False

    def can_be_removed(self):
        can_remove = True
        for account in self.listAccount:
            if account.account_balance > 0:
                can_remove = False
        return can_remove