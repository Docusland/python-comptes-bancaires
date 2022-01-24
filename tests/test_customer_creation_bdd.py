from pytest_bdd import given, when, then, parsers, scenarios, scenario
from src.bank import Bank
from src.customer import Customer

scenarios('./features/test_bank_operations.feature')


@given(parsers.parse("I have an existing Bank named {bank_name}"), target_fixture="bank")
def bank(bank_name):
    return Bank(name=bank_name)


@given(parsers.parse("I am an Admin at Westpac bank"))
def create_admin():
    pass


@when(parsers.parse("I add a new Customer named {customer_name}"), target_fixture="customer")
@when(parsers.parse("I add another new Customer named {customer_name}"))
def add_customer(customer_name, bank):
    return Customer(name=customer_name, bank=bank)


@then(parsers.parse("a new Customer named {customer_name} exists"))
def check_customer(customer_name, customer):
    assert customer.name == customer_name


@then(parsers.parse("the bank has {number} Customer"))
@then(parsers.parse("the bank has {number} Customers"))
def check_number_of_customers(number):
    assert len(bank.customers) == number
