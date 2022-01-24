import pytest
from src.bank import Bank


@pytest.mark.v2
class TestBank:

    @pytest.fixture
    def bank(self) -> Bank:
        return Bank("la_banque_bidule")


