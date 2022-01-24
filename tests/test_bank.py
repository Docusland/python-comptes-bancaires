from banks import Bank
from unittest import TestCase


class TestBank(TestCase):

    def setUp(self):
        self.bank = Bank('LaBanque')