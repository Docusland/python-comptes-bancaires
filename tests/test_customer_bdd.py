from src.bank import Bank
from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import Account
from src.customer import Customer

BANK = Bank("SuperBank")
CUSTOMER = Customer("Client")

scenarios('./features')


@pytest.fixture
def customer():
    return Customer('Default User')


@when(parsers.parse("I create new customer named Customer"))
def new_customer():
    return Customer("Customer")


@given(parsers.parse("I want to open an account"))
def add_customer_to_bank_customer_list(account: Account):
    CUSTOMER.add_account(account)
    assert len(CUSTOMER.accounts) == 1


@given("I want to remove an account from customer's account list")
def remove_account_to_customer_list(account: Account):
    CUSTOMER.remove_account(account)
    assert len(CUSTOMER.accounts) == 0


@when("I check if an account is out of money")
def check_if_account_can_be_remove():
    assert CUSTOMER.can_be_remove() == True
