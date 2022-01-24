import pytest

from src import bank
from src.account import Account, CurrentAccount
from unittest import TestCase

from src.bank import Bank
from src.customer import Customer

@pytest.mark.v2
class TestBank(TestCase):
    """" Unit testing for a Bank. """\

    @pytest.fixture
    def bank(self) -> Bank:
            """ Generate a default CC. """
            return Bank("Crédit Mutuel")

    def test_a_bank_exist(self):
        """ Check if a bank exist. """
        #assert
        self.v2.name == "Crédit Mutuel"

    def test_client_in_bank(self):
        """ Check if there is a client in the bank. """

        #act
        self.v2.add_customer("Toto", "Crédit Mutuel")



