from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import CurrentAccount, SavingsAccount
from src.bank import Bank
from src.customer import Customer
scenarios('./features')

@pytest.fixture
def customer():
    return Customer("Customer", bank(), currentAccount(), savingsAccount())

def bank():
    return Bank("Caisse d'épargne")

def currentAccount():
    return CurrentAccount("Compte courant")

def savingsAccount():
    return SavingsAccount("Livret A")