import uuid
from abc import ABC


class Account(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, customer: str):
        """ default constructor """
        self.numero_compte = uuid.uuid4()
        self.customer = customer
        self.account_balance = 0

    def money_withdraw(self, amount=0, forceWithdrawal=False):
        """ default withdrawal. """
        if amount <= 0:
            raise Exception('Invalid amount to deduce ' + str(amount))
        if self.account_balance >= amount or forceWithdrawal:
            self.account_balance -= amount
        else:
            raise Exception('Invalid operation, not enough money')

    def money_transfer(self, montant=0):
        """ default money transfer. """
        if montant <= 0:
            raise Exception('Invalid amount to add ' + str(montant))
        self.account_balance += montant

    def afficher_solde(self):  # pragma: no cover
        """ FIXME: This console display should not be here. """
        print("\t - " + str(self))

    def __repr__(self):
        name = type(self).__name__
        solde = str(self.account_balance)
        return f'{name} - Solde : {solde}'


class CurrentAccount(Account):
    """
            Compte Courant.
            Object representing a classical bank account.
            Can store money. If the balance is negative, generates agios.
    """

    def __init__(self, customer, **kwargs):
        """
            Constructor.
            Args:
                **kwargs : Can contain attributes :
                    - max_limit,specifying the maximum negative balance
                    the owner can have.
        """
        Account.__init__(self, customer)
        self.negative_balance_limit = kwargs['max_limit'] if 'max_limit' in kwargs else 0
        self.agios_percentage = kwargs['agios'] if 'agios' in kwargs else 0

    def apply_agios(self) -> None:
        """
        Apply agios percentage if negative balance.
        """
        if self.account_balance < 0:
            self.account_balance *= (1 + self.agios_percentage)

    def can_withdraw(self, amount) -> bool:
        """
        Check if the user can withdraw money.
        :param amount : the amount to withdraw
        :return: boolean : the current situation
        """
        basic_rule = amount < self.account_balance

        limit_rule = self.negative_balance_limit > \
                     abs(self.account_balance - amount)
        return basic_rule or limit_rule

    def money_withdraw(self, amount=0):
        """ Can withdraw money if it respects the limitation rules. """
        Account.money_withdraw(self, amount, self.can_withdraw(amount))
        self.apply_agios()

    def money_transfer(self, montant=0):
        """ Appliquer les agios en prime. """
        Account.money_transfer(self, montant)
        self.apply_agios()


class SavingsAccount(Account):
    """
    Compte Epargne d'un particulier.
    Génère des interets.
    """

    def __init__(self, customer, **kwargs):
        """

        :param customer:
        :param kwargs: Can contain attributes :
                    - interests,specifying the maximum negative balance
                    the owner can have.
        """
        Account.__init__(self, customer)
        self.interests_percentage = kwargs['interests'] if 'interests' in kwargs else 0

    def apply_interests(self):  # pragma: no cover.
        # FIXME: Not sure yet if this
        # method of interests is suited
        if self.account_balance > 0:
            self.account_balance *= (1 + self.interests_percentage)

    def money_withdraw(self, amount=0):
        """ Appliquer les interets en prime """
        Account.money_withdraw(self, amount)
        self.apply_interests()

    def money_transfer(self, montant=0):
        """ Appliquer les interets en prime """
        Account.money_transfer(self, montant)
        self.apply_interests()
