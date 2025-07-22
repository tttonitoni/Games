from funktionen import begrüßung, menü, thema_1, thema_2, thema_3, code_eingeben

def spiel():
    code = ['_'] * 4  # Platzhalter für den vierstelligen Code
    begrüßung()
    while True:
        wahl = menü()
        if wahl == "1":
            thema_1(code)
        elif wahl == "2":
            thema_2(code)
        elif wahl == "3":
            thema_3(code)
        elif wahl == "4":
            if '_' in code:
                print("\nMinisterium: 'Sie haben noch nicht alle Ziffern des Codes! Sprechen Sie weiter mit uns, um alle Ziffern zu erfahren.'")
            else:
                code_eingeben(code)
                break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie erneut.")

spiel()