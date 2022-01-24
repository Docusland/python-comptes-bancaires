from src.account import Account, CurrentAccount
from unittest import TestCase

from src.customer import Customer


class TestCC(TestCase):

    def setUp(self):
        self.cc = Customer('KFZJ JKFEJK')

    def test_cc_unauthorized_withdrawal_generates_exception(self):

        # act
        self.cc.money_transfer(150)
        with self.assertRaises(Exception):
            # assert
            self.cc.money_withdraw(200)


    def test_new_account_has_no_money(self):
        assert self.cc.account_balance == 0
