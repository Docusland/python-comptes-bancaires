from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.customer import Customer as customer, Customer

scenarios('./features/test_customer_search.feature')

@pytest.fixture
def customer():
    return Customer('Customer')

@given("I know the CE uuid of my customer")
def search_customer_by_savings_account_uuid(customer):
    return customer.name

@given("I know the CC uuid of my customer")
def search_customer_by_current_account_uuid(customer):
    return customer.name

@given("I am an Admin")
def search_customer_by_name():
    return customer.name
