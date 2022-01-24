import pytest

from src.account import CurrentAccount, SavingsAccount
from src.bank import Bank
from src.customer import Customer


@pytest.mark.v2
class TestBank:

    @pytest.fixture
    def bank(self) -> Bank:
        customers = [Customer("jean premier", [CurrentAccount("jean"), SavingsAccount("jean")]),
                     Customer("jean deuxieme", [CurrentAccount("jean"), SavingsAccount("jean")])]
        return Bank("la_banque_bidule", customers)

    def test_bank_name(self, bank):
        assert bank.name == "la_banque_bidule"

    def test_customers(self, bank):
        assert bank.customers


