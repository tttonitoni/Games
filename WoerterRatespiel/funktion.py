import random


def MenuPrint():
    print("1. Spiel Starten")

def getRandomWort(WoerterList):
    gewaehltes_wort = random.choice(WoerterList).lower()
    return gewaehltes_wort

def WoeterRatespil(randomWort):
    eratenebustaben = 0
    laengewort = len(randomWort)
    erratenes_wort = ["_"] * laengewort
    versuche = 6

    print("Das Wort hat", len(randomWort), "Buchstaben.")

    while versuche > 0 and "_" in erratenes_wort:
        user_bustabe = input("\nBitte gib einen einzelnen Buchstaben ein: ").lower()

        if user_bustabe in randomWort:
            print(f"Richtig! {user_bustabe} ist im Wort.")

            for i in range(len(randomWort)):
                if randomWort[i] == user_bustabe:
                    erratenes_wort[i] = user_bustabe

        else:
            versuche -= 1
            print(f"Falsch! Du hast noch {versuche}")
        

        print(" ".join(erratenes_wort))

    if versuche == 0:
        print("Du hast leider Verloren!")
        print(f"Das Wort war {randomWort}")
    else:
        print(f"Du hast das wort erraten. Es war {randomWort}")

