from src.account import Account, CurrentAccount
from src.customer import Customer
from src.bank import Bank
from unittest import TestCase


class TestCC(TestCase):

    def setUp(self):
        self.cc = CurrentAccount(Customer('Customer1', Bank('Bank1')))

    def test_cc_unauthorized_withdrawal_generates_exception(self):
        # act
        self.cc.money_transfer(150)
        with self.assertRaises(Exception):
            # assert
            self.cc.money_withdraw(200)

    def test_new_account_has_no_money(self):
        assert self.cc.account_balance == 0
