from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import CurrentAccount, SavingsAccount, Account
from src.bank import Bank
from src.customer import Customer
scenarios('./features')

@pytest.fixture
def customer():
    return Customer("Customer",Bank("Caisse d'épargne"), CurrentAccount("Compte courant"), SavingsAccount("Livret A"))