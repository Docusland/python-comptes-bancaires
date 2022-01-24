from src.customer import Customer
from src.bank import Bank
from src.account import CurrentAccount
from src.account import SavingsAccount
import pytest

@pytest.mark.customer
class TestCustomer():

    def setUp(self) -> None:

        self.foreignAccount = CurrentAccount("ForeignAccount")

        self.bank = Bank("MyBank")
        self.account = CurrentAccount("CC")
        self.savings_account = SavingsAccount("CE")

        self.customer = Customer("customer", self.bank, self.account, self.savings_account)

    # Create new customer
    def test_create_new_customer(self) -> Customer:
        assert self.customer

    def test_amount_zero(self):
        assert self.account.account_balance == 0
