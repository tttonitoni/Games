# Funktionen für main

import random
import os

def PrintMenue():
    clear()
    PrintLogo()
    print("Wilkommen zu Numberle")
    print()
    print("1.Spiel Starten     2. Scoreboard") 
    print("3.Beenden")
    print()

def PrintLogo():
    logo = r"""
     _ _  _ _  __ __  ___  ___  ___  _    ___ 
    | \ || | ||  \  \| . >| __>| . \| |  | __>
    |   || ' ||     || . \| _> |   /| |_ | _> 
    |_\_|`___'|_|_|_||___/|___>|_\_\|___||___>
                                          
------------------------------------------------------------ 
    """


    print(logo)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def ZielZahlGen():
    ZielZahl = str(random.randint(0,99999))
    ZielZahl = ZielZahl.zfill(5)
    ZielZahl = list(ZielZahl)
    return ZielZahl

def user_inputlist():
    user_zahl = input("Geben sie ein 5 stellige Zahl ein: ")
    if user_zahl == "exit":
        return None, "exit"
    user_zahl = user_zahl.zfill(5)
    user_zahl = list(user_zahl)
    return user_zahl, None

# score board
def score_speichern(score_liste,name,versuche):
    if name in score_liste:
        score_liste[name] = versuche # Punkte zum bestehenden Score hinzufügen
    else:
        score_liste[name] = versuche   # Neuen Spieler mit Punkten hinzufügen
    return score_liste 

def zeige_scoreboard(score_liste):
    print("Scoreboard:")
    for spieler, punkte in score_liste.items():
        print(f"{spieler}: {punkte} Verscuhe")
    input()

def copylist(List):
    copyList = List
    copyList = list(copyList)
    return copyList

def UserInputCheck(user_zahl, ZielZahl, Tippfarbe, richtigezahlenliste):  
    copyZielZahl = copylist(ZielZahl)

    for index in range(5):
        
        if user_zahl[index] not in copyZielZahl:
            Tippfarbe[index] = "Grau"

            user_zahl[index] = "Checked" # User_zahl wird mit nichts ersätz


    for index in range(5):
        if user_zahl[index] ==  copyZielZahl[index]: # Wenn Richtige Zahl Richtige stelle
            Tippfarbe[index] = "Grün"
            copyZielZahl[index] = None 

            # Richtigen ziffern werden gespeichert
            richtigezahlenliste[index] = user_zahl[index]
            user_zahl[index] = "Checked" # User_zahl wird mit nichts ersätzt

    for index in range(5):
        if user_zahl[index] in copyZielZahl: # Wenn Zahl in ZielListe ist
            Tippfarbe[index] = "Gelb"

            # Zahl wird aus KoporterZielZahl liste mit None ersätzt
            ziel_index = copyZielZahl.index(user_zahl[index]) # findet die user_zahl in copy liste
            copyZielZahl[ziel_index] = None # ersätzt die user_zahl mit None
        
    #ä gefilterte_liste_ziffern = [element for element in richtigezahlenliste if element is not None]

    return Tippfarbe, richtigezahlenliste