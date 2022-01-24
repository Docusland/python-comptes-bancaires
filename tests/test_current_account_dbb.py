from pytest_bdd import scenario, given, when, then


@when("I create a current account to customer Jean-Michel")
def step_impl():
    raise NotImplementedError(u'STEP: When I create a current account to customer Jean-Michel')


@then("a current account is created")
def step_impl():
    raise NotImplementedError(u'STEP: Then a current account is created')


@given("a customer named Jean-Michel has current account")
def step_impl():
    raise NotImplementedError(u'STEP: And a customer named Jean-Michel has current account')