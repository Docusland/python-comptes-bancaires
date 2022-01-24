from src.customer import Customer
from src.bank import Bank
from src.account import CurrentAccount
from src.account import SavingsAccount
from src.account import Account
import pytest


@pytest.mark.customer
class TestCustomer:

    def setUp(self) -> None:
        self.foreignAccount = CurrentAccount("ForeignAccount")

        self.bank = Bank("SuperBank")
        self.account_list = []

        self.customer = Customer("customer", self.bank, self.account_list)

    # Create new customer
    def test_create_new_customer(self) -> Customer:
        assert self.customer

    def test_amount_zero(self):
        assert self.account[0].account_balance == 0

    def test_add_account_to_customer(self, account: Account):
        self.customer.add_account(account)
        assert len(self.account_list) == 1

    def test_remove_account_to_customer(self, account: Account):
        self.customer.add_account(account)
        assert len(self.customer.accounts) == 1

        self.customer.remove_account(account)
        assert len(self.customer.accounts) == 0
