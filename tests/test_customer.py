import pytest

from unittest import TestCase

from src.customer import Customer


class TestCustomer(TestCase):
    """" Unit testing for a Bank. """

    @pytest.fixture
    def bank(self) -> Customer:
            """ Generate a default CC. """
            return Customer("Toto")

    def test_a_client_exist(self):
        """ Check if a bank exist. """
        #assert
        self.v2.name == "Toto"


