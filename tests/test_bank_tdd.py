"""
    Unit testing for Bank.
"""

from src.Bank import Bank
from src.customer import Customer
import pytest


class TestBank:
    """ Unit testing for Banks. """

    SUPPOSED_BANK_NAME = 'bank'

    @pytest.fixture
    def default_bank(self) -> Bank:
        """ default bank object """
        return Bank(self.SUPPOSED_BANK_NAME)

    def test_i_create_new_bank(self, default_bank: Bank):
        assert default_bank.get_name() == self.SUPPOSED_BANK_NAME

    def test_i_append_customer(self, default_bank: Bank):
        benoit = Customer('Benoit')
        pikachu = Customer('Pikachu')
        default_bank.add_customer(benoit)
        default_bank.add_customer(pikachu)
        assert len(default_bank.get_customers()) == 2

    def test_i_remove_customer(self, default_bank: Bank):
        benoit = Customer('Benoit')
        default_bank.add_customer(benoit)
        default_bank.add_customer(Customer('Pikachu'))
        default_bank.remove_customer(benoit)
        assert len(default_bank.get_customers()) == 1
