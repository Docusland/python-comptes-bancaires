from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import Bank

scenario('./features/test_bank_creation.feature')


@given("I am an administrator")
def administration():
    return Bank()


@when(parsers.parse("I create a new bank named {name}"))
def new_bank(administration, name):
    administration.bank = name


@then(parsers.parse("A bank named {name} exists"))
def check_bank(administration, name):
    assert administration.bank == name


@then(parsers.parse("It has {customer:d} customer"))
def check_bank(administration, customer):
    if administration.customers:
        customer = 0

    return customer
