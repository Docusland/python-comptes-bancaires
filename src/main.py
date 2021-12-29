from colorama import Fore
from .compte import *
import src.constants as constants


def ui_saisie_montant():
    """
        stdout : input money
    """
    cc = None
    while cc not in [constants.COMPTE_COURANT, constants.COMPTE_EPARGNE]:
        print(Fore.BLACK + """ Sur quel compte ? 
                 1 - Compte Courant
                 2 - Compte Epargne
                 """)
        cc = input()
    account = compteC if cc == constants.COMPTE_COURANT else compteE

    print("Quel montant ?")
    try:
        amount = float(input())
        account.versement(amount) if amount > 0 else account.retrait(-1 * amount)
    except Exception as e:
        print(Fore.RED + 'ERROR : An exception occured : ' + getattr(e, 'message', repr(e)))


def ui_affichage_soldes() :
    """
        stdout : Display account statuses.
    """
    print(Fore.BLACK + 'Affichage des soldes : ')
    compteC.afficherSolde()
    compteE.afficherSolde()

def ui():
    """
        Basic stdout user interface.
    """
    not_exit = True
    while not_exit:
        print(Fore.BLACK + """Que voulez-vous faire ? 
                        1 - Saisir une depense ou un virement
                        2 - Voir mon solde
                        3 - Quitter
                        """)
        choice = input()

        if choice == constants.APP_VIREMENT:
            ui_saisie_montant()
            pass
        elif choice == constants.APP_SOLDE:
            ui_affichage_soldes()
            pass
        elif choice == constants.APP_QUITTER:
            not_exit = False
            pass
        else:
            print('Réponse non comprise, veuillez réessayer.')
            continue;


user = 'TestUser'
compteE = CompteEpargne(user, interets=0.1)
compteC = CompteCourant(user, agios=0.1, limiteMax=1000)

if __name__ == '__main__':
    ui()
