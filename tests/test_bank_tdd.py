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

    # FIXME problème d'import circulaire
    def test_find_account_by_account_uuid(self, bank):
        # assert bank.find_account_by_account_uuid(0) == "jean"
        pass

    def test_find_account_by_customer_name(self, bank):
        assert bank.find_customer_by_customer_name("jean premier") == "jean premier"

    def test_add_customer_verify_size(self, bank):
        size_before = len(bank.customers)
        bank.add_customer(Customer("jean trois", [CurrentAccount("jean trois"), SavingsAccount("jean trois")]))
        assert size_before == len(bank.customers) - 1

    def test_remove_customer_verify_size(self, bank):
        bank.add_customer(Customer("jean trois", [CurrentAccount("jean trois"), SavingsAccount("jean trois")]))
        size_before = len(bank.customers)
        bank.remove_customer("jean trois")
        assert size_before == len(bank.customers) + 1
