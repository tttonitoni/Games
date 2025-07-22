import random 

class Feld:
    def __init__(self, name, typ, farbe=None, preis=0, miete=[0,0,0,0,0,0], Hauskosten=0):
        self.name = name
        self.typ = typ  # Typ des Feldes (z.B. Straße, Bahnhof, Ereignis)
        self.preis = preis
        self.farbe = farbe
        self.besitzer = None  # Besitzer des Feldes (anfangs niemand)
        self.mietelist = miete # Liste mit Mite
        self.Hauslevel = 0 # Legt die miete fest je nach haus
        self.Hauskosten = Hauskosten
        self.Hausbauen = False # legt fest ob man häuser kaufen darf

    def MieteZahlen(self, spieler):
        input(f"{spieler.name} : Du must {self.mietelist[self.Hauslevel]}$ miete an {self.besitzer.name} zahlen")
        self.besitzer.geld += self.mietelist[self.Hauslevel]
        spieler.geld -= self.mietelist[self.Hauslevel]
    
    def kaufen(self, spieler, farbgruppen):
        """Spieler kauft das Feld, wenn möglich."""
        if self.besitzer is None:  # Nur kaufen, wenn Feld frei
            if spieler.geld >= self.preis:  # Spieler hat genug Geld
                spieler.geld -= self.preis  # Geld abziehen
                self.besitzer = spieler  # Besitzer ändern
                spieler.straßen.append(self)  # Feld zu Spielerbesitz hinzufügen
                # Farbgruppen für hauser kaufen
                if self.farbe not in spieler.farbgruppenBesitz:
                    spieler.farbgruppenBesitz[self.farbe] = 1
                else:
                    spieler.farbgruppenBesitz[self.farbe] += 1

                print(f"{spieler.name} hat {self.name} für {self.preis}$ gekauft!")
            else:
                print(f"{spieler.name} hat nicht genug Geld, um {self.name} zu kaufen!")
        else:
            print(f"{self.name} gehört bereits {self.besitzer}.")

    def baucheck(self, spieler, farbgruppen):
        if spieler.farbgruppenBesitz[self.farbe] == len(farbgruppen[self.farbe]):
            self.Hausbauen = True

class Spieler:
    def __init__(self, name, geld, position=0):
        self.name = name
        self.geld = geld
        self.position = position
        self.straßen = []  # Liste der besessenen Felder
        self.farbgruppenBesitz = {} # Liste der anzahl von farben 

    def Würfeln(self):
        wüfelzahl = Würfeln() # zahl wird gewürfelt
        print("\n________________________________")
        print(f"{self.name} ist dran : {self.geld}$")
        input(f"{self.name} : Enter um zu Würfeln.")
        print(f"{self.name} : Hat eine {wüfelzahl} gewürfelt")
        return wüfelzahl

    def ziehe(self, schritte, brett):
        """Spieler zieht auf dem Spielfeld."""
        position = self.position
        self.position = (self.position + schritte) % len(brett)  # Spielfeld-Position berechnen

        # überprüft ob über los
        if position + schritte >= 41:
            print(f"Du bist über los und bekommst 200$")
            self.geld += 200

        feld = brett[self.position]
        print(f"{self.name} ist auf {feld.name} gelandet.")
        return feld
            
def finde_ziel(liste, ziel):
    """
    Sucht nach einem Ziel in einer Liste.

    Args:
        liste (list): Die Liste, in der gesucht wird.
        ziel: Das Ziel, das gefunden werden soll.

    Returns:
        int: Der Index des Ziels, falls es gefunden wurde.
        None: Wenn das Ziel nicht in der Liste ist.
    """
    for index, element in enumerate(liste):
        if element == ziel:
            return index  # Ziel gefunden, Index zurückgeben
    return None  # Ziel nicht gefunden


def Würfeln():
    zahl = random.randint(1,6)
    return zahl

def Spielermenu(spieler):
    print("______OPTIONEN_____")
    print("1. Häusbauen")
    print("2. Tauschen")
    print("3. Beenden")

    antwort = input(f"{spieler.name} : ")
    return antwort
    
def Haeserbauen(spieler):
    HausbauFelder = []
    RichtigeAntwort = False
    nummer = 1
    for straße in spieler.straßen:
        if straße.Hausbauen: # Wenn Hausbauen auf True ist 
            print(f"{nummer}.{straße.name} {straße.farbe} {straße.mietelist} 1 Haus : {straße.Hauskosten}")
            HausbauFelder.append(straße)
            nummer += 1
        
    if HausbauFelder:
        # Eine Richtige Zahl bekommen ohne crash
        while not RichtigeAntwort:
            antwort = input("Auf welchem Feld möchtest du ein Haus(Nummer): ")
            try:
                index = int(antwort)
                RichtigeAntwort = True
            except:
                if antwort == "Exit":
                    return
                print("Eine zahl oder Exit")
            
            straße = HausbauFelder[index-1] # Nimmt die ausgewählte straße speichert in straße
            spilerstraßen_index = finde_ziel(spieler.straßen, straße) # sucht die straße bei dem spiler und speicher den index
            zielstraße = spieler.straßen[spilerstraßen_index]

            if spieler.geld >= zielstraße.Hauskosten: # wenn man genug geld hat
                zielstraße.Hauslevel += 1 # Haus level hoch
                print(f"Du hast erforgreich ein Haus gebaut. Aktuelles level: {zielstraße.Hauslevel}")
            else:
                print("Nicht genug geld")
    else:
        print("Keine voll Farbgruppe!")

def Einstellungen():
    print("1 Start Geld ändern")

    antwort = input(">>> ")

    if antwort == "1":
        Geld = int(input("Start Geld = "))
        return Geld