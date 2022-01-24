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

    def test_add_customer(self, default_bank: Bank):
        """ Check if a customer is add to a bank. """

        assert default_bank.add_customer(Customer)
    def test_remove_customer(self, default_bank: Bank):
        """ Chef if a customer is remove from the bank"""

        assert default_bank.remove_customer(Customer)



