from src.account import Account


class Customer:
    """
        Customer.
        Object representing a classic customer.
        Has a name, is affiliated to a bank, possess accounts
    """

    def __init__(self, name):
        self.name = name
        self.bank = None
        self.accounts = []

    def add_bank(self, bank):
        """ Assign bank to customer"""
        self.bank = bank

    def remove_bank(self):
        """ Remove bank from customer"""
        self.bank = None

    def get_bank(self):
        """ Return customer's bank"""
        return self.bank

    def add_account(self, account: Account):
        """ Add any type of account"""
        self.accounts.append(account)

    def remove_account(self, account: Account):
        """ Remove any type of account"""
        self.accounts.remove(account)

    def get_accounts(self):
        """ Return array of customer's accounts"""
        return self.accounts

    def can_be_removed(self):
        """ Return true if array of accounts is null"""
        if len(self.accounts) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.name} {self.bank} {self.accounts}'

