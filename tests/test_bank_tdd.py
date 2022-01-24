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
        assert bank.name == "CIC"

    def test_add_customer_in_bank(self, bank:Bank, customer:Customer) -> None:
        bank.add_customer(customer)
        assert bank.customers[0] == customer

    def test_customer_in_bank(self,bank: Bank, customer:Customer) -> None:
        bank.add_customer(customer)
        assert len(bank.customers) > 0

