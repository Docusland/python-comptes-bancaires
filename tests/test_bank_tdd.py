"""
    Unit testing for Bank.
"""

import unittest

from src.Bank import Bank
from src.customer import Customer
import pytest


class TestBank(unittest.TestCase):
    """ Unit testing for Banks. """

    SUPPOSED_BANK_NAME = 'bank'

    @pytest.fixture
    def default_bank(self) -> Bank:
        """ default bank object """
        return Bank(bank_name=self.SUPPOSED_BANK_NAME)

    def test_i_create_nw_bank(self, default_bank: Bank):
        assert Bank(self.default_bank).get_name() == self.SUPPOSED_BANK_NAME

    def test_i_append_customer(self):
        bank = Bank('toto')
        bank.add_customer(Customer('Benoit'))
        bank.add_customer(Customer('Pikachu'))
        assert len(bank.get_customers()) == 2

    def test_i_remove_customer(self):
        bank = Bank('toto')
        bank.add_customer(Customer('Benoit'))
        bank.add_customer(Customer('Pikachu'))
        bank.remove_customer()
        assert len(bank.remove_customer()) == 1
