from src.customer import Customer
from src.bank import Bank
from src.account import Account, CurrentAccount, SavingsAccount
from unittest import TestCase


class TestCustomer(TestCase):

    def setUp(self):
        self.customer = Customer('Sterenn Grace',
                                 Bank('CA'),
                                 CurrentAccount(max_limit=1000, agios=0.1),
                                 SavingsAccount(interests=0.05))

    def test_nothing(self):
        pass
