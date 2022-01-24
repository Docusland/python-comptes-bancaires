"""
    Unit testing for Bank.
"""
import pytest
from src.bank import Bank
from src.account import SavingsAccount
from src.customer import Customer


@pytest.mark.cc
class TestBank:
    """ Unit testing for a Bank."""

    @pytest.fixture
    def bank(self) -> Bank:
        """Generate a default bank"""
        return Bank("Test")

    def test_bank_creation(self, bank: Bank):
        assert bank.name == "Test"

    def test_bank_add_customer(self, bank: Bank):
        customer = Customer("Test")
        bank.add_customer(customer)
        assert bank.customers[0].name == "Test"

    def test_bank_remove_customer(self, bank: Bank):
        customer = Customer("Test")
        customer2 = Customer("Test2")
        bank.add_customer(customer)
        bank.add_customer(customer2)
        bank.remove_customer(customer)
        assert bank.customers[0] == customer2

    def test_bank_has_customer(self, bank: Bank):
        customer = Customer("Jean")
        bank.add_customer(customer)
        assert bank.has_customers() == True

    def test_bank_has_no_customers(self, bank: Bank):
        assert bank.has_customers() == False

    def test_find_customer_by_account_uuid(self, bank: Bank):
        test = Customer("Test")
        test2 = Customer("Test2")
        test3 = Customer("Test3")
        saving = SavingsAccount("Test")
        saving2 = SavingsAccount("Test")
        saving3 = SavingsAccount("Test")
        saving4 = SavingsAccount("Test2")
        saving5 = SavingsAccount("Test2")
        saving6 = SavingsAccount("Test3")
        test.add_account(saving)
        test.add_account(saving2)
        test.add_account(saving3)
        test2.add_account(saving4)
        test2.add_account(saving5)
        test3.add_account(saving6)
        bank.add_customer(test)
        bank.add_customer(test2)
        bank.add_customer(test3)
        uuid_to_search = saving5.numero_compte
        assert bank.find_customer_by_account_uuid(uuid_to_search) == test2

    def test_find_customer_by_customer_name(self, bank: Bank):
        test = Customer("Test")
        test2 = Customer("Test2")
        test3 = Customer("Test3")
        bank.add_customer(test)
        bank.add_customer(test2)
        bank.add_customer(test3)
        assert bank.find_customer_by_customer_name("Test3") == test3

    def test_inner_transfer(self, bank: Bank):
        test = Customer("Test")
        saving = SavingsAccount("Test")
        test.add_account(saving)
        bank.add_customer(test)
        saving.money_transfer(100)
        test2 = Customer("Test2")
        saving2 = SavingsAccount("Test2")
        test2.add_account(saving2)
        bank.add_customer(test2)
        bank.inner_transfer(100, saving, saving2)
        assert saving.account_balance == 0
        assert saving2.account_balance == 100

    def test_inner_transfer_not_enough_funds(self, bank: Bank):
        test = Customer("Test")
        saving = SavingsAccount("Test")
        test.add_account(saving)
        bank.add_customer(test)
        saving.money_transfer(100)
        test2 = Customer("Test2")
        saving2 = SavingsAccount("Test2")
        test2.add_account(saving2)
        bank.add_customer(test2)
        saving.money_transfer(100)
        assert bank.inner_transfer(100, saving2, saving) == False

    def test_inner_transfer_to_another_bank(self, bank: Bank):
        test = Customer("Test")
        saving = SavingsAccount("Test")
        test.add_account(saving)
        bank.add_customer(test)
        saving.money_transfer(100)
        second_bank = Bank("2")
        test2 = Customer("Test2")
        saving2 = SavingsAccount("Test2")
        test2.add_account(saving2)
        second_bank.add_customer(test2)
        assert bank.inner_transfer(100, saving, saving2) == False