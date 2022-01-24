from unittest import TestCase
import pytest

from src.banks import Bank


class TestBank:

    @pytest.fixture
    def default_bank(self):
        return Bank('LaBanque')

    def test_create_bank(self, default_bank):
        assert default_bank.name == 'LaBanque'

    def test_create_customer(self, default_bank):
        self.premier_client = Bank.new_customer('LeClient')
        assert self.premier_client.name == 'LeClient'

    # def test_create_two_customers(self, default_bank):
    #     self.premier_client = Bank.new_customer('LeClient')
    #     self.second_client = Bank.new_customer('LeBron')
    #     assert self.premier_client.name == 'LeClient'
    #     assert self.second_client.name == 'LeBron'
