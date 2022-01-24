from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import CurrentAccount

scenarios('./features')

@pytest.fixture
def customer():
    return Customer("Customer")