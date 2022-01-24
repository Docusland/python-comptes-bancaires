"""
    Unit testing for a Bank.
"""
import pytest
from src.bank import Bank


@pytest.mark.b
class TestBank():

    @pytest.fixture
    def bank(self) -> Bank:
        """ Generate a default customer """
        bank = Bank('ING')
        return bank

    def test_b_add_new_bank_with_ing_name(self, bank: Bank) -> None:
        assert bank.name == 'ING'
