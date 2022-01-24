from src.customer import Customer
from src.bank import Bank
from src.account import CurrentAccount
from src.account import SavingsAccount
import pytest


@pytest.mark.bank
class TestBank():

    def setUp(self) -> None:
        self.bank = Bank("SuperBank", customerList=None)
        self.customer = Customer("Customer")

    # Create new customer
    def test_create_new_bank(self) -> Bank:
        assert self.bank

    def test_add_customer(self):
        self.bank.add_customer(self.customer)
        assert len(self.bank.customers) == 1
