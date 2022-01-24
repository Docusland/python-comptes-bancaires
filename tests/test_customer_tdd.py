import pytest
import uuid

from src.customer import Customer
from src.bank import Bank
from src.account import Account


class TestCustomer():

    @pytest.fixture
    def default_customer(self):
        return Customer('Brice')

    @pytest.fixture
    def default_account(self):
        return Account()

    def test_add_account_to_customer(self, default_customer, default_account):
        test_account_number = uuid.uuid4()
        default_customer.add_account(test_account_number)
        assert default_customer.accounts == test_account_number
