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

    def test_add_account_gives_one_more_account(self, customer):
        size_before = len(customer.accounts)
        customer.add_account(CurrentAccount("joe"))
        assert size_before == len(customer.accounts)-1

    def test_add_account_give_account_with_the_good_name(self, customer):
        customer.add_account(CurrentAccount("joe"))
        assert customer.accounts[-1].customer == "joe"

    def test_remove_account_delete_one_account(self, customer):
        customer.add_account(CurrentAccount("joe"))
        size_before = len(customer.accounts)
        customer.remove_account(CurrentAccount("joe"))
        assert size_before == len(customer.accounts) + 1

    def test_can_be_removed_with_positive_account_balance(self, customer):
        customer.accounts[0].money_transfer(10)
        assert customer.can_be_removed(customer.accounts[0]) == False

    def test_can_be_removed_with_null_account_balance(self, customer):
        assert customer.can_be_removed(customer.accounts[0]) == True
