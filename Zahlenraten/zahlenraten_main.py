# Zahlen Raten
# Toni.T 10.10.24

import random
import os
from funktionen import clear, statistiken, MenuePrint, Punkte_berechnen, WettenGewin, RatenWetten, RandomZahlSpiel

main = True
alle_Punkte = 50
Punkte_Ohne_verlust = 50
spiel = 0
best_versuche = 100
os.system("title Zahlen Raten Spiel Toni.T ")


while main:
    MenuePrint()
    coice = input("Welche Option?: ")

    # Abfrage nach coice

    if coice == "1": # Spiel Starten
        gewin, game_versuche, status = RandomZahlSpiel()
        if status == -1:
            print("Back to Menu")
        elif status == 0:
            alle_Punkte = alle_Punkte + gewin
            spiel = spiel + 1
            # if int(game_versuche) < int(best_versuche):
                # best_versuche = game_versuche - 1 
        
    elif coice == "2": # Wetten  
        if alle_Punkte == 0:
            print("Du hast keine Punkte")
        else:
            gewin, game_versuche, status = RatenWetten(alle_Punkte) # spiel wird gestrtet und werte aus Funktion werden gespeichert 
            if status == -1:
                print("Back to Menu")
            elif status == 0:
                alle_Punkte = alle_Punkte + gewin   # Neuer Punkte stand 
                # if game_versuche < int(best_versuche):
                    # best_versuche = game_versuche - 1
                spiel = spiel +1

    elif coice == "3": # Statistiken
        statistiken(best_versuche, spiel, alle_Punkte)

    elif coice == "4": # Beenden
        main = False

    else:
        input("Ungültige Eingabe...")