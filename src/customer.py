from account import *


class Customer():
    def __init__(self, name, bank, current_account: CurrentAccount, savings_account: SavingsAccount):
        self.name = name
        self.bank = bank
        self.current_account = current_account
        self.savings_account = savings_account

    def inner_transfer(self, account_from: Account, account_number_to: Account, amount: int):
        for i in range(len(self.bank.customers)):
            if account_number_to.numero_compte == self.bank.customers[i]:
                account_from.money_withdraw(amount)
                account_number_to.account_balance(amount)
