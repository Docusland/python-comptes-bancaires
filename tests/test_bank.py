from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.bank import Bank

scenarios('./features/test_customer_creation.feature', './features/test_customer_deletion.feature')


@pytest.fixture
def bank():
    return bank('customer')



@given('I am an administrator')
def i_am_an_administrator():
    """I am an administrator."""
    pass


@when('I select a valid name to create my organisation')
def i_select_a_valid_name_to_create_my_organisation(name):
    """I select a valid name to create my organisation."""
    return name


@when('The name selected is exist in the list of bank')
def the_name_selected_is_exist_in_the_list_of_bank(name):
    """The name selected is exist in the list of bank."""
    return name


@when('The name selected is empty or already took')
def the_name_selected_is_void_or_already_took():
    """The name selected is void or already took."""
    pass


@then('I return "the organisation was successfully created"')
def i_return_the_organisation_was_successfully_created(name):
    """I return "the organisation was successfully created"."""
    name = "test"
    return name

@then('I cannot create a bank with an empty name')
def i_cannot_create_bank():
    with pytest.raises(Exception):
        b = Bank('')

@then('I cannot create a bank with a wrong name')
def i_cannot_create_bank():
    with pytest.raises(Exception):
        b = Bank('wrong name')

@then('I return the information about this bank')
def i_return_the_information_about_this_bank():
    """I return the information about this bank."""
    pass


@then('The system raise an exception')
def the_system_raise_an_exception():
    """The system raise an exception."""
    pass

@when('I try to delete the Giangrande Family bank')
def i_try_to_delete_the_giangrande_family_bank():
    """I try to delete the Giangrande Family bank."""
    pass


@when('I\'ve found the name and i delete the bank')
def ive_found_the_name_and_i_delete_the_bank():
    """I've found the name and i delete the bank."""
    pass


@then('I return the bank was deleted')
def i_return_the_bank_was_deleted():
    """I return the bank was deleted."""
    pass
