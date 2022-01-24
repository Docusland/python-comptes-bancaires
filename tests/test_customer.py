import pytest

from src.account import Account, CurrentAccount
from unittest import TestCase

from src.customer import Customer
from src.customer import Customer


class TestCustomer(TestCase):
    """" Unit testing for a Bank. """

    def setUp(self):
        self.v2 = Customer('Toto')

    def test_a_client_exist(self):
        """ Check if a bank exist. """
        #assert
        self.v2.name == "Toto"


