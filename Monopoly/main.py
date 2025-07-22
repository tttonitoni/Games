from funktionen import *
from spielbret import spielbrett, farbgruppen

# Variabel:
spielerlist = [] 
Geld = 1500

main = True
while main:
    print("------ Wilkomnen zu Monopoly ------")
    print("1 Spiel starten")
    print("2 Einstellungen")
    antwort = input(">>> ")

    if antwort == "2":
        Geld = Einstellungen()

    elif antwort == "1":

        # Spiler werden erstelt
        spieleranzahl = int(input("Wie viele Spielen?: "))
        for spieler in range(spieleranzahl):
            name = input(f"Wie heist spieler {spieler+1}: ")
            spielerlist.append(Spieler(name, Geld, 0))

        # Main Spiel loop
        Spielen = True
        while Spielen:
            for spieler in spielerlist:
                # Spielr Würfelt und ziht
                wüfelzahl = spieler.Würfeln() # Spieler Würfelt
                aktuellesFeld = spieler.ziehe(wüfelzahl,spielbrett) # Neues Feld wird wider gegeben als klasse

                # Feld typ wird überprüft und aktion wird ausgefürt :
                if aktuellesFeld.typ == "Straße" or aktuellesFeld.typ == "Bahnhof": #Wenn das Feld ein straße ist wird kann man es kaufen oder man musmiete zahlen
                    # Feld Kaufen oder Miete 
                    if aktuellesFeld.besitzer == None:
                        antwort = input(f"{spieler.name} : Willst du {aktuellesFeld.name} für {aktuellesFeld.preis}$ kaufen (j/n)")
                        if antwort == "j":
                            aktuellesFeld.kaufen(spieler, farbgruppen)
                    else:
                        if aktuellesFeld.besitzer.name == spieler.name:
                            print(f"{spieler.name} : {aktuellesFeld.name} gehört dir.")
                        else:
                            aktuellesFeld.MieteZahlen(spieler)

                # Spezial Karten werden überprüft : 
                elif aktuellesFeld.typ == "Spezial":
                    pass

                # Spieler Menu
                beendet = False
                while not beendet:
                    antwort = Spielermenu(spieler) # Menuprint und input

                    # Haeuserbauen
                    if antwort == "1":
                        # Kuck auf welchen straßen gebaut werden kann
                        for straße in spieler.straßen:
                            if straße.typ == "Straße":
                                straße.baucheck(spieler, farbgruppen)
                        Haeserbauen(spieler)

                    # Tauschen
                    elif antwort == "2":
                        pass

                    elif antwort == "3":
                        beendet = True


