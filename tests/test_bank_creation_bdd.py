from pytest_bdd import given, when, then, parsers, scenarios

from src.bank import Bank

scenarios('./features/test_bank_creation.feature')

@given("I am an Admin")
def new_admin():
    pass

@when(parsers.parse("I create a new bank named {bank_name}"),target_fixture="squirrelBank")
def i_create_a_bank(bank_name):
    return Bank(bank_name)

@then(parsers.parse("A bank named {bank_name} exists"))
def bank_name_is_correct(bank_name, squirrelBank):
    assert bank_name == squirrelBank.name

@then("It has 0 Customer")
def bank_without_customer(squirrelBank):
    return squirrelBank.customers
