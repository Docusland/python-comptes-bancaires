import unittest
import pytest
from src.Customer import Customer


@pytest.mark.customer
class MyTestCase(unittest.TestCase):

    SUPPOSED_NAME = 'astol'

    @pytest.fixture
    def default_customer(self) -> Customer:
        """ default customer account """
        return Customer(customer_name=self.SUPPOSED_NAME)

    def test_customer_bank_name(self):
        """ TODO test customer bank name"""
        pass

    def test_customer_name(self, default_customer: Customer):
        """ test if the saving account match with the username given """
        self.assertEqual(self.SUPPOSED_NAME, default_customer.get_name())

    def test_customer_ca_name(self, default_customer: Customer):
        """ test if the saving account match with the username given """
        self.assertEqual(default_customer.get_name(), default_customer.get_ca_name())

    def test_customer_sc_name(self, default_customer: Customer):
        """ test if the saving account match with the username given """
        self.assertEqual(default_customer.get_name(), default_customer.get_sc_name())

    def test_customer_transfer(self, default_customer: Customer):
        """ TODO test the transfer between two account for customer"""
        pass

if __name__ == '__main__':
    unittest.main()
