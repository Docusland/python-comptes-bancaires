import pytest
from random import randrange
from src.account import SavingsAccount
from src.customer import Customer

@pytest.mark.ce
class TestCompteEpargne():

    @pytest.fixture
    def compte_epargne(self):
        """ Default CE Account. """
        customer = Customer('Sterenn Grace')
        return SavingsAccount(customer)

    def test_CompteEpargne_a_un_solde_a_zero_par_defaut(self, compte_epargne:SavingsAccount) -> None:
        """ By default a newly created account should have 0 €. """
        assert compte_epargne.account_balance == 0

    def test_CompteEpargne_versement_retrait(self, compte_epargne:SavingsAccount):
        montant :int = 150
        compte_epargne.money_transfer(montant)
        compte_epargne.money_withdraw(montant)