from src.account import CurrentAccount, SavingsAccount


class Client():
    def __init__(self, client_name):
        """ default constructor """
        Bank = "test"
        self.bank = Bank
        self.name = client_name
        self.current_account = CurrentAccount
        self.SavingsAccount = SavingsAccount
