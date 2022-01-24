import pytest

from src import bank
from src.account import Account, CurrentAccount
from unittest import TestCase

from src.bank import Bank
from src.customer import Customer


class TestBank(TestCase):
    """" Unit testing for a Bank. """

    def setUp(self):
        self.v2 = Bank('Crédit Mutuel')

    def test_a_bank_exist(self):
        """ Check if a bank exist. """
        #act
        self.v2.name = "Crédit Mutuel"



