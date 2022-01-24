from src.customer import Customer


class Bank:
    """
        Bank.
        Object representing a classic bank.
        Has a name, a list of customers, and can transfer money.
    """

    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer: Customer):
        """ Add customer to bank customers, and assign the bank to the customer"""
        self.customers.append(customer)
        customer.add_bank(self.name)

    def remove_customer(self, customer: Customer):
        """ Remove customer from bank customers, and remove the bank from the customer"""
        self.customers.remove(customer)
        customer.remove_bank()

    def get_customers(self):
        """ Return bank's customers array"""
        return self.customers

    def has_customers(self):
        if len(self.customers) > 0:
            return True
        else:
            return False

    def find_customer_by_account_uuid(self, account_uuid: str):
        """ Return customer if account id is equal to string"""
        for customer in self.customers:
            for account in customer.accounts:
                if account.numero_compte == account_uuid:
                    return customer

    def find_customer_by_customer_name(self, name: str):
        """ Return customer if customer name is equal to string"""
        for customer in self.customers:
            if customer.name == name:
                return customer

    def inner_transfer(self, amount: int, account_from, account_to):
        """
            Transfer money between customers of the same bank,
            if banks aren't the same return false,
            if account doesn't have enough money return false
        """
        if account_from.account_balance - amount < 0:
            return False

        account_from_bank = False
        account_to_bank = False
        for customer in self.customers:
            for account in customer.accounts:
                if account == account_from:
                    account_from_bank = True
                if account == account_to:
                    account_to_bank = True

        if account_from_bank & account_to_bank:
            account_from.money_withdraw(amount)
            account_to.money_transfer(amount)
        else:
            return False

    def __repr__(self):
        return f'{self.name} {self.customers}'

