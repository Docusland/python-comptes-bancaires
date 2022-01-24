from src.account import Account
from src.account import CurrentAccount as Ca
from src.account import SavingsAccount as Sa
import uuid


class Customer:
    def __repr__(self):
        return 'represent a customer'

    def __init__(self, customer_name: str):
        self.__name: str = customer_name

        # TODO implement bank
        # self.__bank: str = customer_name

        # the current account will always be the first item
        # and the saving account the second
        self.accounts: list[Ca | Sa | Account] = [
            Ca(owner_name=self.__name),
            Sa(owner_name=self.__name),
        ]

    def get_name(self) -> str:
        """ return customer name """
        return self.__name

    def get_ca_name(self) -> str:
        """ return current account name """
        return self.accounts[0].owner_name

    def get_sc_name(self) -> str:
        """ return current account name """
        return self.accounts[1].owner_name

    def add_account(self, account: Account):
        """
        add an account for the customer

        :param account:
        """
        pass

    def remove_account(self, account: Account):
        """
        remove an account for the customer

        :param account:
        """
        pass

    def can_be_removed(self):
        """
        check if an account can be removed
        """
        pass
