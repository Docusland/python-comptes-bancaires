import pytest

from src.customer import Customer


class TestCustomer:

    @pytest.fixture
    def default_customer(self):
        return Customer("TheoJOUAN")

    def test_name_Customer(self, default_customer):
        assert default_customer.name == "TheoJOUAN"
