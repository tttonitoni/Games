from funktionen import *
from spielbret import farbgruppen

spielbrett = [
    Feld("Los", "Start", preis=0),
    Feld("Badstraße", "Straße", "Braun", preis=60, miete=[2, 10, 30, 90, 160, 250], Hauskosten=50),
    Feld("Ereignisfeld", "Ereignis"),
    Feld("Turmstraße", "Straße", "Braun", preis=60, miete=[4, 20, 60, 180, 320, 450], Hauskosten=50),
    Feld("Einkommenssteuer", "Spezial", preis=200),
]

spieler = Spieler("Toni", geld=1500)
spieler2 = Spieler("Rosa", geld=1500)
for feld in spielbrett:
    if feld.typ == "Straße":
        feld.kaufen(spieler, farbgruppen)
    
print(spieler.farbgruppenBesitz)

for feld in spieler.straßen:
    feld.baucheck(spieler, farbgruppen)

for feld in spieler.straßen:
    print(f"{feld.name} : {feld.Hausbauen}")

spielbrett[3].MieteZahlen(spieler2)