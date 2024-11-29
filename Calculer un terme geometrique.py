from colorama import Fore, Style

def terme_suite_geometrique(Ux, y, q, n):
    """
    Calcule le terme Un de la suite géométrique reçu par Un = U0 * q^(n-1) 
    :param Ux: numéro du terme donné
    :param y: valeur du terme donné
    :param q: raison de la suite
    :param n: numéro du terme à calculer
    :return: valeur du terme Un
    """
    U0 = y / (q ** (Ux - 1))  
    Un = U0 * (q ** (n - 1))  #mdr
    return Un

def main():
    exit_command = 'exit'
    while True:
        try:
            print()
            user_input = input("Tape 'exit' pour quitter : ")
            if user_input.lower() == exit_command:
                print("Fin du programme.")
                break

            Ux = int(input("C'est quoi le rang du terme donné ? : "))
            y = float(input("Ok cool, et il est égal à combien ? : "))
            q = float(input("Quelle est la raison (q) ? : "))
            n = int(input("Numéro du terme à calculer : "))

            Un = terme_suite_geometrique(Ux, y, q, n)
            print("\nRésultat du calcul :")
            print(f"Le rang du terme donné est : {Fore.BLUE}{Ux}{Style.RESET_ALL}")
            print(f"La valeur du terme donné est : {Fore.BLUE}{y}{Style.RESET_ALL}")
            print(f"La raison (q) est : {Fore.GREEN}{q}{Style.RESET_ALL}")
            print(f"Le numéro du terme à calculer : {Fore.YELLOW}{n}{Style.RESET_ALL}")
            print(f"Le résultat est : {Fore.RED}{Un}{Style.RESET_ALL}")
            
        except ValueError:
            print("Erreur : entre une valeur valide.")
        except ZeroDivisionError:
            print("Erreur : la raison (q) ne peut pas être nulle.")

if __name__ == "__main__":
    main()
