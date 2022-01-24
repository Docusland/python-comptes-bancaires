from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import CurrentAccount

scenarios('./features')

@when(parsers.parse("I add {amount:d}€"))
def add_to_cc(compte_courant, amount):
    compte_courant.money_transfer(amount)
