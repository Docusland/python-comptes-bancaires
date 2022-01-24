import random
from unittest import TestCase
import pytest

from src.banks import Bank
from src.customers import Customer


class TestBank:

    @pytest.fixture
    def default_bank(self):
        return Bank('LaBanque')

    def test_create_bank(self, default_bank):
        assert default_bank.name == 'LaBanque'

    def test_create_customer(self, default_bank):
        default_bank.new_customer('LeClient')
        assert default_bank.customers[0].name == 'LeClient'

    def test_create_two_customers(self, default_bank):
        i = random.randint(1, 20)
        for j in range(i):
            default_bank.new_customer('LeClient')
        assert len(default_bank.customers) == i

    def test_delete_one_customer(self, default_bank):
        i = random.randint(1, 20)
        for j in range(i):
            default_bank.new_customer('LeClient')
        k = random.randint(0, i)
        for j in range(k):
            default_bank.delete_customer(0)
        assert len(default_bank.customers) == (i - k)