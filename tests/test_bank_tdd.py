"""
    Unit testing for Bank
"""
from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import CurrentAccount, SavingsAccount
from src.bank import Bank
from src.customer import Customer
scenarios('./features')
@pytest.mark.cc
class TestBank():
    @pytest.fixture
    def bank(self):
        """ Generate a default Bank named CIC"""
        return Bank("CIC")

    @pytest.fixture
    def customer(self):
        """Generate a default Customer named Client1"""
        return Customer("Client1", [CurrentAccount("Compte courant"), SavingsAccount("Livret A")])

    def test_bank_name(self, bank:Bank) -> None:
        """
        If bank name is equal CIC
        """
        assert bank.name == "CIC"

    def test_add_customer_in_bank(self, bank:Bank, customer:Customer) -> None:
        """
        If customer add in list of customers in bank is customer
        """
        bank.add_customer(customer)
        assert bank.customers[0] == customer

    def test_customer_in_bank(self,bank: Bank, customer:Customer) -> None:
        """
        If bank have one customer after add customer in customers list of bank
        """
        bank.add_customer(customer)
        assert len(bank.customers) > 0

    def test_remove_customer_in_bank(self, bank:Bank, customer:Customer) ->None:
        """
        If can remove customer in customers list of bank
        """
        bank.add_customer(customer)
        bank.remove_customer(customer)
        assert len(bank.customers) == 0

    def test_find_customer_with_customer_name(self, bank:Bank, customer:Customer):
        """
        If exist customer in customers list of bank with customer name
        """
        bank.add_customer(customer)
        assert bank.find_customer_by_customer_name("Client1") == customer

    def test_find_customer_with_customer_uuid(self, bank:Bank, customer:Customer):
        """
        If exist customer in customers list of bank with uuid
        """
        uuid_customer = customer.listAccount[0].numero_compte
        bank.add_customer(customer)
        assert bank.find_customer_by_account_uuid(uuid_customer) == customer

    def test_transfert_with_from_account_who_have_no_money_to_account_of_same_customer_in_same_bank(self, bank:Bank, customer:Customer):
        """
        If bank can transfert money from account who have no money to account of same customer
        """
        assert bank.inner_transfert(customer.listAccount[0], customer.listAccount[1],100) == False

    def test_transfert_with_from_account_to_account_of_same_customer_in_same_bank(self, bank:Bank, customer:Customer):
        """
        If bank can transfert money from account to an account of same customer
        """
        customer.listAccount[0].money_transfer(100)
        assert bank.inner_transfert(customer.listAccount[0], customer.listAccount[1],50) == True

    def test_transfert_with_from_account_to_account_of_customers_in_same_bank(self, bank: Bank, customer: Customer):
        """
        If bank can transfert money from account to an account
        """
        customer_two = Customer("Client2", [CurrentAccount("Compte courant"), SavingsAccount("Livret A")])
        customer_two.listAccount[0].money_transfer(100)
        bank.add_customer(customer_two)
        assert bank.inner_transfert(customer_two.listAccount[0], customer.listAccount[1], 50) == True