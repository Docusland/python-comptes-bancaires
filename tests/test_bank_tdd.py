import pytest

from src.bank import Bank
from src.customer import Customer

class TestBank:

    @pytest.fixture
    def default_bank(self):
        return Bank('Banque', [])

    @pytest.fixture
    def first_customer(self):
        return Customer('John')

    @pytest.fixture
    def second_customer(self):
        return Customer('Jack')

    def test_create_bank(self, default_bank):
        assert default_bank.name == 'Banque'

    def test_add_one_customer_to_bank(self, default_bank, first_customer):
        default_bank.add_customer(first_customer)
        assert default_bank.customers == ['John']

    def test_add_two_customers_to_bank(self, default_bank, first_customer, second_customer):
        default_bank.add_customer(first_customer)
        default_bank.add_customer(second_customer)
        assert default_bank.customers == ['John', 'Jack']

    # def test_remove_customer_to_bank(self, default_bank, first_customer):

