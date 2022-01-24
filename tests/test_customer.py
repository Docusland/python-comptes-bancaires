from src.customers import Customer
from unittest import TestCase

import pytest


class TestCustomer:

    @pytest.fixture
    def default_customer(self):
        return Customer('LeClient', 'LaBanque')

    def test_create_bank(self, default_customer):
        assert default_customer.name == 'LeClient'

    def test_create_account(self, default_customer):
        default_customer.create_account('Compte Courant')
        assert default_customer.accounts[0].owner_name == 'Compte Courant'






