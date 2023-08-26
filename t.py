import random

def spin_wheel():
    return random.randint(0, 36)

if __name__ == "__main__":
    while True:
        input("Appuyez sur Entrée pour lancer la roulette...")
        numero = spin_wheel()
        print(f"Le numéro gagnant est : {numero}")