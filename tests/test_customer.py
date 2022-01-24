import pytest

from src.account import Account, CurrentAccount
from unittest import TestCase

from src.customer import Customer


class TestCustomer(TestCase):
    """" Unit testing for a Bank. """

    def default_customer(self) -> Customer:
        """ Generate a default CC. """
        return Customer("Toto", "Crédit Mutuel")

    def test_a_customer_exist(self):
        """ Check if a customer exist. """
        #assert
        self.default_customer().name == "Toto", "Crédit Mutuel"

    def test_customer_add_account(self, default_customer: Customer):
        """ Check if an account is add to a customer """
        assert default_customer.add_account(Account)

    def test_customer_remove_account(self, default_customer: Customer):
        """ Check if an account is delete to a customer """
        assert default_customer.remove_account(Account)


