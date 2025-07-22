from funktionen import *

Spielerliste = []

# Spieler erstellen
anzahlSpieler = Validint("Wie viele Spielen? ")
for i in range(anzahlSpieler):
    name = input(f"Wie heist Spieler {i+1}: ")
    Spielerliste.append(spieler(name))

Spielen = True
while Spielen:
    for Spieler in Spielerliste:
        Spieler.printkarte()
        input(f"{Spieler.name} ist dran. \nEnter um zu Würfeln...")
        zahlen = Würfeln()
        
        Spieler.addToKarte(zahlen)
        




