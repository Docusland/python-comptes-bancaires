from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import Bank

scenarios("./v2")


@pytest.fixture
def default_bank():
    return None


@given(parsers.parse("Im an employee from the bank named {bank_name}"), target_fixture="default_bank")
def background(bank_name):
    return Bank(bank_name)


@then("it has no customer")
def bank_has_no_customers(default_bank):
    assert default_bank.customers_count == 0


@given(parsers.parse("I want to add a new customer named {customer_name}"), target_fixture="default_bank")
def create_new_bank(default_bank, customer_name):
    default_bank.add_new_customer(customer_name)
    return default_bank


@then(parsers.parse("there is now one customer named {customer_name}"))
def add_new_customer(default_bank, customer_name):
    find = True if default_bank.customers_dict[customer_name] == 0 else False
    assert default_bank.customers_count == 1
    assert find == True
