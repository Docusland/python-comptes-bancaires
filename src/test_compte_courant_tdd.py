"""
    Unit testing for Compte Courant.
"""

from random import randrange
import pytest
from src.compte import CompteCourant

@pytest.mark.cc
class TestCompteCourant():
    """ Unit testing for a Compte Courant. """

    @pytest.fixture
    def compte_courant(self) -> CompteCourant:
        """ Generate a default CC. """
        return CompteCourant("Username")

    def test_cc_a_un_solde_a_zero_par_defaut(self, compte_courant
    :CompteCourant) -> None:
        """ By default, a newly created CC has no money in it. """
        assert compte_courant.solde == 0

    def test_cc_un_versement(self,compte_courant :CompteCourant) ->\
            None:
        """ If I add money to my account, it should be there. """

        # arrange
        montant = 150

        # act
        compte_courant.versement(montant)

        # assert
        assert compte_courant.solde == montant

    def test_cc_plusieurs_versements(self,compte_courant
    :CompteCourant) -> None:
        """
            If I add several times money to my account,
            everything should be there.
        """

        # arrange
        montant = 150
        nb_versements = randrange(2, 10)

        # act
        for _ in range(nb_versements):
            compte_courant.versement(montant)

        # assert
        assert compte_courant.solde == nb_versements*montant

    @pytest.mark.parametrize("montant", {-150, -99, 0})
    def test_cc_versement_negatif_genere_exception(self,
                  compte_courant :CompteCourant, montant :int) -> None:
        """ Testing several erroneous values. Specified by mark.parametrize """

        # act and assert
        with pytest.raises(Exception):
            compte_courant.versement(montant)

    @pytest.mark.parametrize("montant", {-150, -99, 0})
    def test_cc_retrait_negatif_genere_exception(self,
                  compte_courant :CompteCourant, montant :int) -> None:
        """ Testing several erroneous values. Specified by mark.parametrize """

        # act and assert
        with pytest.raises(Exception):
            compte_courant.retrait(montant)

    def test_cc_retrait_trop_eleve_genere_exception(self,
                  compte_courant :CompteCourant) -> None:
        """ Assert that you cannot take money you do not have. """
        montant: int = 150
        compte_courant.versement(montant)
        # act and assert
        with pytest.raises(Exception):
            compte_courant.retrait(montant + montant)

    def test_cc_affichage(self, compte_courant :CompteCourant):
        """ Check object representation """
        assert 'CompteCourant - Solde : 0' in str(compte_courant)