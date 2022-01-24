import pytest
from src.Bank import Bank
from src.Customer import Customer


@pytest.mark.bank
class TestBank:
    SUPPOSED_CUSTOMER_NAME: str = 'astol'

    SUPPOSED_BANK_NAME: str = 'picsou'

    @pytest.fixture
    def default_bank(self) -> Bank:
        """ default customer account """
        return Bank(bank_name=self.SUPPOSED_BANK_NAME)

    @pytest.fixture
    def default_customer_can_be_removed(self) -> Customer:
        """ default customer account can be removed """
        return Customer(customer_name=self.SUPPOSED_CUSTOMER_NAME)

    @pytest.fixture
    def default_customer_cant_be_removed(self) -> Customer:
        """ default customer account cant be removed """
        return Customer(customer_name=self.SUPPOSED_CUSTOMER_NAME)

    def test_bank_name(self, default_bank: Bank):
        """ test bank name """
        assert self.SUPPOSED_BANK_NAME == default_bank.get_name()

    def test_add_customer(self, default_bank: Bank, default_customer: Customer):
        """ test the add of a new customer in the bank """
        supposed_customer_in_bank = 1
        default_bank.add_customer(default_customer)

        assert len(default_bank.get_customers()) == supposed_customer_in_bank

    # FIXME after fix test in customer check this
    def test_remove_customer_not_removed(self, default_bank: Bank, default_customer_cant_be_removed: Customer):
        """ test the method dont removed the customer """
        supposed_customer_in_bank = 1
        default_bank.add_customer(default_customer_cant_be_removed)
        default_bank.remove_customer(default_customer_cant_be_removed)

        assert len(default_bank.get_customers()) == supposed_customer_in_bank

    def test_remove_customer_removed(self, default_bank: Bank, default_customer_can_be_removed: Customer):
        """ test the method removed the customer """
        supposed_customer_in_bank = 0
        default_bank.add_customer(default_customer_can_be_removed)
        default_bank.remove_customer(default_customer_can_be_removed)

        assert len(default_bank.get_customers()) == supposed_customer_in_bank

    def test_find_customer_by_name_not_find(self, default_bank: Bank, default_customer_can_be_removed: Customer):
        """ write test for checking customer exist in the bank with searched by name """
        not_work_uuid = '0'
        default_bank.add_customer(default_customer_can_be_removed)

        assert not default_bank.find_customer_by_account_uuid(account_uuid=not_work_uuid)

    def test_find_customer_by_name_find(self, default_bank: Bank, default_customer_can_be_removed: Customer):
        """ write test for checking customer exist in the bank with searched by name """
        default_bank.add_customer(default_customer_can_be_removed)
        worked_uuid = default_bank.get_customers()[0].get_accounts()[0].numero_compte
        assert default_bank.find_customer_by_account_uuid(account_uuid=worked_uuid) == default_customer_can_be_removed

    def test_inner_transfer(self, default_bank: Bank, default_customer_can_be_removed: Customer):
        """ test money transfer between two account """
        supposed_amount = 15

        default_bank.add_customer(customer=default_customer_can_be_removed)
        default_bank.get_customers()[0].get_accounts()[0].money_transfer(supposed_amount)

        default_bank.inner_transfer(
            account_from=default_bank.get_customers()[0].get_accounts()[0],
            account_to=default_bank.get_customers()[0].get_accounts()[1],
            amount=supposed_amount,
        )

        assert default_bank.get_customers()[0].get_accounts()[1].account_balance == supposed_amount
