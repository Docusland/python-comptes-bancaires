from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import Bank

scenarios("./features")

@pytest.fixture
def bank():
    return Bank('Bank01')

@given("I am an Administrator")
def new_bank():
    pass

@when(parsers.parse("I created a Bank named {bank_name}"))
def add_bank(bank):
    bank.add_bank(bank)

@then(parsers.parse("A bank named {bank_name} exist"))
def check_bank(bank):
    assert bank.get_bank == bank

@when(parsers.parse("I check if Bank named {bank_name} already exist"))
def