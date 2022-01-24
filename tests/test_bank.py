import pytest
from src.Customer import Customer
from src.account import Account


@pytest.mark.customer
class TestCustomer():
    SUPPOSED_NAME: str = 'astol'

    SUPPOSED_NEW_ACCOUNT_NAME: str = 'added_account'

    @pytest.fixture
    def default_bank(self) -> Customer:
        """ default customer account """
        return Customer(customer_name=self.SUPPOSED_NAME)

    @pytest.fixture
    def default_new_account(self) -> Account:
        """ default new account """
        return Account(owner_name=self.SUPPOSED_NEW_ACCOUNT_NAME)

    def test_bank_name(self, default_customer: Customer):
        """ test bank name """
