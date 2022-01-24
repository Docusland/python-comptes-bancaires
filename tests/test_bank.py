from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import CurrentBank

scenarios('./features')

@pytest.fixture
def atual_bank():
    return CurrentBank('Default Bank')

@given("Bank is newly created")
def new_bank():
    pass

@given("Bank is removed")
def delete_bank():
    pass

@when(parsers.parse("I want to create a Bank"))
def remove_bank(actual_bank):
    actual_bank = {}

@when(parsers.parse("I want to remove a bank"))
def remove_bank(actual_bank):
    actual_bank = {}