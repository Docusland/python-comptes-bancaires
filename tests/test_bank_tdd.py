

import pytest

from src.bank import Bank


@pytest.mark.cc
class TestBank:

    @pytest.fixture
    def bank(self) -> Bank:
        return Bank("la_banque_bidule")


