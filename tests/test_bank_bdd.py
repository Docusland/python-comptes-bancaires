from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import Bank

scenarios('./features')


@given("I am an Administrator")
def is_admin():
    pass


@when(parsers.parse("I create a new bank named {bank_name:s})"))
def create_bank(bank_name):
    bank = Bank(bank_name)


@then("a bank named {bank_name:s} exists")
def step_impl():
    assert bank.name == bank_name


@given("it has no customers")
def step_impl():
    assert bank.customers.len == 0


@when("I create a new bank with no name")
def step_impl():
    Bank()


@then("a bank is not created")
def step_impl():
    raise NotImplementedError(u'STEP: Then a bank is not created')
