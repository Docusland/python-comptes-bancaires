from unittest import TestCase
from pytest_bdd import scenario, given, when, then, parsers, scenarios

from src.customer import Customer

scenario('./features/test_customer_creation.feature')


class TestCustomer(TestCase):
    def setUp(self):
        self.customer = Customer("John Doe", "Goodbank")

    def test_create_customer(self):
        assert self.customer.name == "John Doe"
