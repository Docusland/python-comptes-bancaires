from unittest import TestCase
from src.bank import listBank


class TestBank(TestCase):

    def list_customer(self):
        #a bank with two customer
        self.nb = listBank("La Boiserie")
        self.listCustomer = ["Steve", "Herobrine"]
        assert self.listCustomer == ["Steve", "Herobrine"]

    def check_account(self):

        # an account with a customer named Steve with an account_balance at 0
        assert self.listCustomer == ["Steve"]
        assert self.cc.account_balance == 0