import uuid
from abc import ABC

class Compte(ABC):
    """
        Abstract class Compte
    """
    def __init__(self, nomProprietaire, **kwargs):
        self.numeroCompte = uuid.uuid4()
        self.nomProprietaire = nomProprietaire
        self.solde = 0

    def retrait(self, montant= 0):
        if montant <= 0:
            raise Exception('Invalid amount to deduce ' + str(montant))
        if self.solde >= montant:
            self.solde -= montant
        else:
            raise Exception('Invalid operation, not enough money')
        
    def versement(self, montant = 0):
        if montant <= 0:
            raise Exception('Invalid amount to add ' + str(montant))
        self.solde += montant

    def afficherSolde(self): # pragma: no cover
        print("\t - " + str(self))

    def __repr__(self):
        return "{} - Solde : {}".format(type(self).__name__, str(self.solde))

class CompteCourant(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        Compte.__init__(self, nomProprietaire, **kwargs)
        self.autorisationDecouvert = kwargs['limiteMax'] if 'limiteMax' in kwargs else 0
        self.pourcentageAgios = kwargs['agios'] if 'agios' in kwargs else 0

    def appliquerAgios(self):
        if self.solde < 0:
            self.solde *= (1 + self.pourcentageAgios)

    def retrait(self, montant= 0):
        if self.autorisationDecouvert :
            self.solde -= montant
            self.appliquerAgios()
        else:
            Compte.retrait(self, montant)

    def versement(self, montant):
        Compte.versement(self, montant)
        self.appliquerAgios()

class CompteEpargne(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        Compte.__init__(self, nomProprietaire, **kwargs)
        self.pourcentageInterets = kwargs['interets'] if 'interets' in kwargs else 0

    def appliquerInterets(self): # pragma: no cover. Not sure yet if this
        # method of interests is suited
        if self.solde > 0:
            self.solde *= (1 + self.pourcentageInterets)

    def retrait(self, montant= 0):
        Compte.retrait(self, montant)
        self.appliquerInterets()

    def versement(self, montant):
        Compte.versement(self, montant)
        self.appliquerInterets()
