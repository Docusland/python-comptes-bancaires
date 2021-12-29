from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from .compte import CompteCourant

scenarios('features')

@pytest.fixture
def compte_courant():
    return CompteCourant('Default User')

@given("CC is newly created")
def new_cc():
    pass

@given(parsers.parse("I have an existing CC with {montant:d}€"))
def new_cc(compte_courant, montant):
    compte_courant.versement(montant)

@given(parsers.parse("I have an overdraft authorization with a {agios:d}% agios"), target_fixture="compte_courant")
def cc_with_overdraft(agios):
    return CompteCourant('Default User', limiteMax=1000, agios=agios/100)

@when(parsers.parse("I add {amount:d}€"))
def add_to_cc(compte_courant, amount):
    compte_courant.versement(amount)

@when(parsers.parse("I withdraw {amount:d}€"))
def remove_from_cc(compte_courant, amount):
    compte_courant.retrait(amount)

@then(parsers.parse("CC holds {amount:d}€"))
def check_account(compte_courant, amount):
    assert compte_courant.solde == amount