from src.utils import add, subtract, multiply, divide


def get_user_input():
    """Demande à l'utilisateur de choisir une opération et de saisir deux nombres."""
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Entrez votre choix (1/2/3/4) : "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))

        return choice, num1, num2
    except ValueError as e:
        print(f"Erreur : {e}")
        return None


def perform_calculation(choice, num1, num2):
    """Effectue le calcul en fonction du choix de l'utilisateur."""
    if choice == 1:
        return add(num1, num2)
    elif choice == 2:
        return subtract(num1, num2)
    elif choice == 3:
        return multiply(num1, num2)
    elif choice == 4:
        try:
            return divide(num1, num2)
        except ValueError as e:
            return str(e)


def main():
    """Fonction principale pour exécuter la calculatrice."""
    while True:
        user_input = get_user_input()
        if not user_input:
            continue  # Redemander en cas d'erreur

        choice, num1, num2 = user_input
        result = perform_calculation(choice, num1, num2)
        print(f"Résultat : {result}")

        another_calculation = input("Voulez-vous faire un autre calcul ? (o/n) : ").strip().lower()
        if another_calculation != 'o':
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            break


if __name__ == "__main__":
    main()
