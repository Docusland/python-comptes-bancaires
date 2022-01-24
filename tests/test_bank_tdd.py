from src.bank import Bank
from unittest import TestCase


class TestBank(TestCase):

    def setUp(self):
        self.bank = Bank('CA')

    def test_nothing(self):
        pass
