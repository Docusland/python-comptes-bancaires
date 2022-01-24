"""
    Unit testing for Compte Courant.
"""

from random import randrange
import pytest
from src.account import CurrentAccount


@pytest.mark.cc
class TestCompteCourant:
    """ Unit testing for a Compte Courant. """

    @pytest.fixture
    def compte_courant(self) -> CurrentAccount:
        """ Generate a default CC. """
        return CurrentAccount("Username")

    @pytest.fixture
    def compte_courant_ayant_decouvert(self):
        return CurrentAccount("Username", max_limit=1000, agios=0.1)

    def test_cc_a_un_solde_a_zero_par_defaut(self, compte_courant
    : CurrentAccount) -> None:
        """ By default, a newly created CC has no money in it. """
        assert compte_courant.account_balance == 0

    def test_cc_un_versement(self, compte_courant_ayant_decouvert: CurrentAccount) -> \
            None:
        """ If I add money to my account, it should be there. """

        # arrange
        montant = 150

        # act
        compte_courant_ayant_decouvert.money_transfer(montant)

        # assert
        assert compte_courant_ayant_decouvert.account_balance == montant

    def test_cc_plusieurs_versements(self, compte_courant
    : CurrentAccount) -> None:
        """
            If I add several times money to my account,
            everything should be there.
        """

        # arrange
        montant = 150
        nb_versements = randrange(2, 10)

        # act
        for _ in range(nb_versements):
            compte_courant.money_transfer(montant)

        # assert
        assert compte_courant.account_balance == nb_versements * montant

    @pytest.mark.parametrize("montant", {-150, -99, 0})
    def test_cc_versement_negatif_genere_exception(self,
                                                   compte_courant: CurrentAccount, montant: int) -> None:
        """ Testing several erroneous values. Specified by mark.parametrize """

        # act and assert
        with pytest.raises(Exception):
            compte_courant.money_transfer(montant)

    @pytest.mark.parametrize("montant", {-150, -99, 0})
    def test_cc_retrait_negatif_genere_exception(self,
                                                 compte_courant: CurrentAccount, montant: int) -> None:
        """ Testing several erroneous values. Specified by mark.parametrize """

        # act and assert
        with pytest.raises(Exception):
            compte_courant.money_withdraw(montant)

    def test_cc_retrait_trop_eleve_genere_exception(self,
                                                    compte_courant: CurrentAccount) -> None:
        """ Assert that you cannot take money you do not have. """
        montant: int = 150
        compte_courant.money_transfer(montant)
        # act and assert
        with pytest.raises(Exception):
            compte_courant.money_withdraw(montant + montant)

    def test_cc_affichage(self, compte_courant: CurrentAccount):
        """ Check object representation """
        assert 'Solde : 0' in str(compte_courant)
