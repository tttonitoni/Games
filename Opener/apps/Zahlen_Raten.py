# Spiel-Zahlen Raten
# Toni.T 26.9.24

import random

r_zahl = random.randint(1, 1000)
e = None

while  e != r_zahl:
    e = int(input("Zahl von 1-1000: "))

    if e < r_zahl:
        print("Zu nidrig!")
    elif e > r_zahl:
        print("Zu hoch!")
    else:
        print(f"Du hast die Zahl {r_zahl} erraten")

    


