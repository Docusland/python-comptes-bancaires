from src.bank import Bank
from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import Account
from src.customer import Customer

BANK = Bank("SuperBank")
CUSTOMER = Customer("Client")

scenarios('./features')


@pytest.fixture
def bank():
    return Bank("Banque")


@
