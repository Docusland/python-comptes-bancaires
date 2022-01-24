from src.account import CurrentAccount as Ca
from src.account import CurrentAccount as Cc


class Customer:
    def __repr__(self):
        return 'represent a customer'

    def __init__(self):
        self.__currentAccount: Ca = Ca()
        self.__savingAccount: Cc = Cc()
