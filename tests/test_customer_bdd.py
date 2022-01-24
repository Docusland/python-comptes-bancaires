from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.customer import Customer

scenarios('./features')


@given("I am an Administrator")
def step_impl():
    raise NotImplementedError(u'STEP: Given I am an Administrator')


@when("I create a customer named Jean-Michel")
def step_impl():
    raise NotImplementedError(u'STEP: When I create a customer named Jean-Michel')


@given("I add them to TurfuBank")
def step_impl():
    raise NotImplementedError(u'STEP: And I add them to TurfuBank')


@then("a customer named Jean-Michel exists")
def step_impl():
    raise NotImplementedError(u'STEP: Then a customer named Jean-Michel exists')


@given("the bank named TurfuBank has customer named Jean-Michel amongst its customers")
def step_impl():
    raise NotImplementedError(
        u'STEP: And the bank named TurfuBank has customer named Jean-Michel amongst its customers')


@given("they have bank TurfuBank")
def step_impl():
    raise NotImplementedError(u'STEP: And they have bank TurfuBank')


@given("they have no accounts")
def step_impl():
    raise NotImplementedError(u'STEP: And they have no accounts')


@when("I create a customer with no name")
def step_impl():
    raise NotImplementedError(u'STEP: When I create a customer with no name')


@then("a customer is not created")
def step_impl():
    raise NotImplementedError(u'STEP: Then a customer is not created')