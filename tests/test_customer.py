from src.customers import Customer
from unittest import TestCase


class TestCustomer(TestCase):

    def setUp(self):
        self.customer = Customer('Erwann Duclos')


    # def test_new_customer_has_no_money(self):
    #     assert self.cc.account_balance == 0
    #
    # def test_inner_transfer(self):
    #
    #     # act
    #     self.cc.money_transfer(150)
    #     with self.assertRaises(Exception):
    #         # assert
    #         self.cc.money_withdraw(200)



