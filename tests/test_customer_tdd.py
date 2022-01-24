import pytest

from src.customer import Customer
from src.bank import Bank
from src.account import Account

class TestCustomer():

    @pytest.fixture
    def default_customer(self):
        return Customer('Brice')

    def test_add_account(self, default_customer):
        assert default_customer.name == 'Brice'