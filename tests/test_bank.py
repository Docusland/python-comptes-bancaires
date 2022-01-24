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
    def default_customer(self) -> Customer:
        """ default customer account """
        return Customer(customer_name=self.SUPPOSED_NAME)

    def test_bank_name(self, default_bank: Bank):
        """ test bank name """
        assert self.SUPPOSED_BANK_NAME == default_bank.get_name()
