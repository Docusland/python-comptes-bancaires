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
        """
        If customer name is the same
        """
        assert customer.name == "Customer"

    def test_add_savings_account_of_customer(self, customer:Customer):
        """
        If can add a savings account for customer
        """
        account = SavingsAccount("Livret Jeune")
        customer.add_account(account)
        assert customer.listAccount[len(customer.listAccount) - 1] == account

    def test_add_current_account_for_customer(self, customer:Customer):
        """
        If can add a current account for customer
        """
        account = CurrentAccount("Compte chèque")
        customer.add_account(account)
        assert customer.listAccount[len(customer.listAccount) - 1] == account

    def test_remove_account_not_exist_in_list_account_for_customer(self, customer:Customer):
        """
        If can remove an account who not exist in listAccount of customer
        """
        account = SavingsAccount("PEL")
        assert customer.remove_account(account) == False

    def test_remove_account_with_money_for_customer(self, customer:Customer):
        """
        If can remove an account with money
        """
        account = SavingsAccount("PEL")
        account.money_transfer(100)
        customer.add_account(account)
        assert customer.remove_account(account) == False

    def test_remove_account_with_no_money_for_customer(self, customer:Customer):
        """
        If can remove an account with no money
        """
        account = SavingsAccount("PEL")
        customer.add_account(account)
        assert customer.remove_account(account) == True
