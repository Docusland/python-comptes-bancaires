"""
    Unit testing for a Customer.
"""

import pytest
from src.customer import Customer
from src.account import CurrentAccount, SavingsAccount

@pytest.mark.c
class TestCustomer():
    """ Unit testing for a Customer. """

    @pytest.fixture
    def customer(self) -> Customer:
        """ Generate a default customer """
        customer = Customer('Sterenn Grace')
        return customer

    def test_c_add_new_customer_with_name_sterenn_grace(self, customer: Customer) -> None:
        assert customer.name == 'Sterenn Grace'

    def test_c_add_current_account(self, customer: Customer):
        current_account = CurrentAccount
        assert customer.add_account(current_account)

    def test_c_add_saving_account(self, customer: Customer):
        saving_account = SavingsAccount
        assert customer.add_account(saving_account)