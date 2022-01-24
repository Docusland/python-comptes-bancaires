"""
    Unit testing for Customer.
"""
import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    """ Unit testing for Customers. """

    def test_i_create_nw_account(self):
        customer_name = 'nom de mon client'
        customer = Customer(customer_name)
        assert customer != None
        assert customer._name == customer_name