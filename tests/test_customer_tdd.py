"""
    Unit testing for Customer.
"""

import pytest
from src.account import *
from src.bank import *
from src.customer import *


class TestCustomer:
    """ Unit testing for a Customer. """
    positive_amount = 1

    @pytest.fixture
    def bank(self) -> Bank:
        return Bank("TheBank", [])

    @pytest.fixture
    def customer(self, bank: Bank) -> Customer:
        return Customer("Bob", bank)

    @pytest.fixture
    def customer_with_accounts(self, customer: Customer) -> Customer:
        customer.accounts.append(CurrentAccount(customer.name))
        customer.accounts.append(SavingsAccount(customer.name))
        return customer

    def test_customer(self):
        assert Customer is not None

    def test_add_accounts(self, customer: Customer):
        """test addition of accounts"""
        customer.add_accounts([
            CurrentAccount(customer.name),
            SavingsAccount(customer.name)]
        )
        assert len(customer.accounts) == 2

    def test_remove_account(self, customer_with_accounts: Customer):
        """test remove an account from a customer with multiple accounts"""
        customer_with_accounts.delete_account(customer_with_accounts.accounts[0])
        assert len(customer_with_accounts.accounts) == 1

    def test_can_be_removed(self, customer, customer_with_accounts):
        """assert a customer with a sold = 0 can be removed"""
        assert customer.can_be_removed()
        assert customer_with_accounts.can_be_removed()

        """ assert if remove a none-empty account customer is impossible"""
        customer_with_accounts.accounts[0].money_transfer(self.positive_amount)
        assert not customer_with_accounts.can_be_removed()
