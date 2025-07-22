# To-Do-Listen-Tool
def zeige_aufgaben(todo_liste):
    print("\nAktuelle To-Do-Liste:")
    if not todo_liste:
        print("Keine Aufgaben vorhanden.")
    else:
        for i, (aufgabe, erledigt) in enumerate(todo_liste, start=1):
            status = "Erledigt" if erledigt else "Offen"
            print(f"{i}. {aufgabe} - {status}")
    print()

def aufgabe_hinzufuegen(todo_liste):
    neue_aufgabe = input("Gib eine neue Aufgabe ein: ")
    todo_liste.append((neue_aufgabe, False))
    print(f"Aufgabe '{neue_aufgabe}' hinzugefügt.\n")

def aufgabe_als_erledigt_markieren(todo_liste):
    aufgaben_nummer = int(input("Gib die Nummer der zu erledigenden Aufgabe ein: "))
    if 0 < aufgaben_nummer <= len(todo_liste):
        aufgabe, _ = todo_liste[aufgaben_nummer - 1]
        todo_liste[aufgaben_nummer - 1] = (aufgabe, True)
        print(f"Aufgabe '{aufgabe}' als erledigt markiert.\n")
    else:
        print("Ungültige Nummer.\n")

def aufgabe_loeschen(todo_liste):
    aufgaben_nummer = int(input("Gib die Nummer der zu löschenden Aufgabe ein: "))
    if 0 < aufgaben_nummer <= len(todo_liste):
        aufgabe, _ = todo_liste.pop(aufgaben_nummer - 1)
        print(f"Aufgabe '{aufgabe}' wurde gelöscht.\n")
    else:
        print("Ungültige Nummer.\n")

def todo_tool():
    todo_liste = []
    print("Willkommen zum To-Do-Listen-Tool!")
    
    while True:
        print("Optionen:")
        print("1 - Aufgaben anzeigen")
        print("2 - Aufgabe hinzufügen")
        print("3 - Aufgabe als erledigt markieren")
        print("4 - Aufgabe löschen")
        print("5 - Beenden")
        
        auswahl = input("Wähle eine Option: ")
        
        if auswahl == "1":
            zeige_aufgaben(todo_liste)
        elif auswahl == "2":
            aufgabe_hinzufuegen(todo_liste)
        elif auswahl == "3":
            aufgabe_als_erledigt_markieren(todo_liste)
        elif auswahl == "4":
            aufgabe_loeschen(todo_liste)
        elif auswahl == "5":
            print("Beenden...")
            break
        else:
            print("Ungültige Option. Bitte erneut versuchen.\n")

# Tool starten
todo_tool()
