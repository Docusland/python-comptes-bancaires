import pytest
from random import randrange
from .compte import CompteEpargne

@pytest.mark.ce
class TestCompteEpargne():

    @pytest.fixture
    def compte_epargne(self):
        """ Default CE Account. """
        return CompteEpargne("Username")

    def test_CompteEpargne_a_un_solde_a_zero_par_defaut(self, compte_epargne:CompteEpargne) -> None:
        """ By default a newly created account should have 0 €. """
        assert compte_epargne.solde == 0

    def test_CompteEpargne_versement_retrait(self,compte_epargne:CompteEpargne):
        montant :int = 150
        compte_epargne.versement(montant)
        compte_epargne.retrait(montant)