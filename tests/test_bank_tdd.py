import pytest

from src.account import CurrentAccount, SavingsAccount
from src.bank import Bank
from src.customer import Customer


@pytest.mark.v2
class TestBank:

    @pytest.fixture
    def bank(self) -> Bank:
        customers = [Customer("jean premier", [CurrentAccount("jean premier"), SavingsAccount("jean premier")]),
                     Customer("jean deuxieme", [CurrentAccount("jean deuxieme"), SavingsAccount("jean deuxieme")])]
        return Bank("la_banque_bidule", customers)

    def test_bank_name(self, bank):
        assert bank.name == "la_banque_bidule"

    def test_customers(self, bank):
        assert bank.customers

    def test_transfer_money_took_money_of_first_account_of_first_customer(self, bank):
        bank.customers[0].accounts[0].money_transfer(10)
        bank.customers[1].accounts[0].money_transfer(10)
        bank.inner_tranfer(bank.customers[0].accounts[0], bank.customers[1].accounts[0])
        assert bank.customers[0].accounts[0].account_balance == 0

    def test_transfer_money_gives_money_to_first_account_of_second_customer(self, bank):
        bank.customers[0].accounts[0].money_transfer(10)
        bank.customers[1].accounts[0].money_transfer(10)
        bank.inner_tranfer(bank.customers[0].accounts[0], bank.customers[1].accounts[0])
        assert bank.customers[1].accounts[0].account_balance == 20
