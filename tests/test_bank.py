import pytest

from src import bank
from src.account import Account, CurrentAccount
from unittest import TestCase

from src.bank import Bank
from src.customer import Customer


class TestBank(TestCase):
    """" Unit testing for a Bank. """

    def default_bank(self) -> Bank:
        """ Generate a default CC. """
        return Bank("Crédit Mutuel")

    def test_a_bank_exist(self):
        """ Check if a bank exist. """
        #assert
        self.default_bank().name == "Crédit Mutuel"

    def test_client_in_bank(self, default_bank: Bank):
        """ Check if there is a client in the bank. """

        assert default_bank.add_customer("Toto", "Crédit Mutuel")



