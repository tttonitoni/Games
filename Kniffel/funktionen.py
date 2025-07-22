import random, os

class spieler:
    def __init__(self, name):
        self.name = name
        self.optinlist = ["1er","2er","3er","4er","5er","6er","dreier pash", "viererpash, full house", "kleine straße","große straße", "kniffel", "chance"]
        self.karte = {
            "1er": "",
            "2er": "",
            "3er": "",
            "4er": "",
            "5er": "",
            "6er": "",
            "Dreier Pash": "",
            "Vierer Pash": "",
            "Full House": "",
            "Kleine Straße": "",
            "Große Straße": "",
            "Kniffel": "",
            "Chance": "",
        }

    def printkarte(self):
        for Objekt in self.karte:
            print(f"{Objekt}: {self.karte[Objekt]}")
    
    def addToKarte(self, zahlen):
        zahltyp = None
        ergebnis = 0

        clear_console()
        self.printkarte()
        print(zahlen)

        Valid = False
        while not Valid:
            # Input
            auswahl = input("Welche option? ")

            if auswahl == "1er" or auswahl == "1":
                auswahl = "1er"
                zahltyp = 1
            elif auswahl == "2er" or auswahl == "2":
                auswahl = "2er"
                zahltyp = 2
            elif auswahl == "3er" or auswahl == "3":
                auswahl = "3er"
                zahltyp = 3
            elif auswahl == "4er" or auswahl == "4":
                auswahl = "4er"
                zahltyp = 4
            elif auswahl == "5er" or auswahl == "5":
                auswahl = "5er"
                zahltyp = 5
            elif auswahl == "6er" or auswahl == "6":
                auswahl = "6er"
                zahltyp = 6
            elif auswahl == "7":
                zahlntyp = input("Welchen dreier Pasc")
            
            # Kuck ob schon was da ist
            if self.karte[auswahl] == "":
                for zahl in zahlen:
                    if zahl == zahltyp:
                        ergebnis += zahltyp
                self.karte[auswahl] = str(ergebnis)
            
            Valid = True
        
        self.printkarte()


def clear_console():
    os.system('cls')

def Validint(text):
    while True:
        inp = input(text)
        try:
            inte = int(inp)
            return inte
        except:
            print("Eine zahl")

def CheckInt(zahl):
    try:
        intZahl = int(zahl)
        return True
    except:
        print("Keine zahl eingegeben")
        return False


def Würfeln():
    Valid = True
    zahlen = []
    safelist = []
    zahlencopy = []
    
    for runde in range(3):
        for index in range(5 - len(zahlen)):
            zahl = random.randint(1,6)
            zahlen.append(zahl)

        if runde == 2:
            return zahlen
        
        zahlencopy = list(zahlen)
        ValidSafe = False
        while not ValidSafe:
            print(zahlen)
            safe = input("Welche Zahlen möchtest du behalten? ")

            # safe zahlen als intager
            for zahl in safe:
                Int = CheckInt(zahl)
                if Int:
                    if int(zahl) in zahlencopy:
                        safelist.append(int(zahl))
                        zahlencopy.remove(int(zahl))
                    else:
                        print("Keine Valid Input.")
                        Valid = False
                        break
            
            if Valid:
                zahlen = safelist
                ValidSafe = True