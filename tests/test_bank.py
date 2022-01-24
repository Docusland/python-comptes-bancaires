"""
    Unit testing for a Bank.
"""
import pytest
from src.bank import Bank
from src.customer import Customer


@pytest.mark.b
class TestBank():

    @pytest.fixture
    def bank(self) -> Bank:
        """ Generate a default customer """
        bank = Bank('ING')
        return bank

    @pytest.fixture
    def customer(self) -> Customer:
        """ Generate a default customer """
        customer = Customer('Sterenn Grace')
        return customer

    def test_b_add_new_bank_with_ing_name(self, bank: Bank) -> None:
        assert bank.name == 'ING'

    def test_b_add_customer_in_ing_bank(self, bank: Bank, customer: Customer) -> None:
        assert bank.add_customer(customer)

    def test_b_remove_customer_in_ing_bank(self, bank: Bank, customer: Customer) -> None:
        bank.add_customer(customer)
        assert bank.remove_customer(customer)

    def test_b_remove_not_existing_customer_in_ing_bank(self, bank: Bank, customer: Customer) -> None:
        with pytest.raises(Exception) as excinfo:
            bank.remove_customer(customer)
        assert str(customer.name)+' is not a customer of the bank' in str(excinfo.value)
