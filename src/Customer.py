from src.account import CurrentAccount as Ca
from src.account import SavingsAccount as Sa


class Customer:
    def __repr__(self):
        return 'represent a customer'

    def __init__(self, customer_name: str):
        self.__name: str = customer_name

        # TODO implement bank
        # self.__bank: str = customer_name

        self.__currentAccount: Ca = Ca(owner_name=self.__name)
        self.__savingAccount: Sa = Sa(owner_name=self.__name)

    def get_name(self) -> str:
        """ return customer name """
        return self.__currentAccount.owner_name

    def get_ca_name(self) -> str:
        """ return current account name """
        return self.__currentAccount.owner_name

    def get_sc_name(self) -> str:
        """ return current account name """
        return self.__savingAccount.owner_name
