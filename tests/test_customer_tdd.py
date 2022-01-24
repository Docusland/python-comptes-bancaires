"""
    Unit testing for Client.
"""
import pytest
from src.customer import Customer
from src.account import SavingsAccount
from src.bank import Bank


@pytest.mark.cc
class TestCustomer:
    """ Unit testing for a Client."""

    @pytest.fixture
    def customer_account(self) -> Customer:
        """Generate a default client"""
        return Customer("Jean")

    def test_customer_creation(self, customer_account: Customer):
        assert customer_account.name == "Jean"
        """assert customer_account.bank.name == "Test"""

    def test_customer_add_account(self, customer_account: Customer):
        saving = SavingsAccount("Jean")
        customer_account.add_account(saving)
        assert len(customer_account.get_accounts()) == 1

    def test_customer_remove_account(self, customer_account: Customer):
        saving = SavingsAccount("Jean")
        customer_account.add_account(saving)
        customer_account.remove_account(saving)
        assert len(customer_account.get_accounts()) == 0

    def test_customer_can_be_removed(self,customer_account: Customer):
        assert customer_account.can_be_removed() == True

    def test_customer_can_not_be_removed(self, customer_account: Customer):
        saving = SavingsAccount("Jean")
        customer_account.add_account(saving)
        assert customer_account.can_be_removed() == False

    def test_customer_add_bank(self, customer_account: Customer):
        bank = Bank("Test")
        customer_account.add_bank(bank)
        assert customer_account.get_bank() == bank
