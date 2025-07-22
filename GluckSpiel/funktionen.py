from farbenGrafiken import *
import random
import os
import copy

def clear_console():
    # Für Windows
    if os.name == 'nt':
        os.system('cls')
    # Für macOS und Linux
    else:
        os.system('clear')

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(row))

def Validint(text):
    while True:
        inp = input(text)
        if inp == "stop" or inp == "Stop":
            return inp
        try:
            vldint = int(inp)
            return vldint
        except:
            print("!!Eine nicht komma Zahl!!")

def ValidCord(text):
    while True:
        cord = Validint(text)
        if cord == "Stop" or cord == "stop":
            return cord
        if cord > 5:
            print("Gibt es nicht")
        else:
            if cord == 1:
                return cord
            elif cord == 2:
                return cord + 1
            elif cord == 3:
                return cord + 2
            elif cord == 4:
                return cord + 3
            else:
                return cord + 4


def Menu(Geld):
    corektcoice = False
    LogoPrint(Logo)
    print(f"     {farb4}|{zuruecksetzen} 1.Start                        {farb4}|{zuruecksetzen} Geld = {Geld}$")
    print(f"     {farb4}|{zuruecksetzen} 2.Beenden\n")

    while not corektcoice:
        coice = input(f"[{farb3}+{zuruecksetzen}] : ")

        if coice == "1":
            return coice
        
        elif coice == "2":
            return coice
        
def Randomize(Falschefelder,defsSpielfeld,spiel):
        
        cordlist = [1,3,5,7,9]
        if spiel == 0:
            Falschefelder = 2

        for i in range(Falschefelder):
            ValidFeld = True
            while ValidFeld:
                x = random.choice(cordlist)
                y = random.choice(cordlist)
                if defsSpielfeld[y][x] == " ":
                    defsSpielfeld[y][x] = "X"
                    ValidFeld = False
        
        return defsSpielfeld

def SpielfeldPrint(Spielfeld):
    cordlist = [1,3,5,7,9]
    i = 0
    zahl = 1
    for row in Spielfeld:
        if i in cordlist:
            print(zahl," ".join(row))
            zahl += 1
        elif i == 0:
            print("Y"," ".join(row))
        else:
            print(" "," ".join(row))
        i += 1
    print("    1   2   3   4   5 X")

def Playerturn(defSpielfeld,Falschefelder,einsatz,spiel):
    Playermap =  [
        ["┌","—","┬","─","┬","─","┬","─","┬","─","┐"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"], # 1:1, 1:3, 1:5, 1:7, 1:9
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],  
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],
        ["└","—","┴","─","┴","─","┴","─","┴","─","┘"],
    ]
    FeldmitX = Randomize(Falschefelder,defSpielfeld,spiel)
    RichtigeFelder = 0

    for i in range(5*5-Falschefelder):
        clear_console()
        LogoPrint(Logo)
        SpielfeldPrint(Playermap)
        print("Welche Felder sind nicht Falsch?(Stop um Rauszugehen)\n")

        # Input
        Y = ValidCord(f"[{farb3}+{zuruecksetzen}] : Y=")
        if Y == "Stop" or Y == "stop":
            return RichtigeFelder
        X = ValidCord(f"[{farb3}+{zuruecksetzen}] : X=")
        if X == "Stop" or X == "stop":
            return RichtigeFelder


        if FeldmitX[Y][X] == "X":
            input(f"[{farb3}+{zuruecksetzen}] : Falsch! -{einsatz}")
            return "Lose"
        
        elif Playermap[Y][X] == "☼":
            input(f"[{farb3}+{zuruecksetzen}] : Schon überpruft!")

        else:
            RichtigeFelder += 1
            input(f"[{farb3}+{zuruecksetzen}] : Richtig! Richtigefelder={RichtigeFelder}")
            Playermap[Y][X] = "☼"
    
    if RichtigeFelder == 1:
        return RichtigeFelder + 10
    else:
        return RichtigeFelder
        



def Startgame(Geld,spiel):
    Spielfeld = [
        ["┌","—","┬","─","┬","─","┬","─","┬","─","┐"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"], # 1:1, 1:3, 1:5, 1:7, 1:9
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],  
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],
        ["├","─","┼","─","┼","─","┼","─","┼","─","┤"],
        ["│"," ","│"," ","│"," ","│"," ","│"," ","│"],
        ["└","—","┴","─","┴","─","┴","─","┴","─","┘"],
    ]
        
    clear_console()
    LogoPrint(Logo)

    Falschefelder = Validint(f"[{farb3}+{zuruecksetzen}] : Wie viele Falschefelder: ")
    if Falschefelder == "Stop" or Falschefelder == "stop":
        return Geld, 0
    quoteProFeld = 1/(25/Falschefelder)
    print(f"[{farb3}+{zuruecksetzen}] : 1x Feld={quoteProFeld}")
    einsatz = Validint(f"[{farb3}+{zuruecksetzen}] : Was ist dein einsatz: ")
    if einsatz == "Stop" or einsatz == "stop":
        return Geld, 0
    
    if einsatz > Geld:
        print("Zuwenig Geld")
        return Geld, 0
    else:
        Geld -= einsatz

    Richtigefelder = Playerturn(Spielfeld,Falschefelder,einsatz,spiel)
    if Richtigefelder != "Lose":
        quote = quoteProFeld * Richtigefelder
        gewin = einsatz * quote
        input(f"[{farb3}+{zuruecksetzen}] : Du hast {gewin}$ Gewonnen")
        Geld += gewin
        return Geld, 1
    return Geld, 0

