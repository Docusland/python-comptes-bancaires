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
        self.__accounts: list[Ca | Sa | Account] = [
            Ca(owner_name=self.__name),
            Sa(owner_name=self.__name),
        ]

    def get_name(self) -> str:
        """ return customer name """
        return self.__name

    def get_ca_name(self) -> str:
        """ return current account name """
        return self.__accounts[0].owner_name

    def get_sc_name(self) -> str:
        """ return current account name """
        return self.__accounts[1].owner_name

    def get_accounts(self):
        """ get customer account """
        return self.__accounts

    def add_account(self, account: Account):
        """
        add an account for the customer

        :param account:
        """
        self.__accounts.append(account)

    def remove_account(self, account: Account):
        """
        remove an account for the customer

        :param account:
        """
        for existing_account in self.__accounts:
            if existing_account.owner_name == account.owner_name:
                self.__accounts.remove(existing_account)
                break

    def can_be_removed(self) -> bool:
        """
        check if an account can be removed
        """
        return len(self.__accounts) == 0
