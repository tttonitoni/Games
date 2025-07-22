# Funktionen für Zahlen raten Spiels
# Toni.T 11.10.24

import random, os

def clear():
    os.system('cls')

def logo_print():
    logo = f"""
        ╦═╗ ╔═╗ ╔╦╗ ╔═╗  ╔═╗ ╔═╗ ╦ ╔═╗ ╦  
        ╠╦╝ ╠═╣  ║  ║╣   ╚═╗ ╠═╝ ║ ║╣  ║  
        ╩╚═ ╩ ╩  ╩  ╚═╝  ╚═╝ ╩   ╩ ╚═╝ ╩═╝
      by Toni.T (exit = menue)
-----------------------------------------------"""
    print(logo)

def statistiken(defBest_versuche, defSpiel,alle_Punkte):
    clear()
    logo_print()
    print("")
    print(f" Punkte: {int(alle_Punkte)}")
    print(f" Gespielten Spiele: {defSpiel}")
    if defSpiel > 0:
        print(f" Am schnestelsten geschaft in: {defBest_versuche} versuchen")
    else:
        print(" Am schnestelsten geschaft in: 0 versuchen")
    print(f"")
    input("Drücke Enter um Fortzufahren...")


def MenuePrint():
        clear()
        logo_print()
        print("")
        print(f" 1.Starte Spiel       3.Statistiken")
        print(f" 2.Punkte Wetten      4.Beenden    ")
        print()
        # print("3.Statistiken (Beta)")

def createStatus(user_input): 
   if user_input == "exit":
       return -1
   else:
       return 0

def validinputInt(text):
    while True:
        user_input_text = None
        try:
            user_input_text = input(text)
            user_input = int(user_input_text)
            return user_input, 0
        except ValueError:
            status = createStatus(user_input_text)
            if status == -1:
                return None, status
            else:
                input("Ungültige Eingabe...")
                

def validinputFloat(text):
    while True:
        try:
            user_input_text = input(text)
            user_input = float(user_input_text)
            return user_input, 0
        except ValueError:
            status = createStatus(user_input_text)
            if status == -1:
                return None, status
            else:
                input("Ungültige Eingabe...")
                

def inputPunkteCheck(text,alle_punkte):
    user_input, status = validinputFloat(text)
    while True:
        if status == -1:
            return None, -1
        elif user_input <= alle_punkte:
            return user_input, status
        else:
            print("Nicht Genug Punkte")
            user_input, status = validinputFloat("Wie viele Punkte setzten sie: ")
        
# Brechnet die Punkte die Gewonnen werden
def Punkte_berechnen(def_versuche):
    def_punkte = 0
    gewin = 100/def_versuche
    def_punkte = def_punkte + gewin
    return def_punkte

# Berechnet Gewinn beim wetten 
def WettenGewin(einsatztP,rateVersuche):
    multiplikartor = 5 / rateVersuche
    win = einsatztP * multiplikartor
    return win

def RatenWetten(alle_Punkte):
    clear()

    # Variabeln
    a = random.randint(1,100)
    user_input = None
    versuche = 1
    gewinn = 0

    # Wetten Input
    logo_print()
    print(f"Sie haben {alle_Punkte} Punkte")
    einsatzt_P, status = inputPunkteCheck("Wie viele Punkte setzten sie: ", alle_Punkte)
    if status == -1:
        return None, None, -1
    ratenVersuch, status = validinputInt("In wie vielen versuchen wollen sie es schafen(1-10)?: ")
    if status == -1:
        return None, None, -1
    while user_input != a:
        # Input
        print("_______________________")
        print(f"Versuche: {versuche}")
        user_input, status = validinputInt("Zahl zwischen 1-100: ") # input
        if status == -1:
            return None, None, -1
        
        # Überprüfung von input
        if user_input == a:
                clear()
                gewinn = WettenGewin(einsatzt_P, ratenVersuch)
                print(f"Die Zahl war {a}")
                print(f"Du hast {int(gewinn)} Punkte gewonnen und {versuche} versuche gebraucht")
                input("Drücken sie Enter um Fortzufahren...")
                return gewinn, versuche, 0        
        elif user_input != a:
            if a > user_input:
                print(f"Die Zahl ist Größer als {user_input}")
            elif a < user_input:
                print(f"Die Zahl ist Kleiner als {user_input}")

        versuche = versuche + 1

        if versuche > ratenVersuch:
            clear()
            print(f"die zahl war {a} und sie haben {einsatzt_P} Punkte Verloren")
            input("Drücken sie Enter um Fortzufahren...")
            return  -einsatzt_P , None, 0


def RandomZahlSpiel():
    clear()
    logo_print()
    # Varibaeln
    spiel_punkte = 0
    a = random.randint(1,100)
    versuche = 1
    user_input = None

    while user_input != a:
        if versuche == 1:
            None
        else:
            print("_______________________")

        # input
        user_input, status = validinputInt("Zahl zwischen 1-100: ")

        # Status check
        if status == -1:
            return None ,None, -1

        # Überprüfung von input
        if user_input == a:
            print(f"Du hast Gewonnen. Die Zahl war {a}")
            spiel_punkte = Punkte_berechnen(versuche)
            input(f"Du hast {versuche} versuche gebraucht und damit {int(spiel_punkte)} punkte bekommen")
        
        elif user_input != a:
            if a > user_input:
                print(f"Die Zahl ist Größer als {user_input}")
            elif a < user_input:
                print(f"Die Zahl ist Kleiner als {user_input}")
        else:
            print("Ungültige Eingabe...")
            
            
        versuche = versuche +1

    return spiel_punkte, versuche, 0