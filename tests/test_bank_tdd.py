"""
    Unit testing for Bank.
"""

from random import randrange
import pytest
from src.account import *
from src.bank import *
from src.customer import *


class TestBank():
    """ Unit testing for a Bank. """

    positive_account: int = 42

    @pytest.fixture
    def bank(self) -> Bank:
        return Bank("TheBank", [
            Customer("Bob", "TheBank", [self.first_account])
        ])

    @pytest.fixture
    def first_account(self) -> CurrentAccount:
        """return an empty current account"""
        return CurrentAccount("Bob")

    @pytest.fixture
    def second_account(self) -> CurrentAccount:
        """return an empty savings account"""
        return CurrentAccount("toto")

    def test_inner_transfer(self,
                            first_account: CurrentAccount,
                            second_account: CurrentAccount,
                            bank: Bank
                            ):
        first_account.account_balance = self.positive_account
        bank.inner_transfer(first_account, second_account, self.positive_account)
        assert first_account.account_balance == 0
        assert second_account.account_balance == self.positive_account

    def test_find_customer_by_account_uuid(self,
                                           bank: Bank,
                                           first_account: CurrentAccount
                                           ):
        assert first_account.owner_name == bank.find_customer_by_account_uuid(first_account.numero_compte)
