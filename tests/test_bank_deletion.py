from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import Bank

scenario('./features/test_bank_deletion.feature')


@given("I am an administrator")
def administration():
    return Bank()


@given(parsers.parse("A bank named {name} exists"))
def check_bank(administration, name):
    administration.bank = name


@when(parsers.parse("I delete a bank named {name}"))
def new_bank(administration, name):
    administration.pop()


@then(parsers.parse("A bank named {name} doesn't exists"))
def check_bank(administration, name):
    assert administration.bank != name
