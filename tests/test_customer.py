import pytest
from src.Customer import Customer
from src.account import Account


@pytest.mark.customer
class TestCustomer():

    SUPPOSED_NAME: str = 'astol'

    SUPPOSED_NEW_ACCOUNT_NAME: str = 'added_account'

    @pytest.fixture
    def default_customer(self) -> Customer:
        """ default customer account """
        return Customer(customer_name=self.SUPPOSED_NAME)

    @pytest.fixture
    def default_new_account(self) -> Account:
        """ default new account """
        return Account(owner_name=self.SUPPOSED_NEW_ACCOUNT_NAME)

    def test_customer_name(self, default_customer: Customer):
        """ test if the saving account match with the username given """
        assert self.SUPPOSED_NAME == default_customer.get_name()

    def test_customer_ca_name(self, default_customer: Customer):
        """ test if the saving account match with the username given """
        assert default_customer.get_name() == default_customer.get_ca_name()

    def test_customer_sc_name(self, default_customer: Customer):
        """ test if the saving account match with the username given """
        assert default_customer.get_name() == default_customer.get_sc_name()

    def test_add_account(self, default_customer: Customer, default_new_account: Account):
        """ TODO test the transfer between two account for customer"""
        base_list: list = default_customer.get_accounts()
        base_list.append(default_new_account)

        default_customer.add_account(account=default_new_account)

        assert base_list == default_customer.get_accounts()
