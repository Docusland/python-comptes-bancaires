"""
    Unit testing for Customer
"""
import pytest

from src.account import CurrentAccount, SavingsAccount
from src.bank import Bank
from src.customer import Customer


@pytest.mark.c
class TestCustomer():
    @pytest.fixture
    def customer(self, currentAccount:CurrentAccount, savingsAccount:SavingsAccount):
        """ Generate a default Customer """
        return Customer("Customer", [currentAccount, savingsAccount])

    @pytest.fixture
    def currentAccount(self):
        """Generate a default currentAccount"""
        return CurrentAccount("Compte courant",max_limit=1000, agios=0.1)

    @pytest.fixture
    def savingsAccount(self):
        """Generate a default savingsAccount"""
        return SavingsAccount("Livret A")

    def test_customer_have_a_current_account(self, customer:Customer):
        """
        If customer have a current accounf
        """
        assert type(customer.listAccount[0]) == CurrentAccount

    def test_customer_have_a_savings_account(self, customer:Customer):
        """
        If customer have a savings accounf
        """
        assert type(customer.listAccount[1]) == SavingsAccount

    def test_customer_name(self, customer:Customer):
        assert customer.name == "Customer"
