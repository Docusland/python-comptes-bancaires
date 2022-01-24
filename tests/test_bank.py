from unittest import TestCase
import pytest

from src.bank import Bank
from src.customer import Customer


class TestBank:

    @pytest.fixture
    def default_bank(self):
        return Bank('TestBank')

    def test_create_bank(self, default_bank):
        assert default_bank.name == 'TestBank'

    def test_create_customer(self, default_bank):
        default_bank.new_customer('Theo')
        assert default_bank.customers[0].name == 'Theo'

    def test_create_two_customers(self, default_bank):
        default_bank.new_customer('Theo')
        default_bank.new_customer('Bernard')
        assert len(default_bank.customers) == 2

    def test_delete_one_customer(self, default_bank):
        default_bank.new_customer('Theo')
        default_bank.new_customer('Bernard')
        default_bank.delete_customer(0)
        assert len(default_bank.customers) != 2


