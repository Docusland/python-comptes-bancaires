import pytest

from src.account import CurrentAccount, SavingsAccount
from src.customer import Customer


@pytest.mark.v2
class TestCustomer:
    @pytest.fixture
    def customer(self) -> Customer:
        return Customer("jean", [CurrentAccount("jean"), SavingsAccount("jean")])

    def test_customer_name(self, customer):
        assert customer.name == "jean"

    def test_account(self, customer):
        assert customer.accounts
