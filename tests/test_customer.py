from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.customer import Customer as customer

scenarios('./features/test_customer_add.feature')
scenarios('./features/test_customer_delete.feature')
scenarios('./features/test_customer_search.feature')


@pytest.fixture
def customer():
    return customer('customer')


@given('I am an administrator')
def i_am_an_administrator():
    """I am an administrator."""
    pass

@when('The name selected is void or already took')
def the_name_selected_is_void_or_already_took():
    """The name selected is void or already took."""
    pass


def i_return_the_organisation_was_successfully_created(name):
    """I return "the organisation was successfully created"."""
    pass

@then('The system raise an exception')
def the_system_raise_an_exception():
    """The system raise an exception."""
    pass


@when('I try to delete a void or an invalid name of customer')
def i_try_to_delete_a_void_or_an_invalid_name_of_customer(name):
    """I try to delete a void or an invalid name of customer."""
    pass


@when('I\'ve found the name and i delete the customer')
def ive_found_the_name_and_i_delete_the_customer():
    """I've found the name and i delete the customer."""
    pass


@then('I return the customer was deleted')
def i_return_the_customer_was_deleted():
    """I return the customer was deleted."""
    pass



@when('The name selected is exist in the list of customer')
def the_name_selected_is_exist_in_the_list_of_customer():
    """The name selected is exist in the list of customer."""
    pass


@when('The name selected is void or already took')
def the_name_selected_is_void_or_already_took():
    """The name selected is void or already took."""
    pass


@then('I return the information about this customer')
def i_return_the_information_about_this_customer():
    """I return the information about this customer."""
    pass

