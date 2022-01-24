from src.customer import Customer
from src.bank import Bank
from src.account import CurrentAccount
from src.account import SavingsAccount
import pytest

@pytest.mark.customer
class TestCustomer():

    def setUp(self) -> None:
        self.bank = Bank("MyBank")
        self.account = CurrentAccount("CC", max_limit=1000, agios=0.1)
        self.savings_account = SavingsAccount("CE", interest=0.2)
        self.customer = Customer("customer", Bank(), CurrentAccount(), SavingsAccount())

    # Create new customer
    def test_create_new_customer(self) -> Customer:
        assert self.customer