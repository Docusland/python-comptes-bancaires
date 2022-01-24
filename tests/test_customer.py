"""
    Unit testing for a Customer.
"""

import pytest
from src.customer import Customer


@pytest.mark.c
class TestCustomer():
    """ Unit testing for a Customer. """

    @pytest.fixture
    def customer(self) -> Customer:
        """ Generate a default customer """
        customer = Customer('Sterenn Grace')
        return customer

    def test_c_add_customer(self, customer: Customer) -> None:
        assert customer.name == 'Sterenn Grace'
