class BankKonto:
    def __init__(self, guthaben=0):
        self.guthaben = guthaben

    def einzahlen(self, betrag):
        if betrag > 0:
            self.guthaben += betrag
        else:
            print("Ungültiger Betrag, muss positiv sein.")
    
    def abheben(self, betrag):
        if betrag > self.guthaben:
            print("Nicht genug Guthaben.")
        elif betrag < 0:
            print("Ungültiger Betrag, muss positiv sein.")
        else:
            self.guthaben -= betrag

    def kontostand(self):
        print(f"Sie haben {self.guthaben} Euro auf Ihrem Konto.")

    def menue(self):
        while True:
            print("\nWählen Sie eine Aktion:")
            print("1: Einzahlen")
            print("2: Kontostand anzeigen")
            print("3: Abheben")
            print("4: Beenden")
            
            try:
                wahl = int(input("Ihre Wahl: "))
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
                continue
            
            if wahl == 1:
                betrag = int(input("Wie viel möchten Sie einzahlen? "))
                self.einzahlen(betrag)
            elif wahl == 2:
                self.kontostand()
            elif wahl == 3:
                betrag = int(input("Wie viel möchten Sie abheben? "))
                self.abheben(betrag)
            elif wahl == 4:
                print("Programm beendet.")
                break
            else:
                print("Ungültige Auswahl, bitte erneut versuchen.")

# Hauptprogramm
konto = BankKonto()
konto.menue()
