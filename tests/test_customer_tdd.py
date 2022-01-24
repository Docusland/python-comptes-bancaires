from src.customer import Customer
from src.bank import Bank
from src.account import Account, CurrentAccount, SavingsAccount
from unittest import TestCase


class TestCustomer(TestCase):

    def setUp(self):
        self.customer = Customer('Sterenn Grace', Bank('CA'), CurrentAccount('Sterenn Grace'), SavingsAccount('Sterenn Grace'))

    def test_nothing(self):
        pass
