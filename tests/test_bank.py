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

    # def test_create_two_customers(self, default_bank):
    #     self.premier_client = Bank.new_customer('LeClient')
    #     self.second_client = Bank.new_customer('LeBron')
    #     assert self.premier_client.name == 'LeClient'
    #     assert self.second_client.name == 'LeBron'
