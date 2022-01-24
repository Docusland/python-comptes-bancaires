from pytest_bdd import given, when, then, parsers, scenarios, scenario
from src.bank import Bank

scenarios('./features/test_bank_creation.feature')


@given(parsers.parse("I am an Admin"))
def create_admin():
    pass


@when(parsers.parse("I create a new bank named {name}"), target_fixture="bank")
def bank(name):
    return Bank(name=name)


@then(parsers.parse("a Bank named {name} exists"))
def check_bank_name(bank, name):
    assert type(bank) == Bank
    assert bank.name == name


@then(parsers.parse("it has {number:d} Customers"))
def check_bank_customers(bank, number):
    assert len(bank.customers) == 0
