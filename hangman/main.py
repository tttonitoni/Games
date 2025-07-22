# Hangman nach machen 
# Toni.T 27.10.24

import random

# Wörter liste und random auswahl
wörter = ["hallo","becher","eichel","auto","eier","esel","rakete","durchfall"]
random_wort = random.choice(wörter)

#Liste mit Anzahl der bustaben wird erstelt
wort_liste = []
for bustaben in random_wort:
    wort_liste += "_"

#main
print("Wilkommen zu Hangman")
game_over = False
while not game_over:
    bustabe = input("Raten sie einen Bustaben: ").lower()

    for index in range(len(random_wort)):
        if bustabe == random_wort[index]:
            wort_liste[index] = bustabe
    print(wort_liste)

    if "_" not in wort_liste:
        print(f"Du hast das Wort {random_wort} eraten")
        game_over = True

