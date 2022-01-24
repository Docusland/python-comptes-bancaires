from pytest_bdd import given, when, then, parsers, scenarios

scenarios('./features/test_bank_deletion.feature')

@given("A bank already exist")
def bank():
    pass

@when(parsers.parse("I select a bank {bank_name}"),target_fixture="squirrelBank")
def i_delete_a_bank(bank_name):
    return bank_name

@then(parsers.parse("{bank_name} is delete"))
def bank_name_is_delete(bank_name, squirrelBank):
    return None


