import pytest

from src.account import CurrentAccount, SavingsAccount
from src.customer import Customer


@pytest.mark.v2
class TestCustomer:
    @pytest.fixture
    def customer(self) -> Customer:
        return Customer("lecompteici", CurrentAccount("jean"), SavingsAccount("jean"))
