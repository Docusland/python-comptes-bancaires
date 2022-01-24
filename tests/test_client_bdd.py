"""from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest

from src.client import Client

scenarios('./features')


@pytest.fixture
def client():
    return Client('Default User')

@given("Customer is newly created")
def new_customer():
    #pass

@when(parsers.parse("I add {TOTO}"))
def add_customer_name(customer_name):
    client.name = customer_name
    return client()

@then("Customer has been created with client_name")
def check_client_name(customer_name, client.name)
    assert client.name == customer_name"""