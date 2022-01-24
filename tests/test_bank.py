from src.customer import Customer
from src.bank import Bank

import pytest


@pytest.mark.bank
class TestBank():

    def setUp(self) -> None:
        self.bank = Bank("SuperBank")
        self.customer = Customer("Customer")

    # Create new customer
    def test_create_new_bank(self) -> Bank:
        assert self.bank

    def test_add_customer(self):
        self.bank.add_customer(self.customer)
        assert len(self.bank.customers) == 1

    def test_find_customer_by_account_uuid(self, customer_uuid: str):
        customer_find = self.bank.find_customer_by_account_uuid(customer_uuid)
        assert customer_find == self.customer

    def test_find_customer_by_customer_name(self, customer_name: str):
        customer_find = self.bank.find_customer_by_account_uuid(customer_name)
        assert customer_find == self.customer
