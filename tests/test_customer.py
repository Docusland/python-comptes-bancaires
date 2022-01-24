import pytest
from src.customer import Customer

@pytest.mark.customer
class TestCustomer():

    @pytest.fixture
    def add_Account(self):
        """ Default CE Account. """
        pass

    def remove_Account(self):
        """ By default a newly created account should have 0 €. """
        pass

    def test_CompteEpargne_versement_retrait(self, compte_epargne:SavingsAccount):
        montant :int = 150
        compte_epargne.money_transfer(montant)
        compte_epargne.money_withdraw(montant)
