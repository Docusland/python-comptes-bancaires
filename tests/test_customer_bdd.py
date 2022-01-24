from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.customer import Customer


@pytest.fixture
def customer():
    return Customer("Customer01")


@given("I am an Employee of the Bank named {bank_name}")
def new_customer():
    pass


@when(parsers.parse("I create a Customer named {customer_name}"))
def add_customer(customer_name, bank):
    customer = Customer(customer_name)
    return customer


@when(parsers.parse("I edit a customer named {customer_name}"))
def update_a_customer(customer_name, new_customer_name, bank):
    customer = Customer(customer_name)
    customer.name = new_customer_name
    return customer


@when(parsers.parse("I delete a customer named CustomerA"))
def delete_a_customer(customer_name, bank):


@then(parsers.parse("A Customer named {customer_name} exist"))
def check_customer(customer_name, bank):
    assert customer.check_customer == customer_name
