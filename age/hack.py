import random
import time

startzeit = time.time()

while time.time() - startzeit < 3:
    # Länge der Sequenz
    laenge1 = random.randint(20,40)
    laenge2 = random.randint(25,55)

    # Erstelle eine Liste mit zufälligen 0 und 1
    sequenz1 = [random.randint(0, 1) for _ in range(laenge1)]
    sequenz2 = [random.randint(0, 1) for _ in range(laenge2)]

    # Die Liste in eine Zeichenkette umwandeln und ohne Kommas oder Klammern drucken
    print(''.join(map(str, sequenz1 + sequenz2)))
    