from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import Bank

scenarios('./features/test_bank_create.feature')

@pytest.fixture
def bank():
    return Bank('Default Bank Name')

@given("New Bank created")
def new_bank():
    pass

@when(parsers.parse("I add new Bank called {new_Bank_name}"), target_fixture="bank")
def new_bank(bank,new_Bank_name):
    return Bank(new_Bank_name)

@then(parsers.parse("Bank called {new_Bank_name} has been created."))

def check_name_bank(bank, new_Bank_name):
    assert getattr(bank, __name) == new_Bank_name




@given(parsers.parse("New {bank_name} Bank created"))
def cmb_bank(bank, bank_name):
    return Bank(bank_name)

@when(parsers.parse("I check Customers in {bank_name} Bank"), target_fixture="bank")
def check_bank_customers(bank_name):
    bank_customers = getattr(bank, "_customers")
    return len(bank_customers)

@then(parsers.parse("{bank_name} Bank has {customers_number} customers"))
def check_bank_has_not_customers(bank_name, customers_number):
    assert check_bank_customers(cmb_bank, bank_name) == customers_number

