"""
    Unit testing for Customer.
"""
import pytest

from src.customer import Customer

class TestCustomer():
    """ Unit testing for Customers. """

    SUPPOSED_CUSTOMER_ACCOUNT = 'Compte'
    SUPPOSED_CUSTOMER_NAME = 'Henri'

    @pytest.fixture
    def default_customer(self) -> Customer:
        """ default customer object """
        return Customer(self.SUPPOSED_CUSTOMER_NAME, self.SUPPOSED_CUSTOMER_ACCOUNT)

    @pytest.fixture
    def default_account(self) -> Customer:
        """ default account object """
        return Customer(self.SUPPOSED_CUSTOMER_NAME, self.SUPPOSED_CUSTOMER_ACCOUNT)

    def test_i_create_nw_account(self, default_customer: Customer):
        assert default_customer.get_name() == self.SUPPOSED_CUSTOMER_NAME

    def test_i_create_new_account(self, default_account: Customer):
        assert default_account.get_new_account() == self.SUPPOSED_CUSTOMER_ACCOUNT

