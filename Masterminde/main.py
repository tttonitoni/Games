# Number Wordle nachbauen
# Toni.T 17.10.24

import time
from funktionen import *

# Variabeln
main = True
score_liste = {}

# Main
while main:
    PrintMenue()
    # Menue input
    coice = input("Wahlen sie eine Option: ")

    # Normales Spiel
    if coice == "1":
        clear()
        PrintLogo()

        # ZielZahl wird generirt
        ZielZahl = ZielZahlGen()
        # Regeln werden geprintet
        print("Es könne die ziffern von 0-9 sein")
        # variabeln
        gewonnen = ["Grün"]*5
        Tippfarbe = ["Nichts"]*5
        richtigeziffernliste = ["_"]*5
        versuche = 0

        # loop bis die Zahl geraten wurde
        while Tippfarbe != gewonnen:
            user_zahl,status = user_inputlist()
            if status == "exit":
                break
            Tippfarbe, richtigeziffernliste = UserInputCheck(user_zahl, ZielZahl, Tippfarbe, richtigeziffernliste)
            # versuche werden gezählt
            versuche = versuche + 1

            # Feedback wenn man Gewonnen hat
            if "_" not in richtigeziffernliste:
                clear()
                PrintLogo()
                print("Du hast Gewonnen")
                input(f"Die Zahl war {ZielZahl}")

                # frag ob man auf score bord will
                coice = input("\nVersuche auf scorebord speichern?(y/n): ")
                if coice == "y":
                    name = input("Wie willst du heißen: ")
                    score_liste = score_speichern(score_liste,name,versuche)
                
            # Feedback
            print(Tippfarbe)
            print("------------------------------------------")
            print(f"Es sind die ziffern {richtigeziffernliste}")                

        richtigeziffernliste = None
        Tippfarbe = None
    
    elif coice == "2":
        clear()
        PrintLogo()
        zeige_scoreboard(score_liste)
    
    elif coice == "3":
        clear()
        PrintLogo()
        print("Schönen Tag noch")
        time.sleep(1)
        main = False