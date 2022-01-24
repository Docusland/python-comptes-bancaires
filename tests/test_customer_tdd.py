from src.customer import Customer
from unittest import TestCase


class TestCustomer(TestCase):

    def setUp(self):
        self.customer = Customer('Sterenn Grace')

    def test_nothing(self):
        pass
