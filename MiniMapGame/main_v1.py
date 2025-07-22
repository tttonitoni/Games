# Spiel mit einer Karte wo man sachen sammeln und Kämpfen kann

import pickle
import os

class game_charackter:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.map_level = 0
        self.curent_map = None
        self.life = 100
        self.inventar = [("/",0),("/",0),("/",0),("/",0),("/",0)]

    def print_curent_map(self):
        for row in self.curent_map:
            print(row)

class game_map:
    def __init__(self, map_name,spalten=0,zeilen=0):
        self.name = map_name
        self.matrix = [["+" for _ in range(spalten)] for _ in range(zeilen)]

    def print_map(self):
        for zeilen in self.matrix:
            print("|" + " ".join(zeilen) + "|" )

# Save/Load charakter
def speichere_charakter(neuer_charakter, dateiname="charaktere.pkl"):
    charakter_liste = []

    # ✅ Nur 1 Argument an os.path.exists
    if os.path.exists(dateiname):
        with open(dateiname, "rb") as f:
            if os.path.getsize(dateiname) > 0:
                charakter_liste = pickle.load(f)

    charakter_liste.append(neuer_charakter)

    with open(dateiname, "wb") as f:
        pickle.dump(charakter_liste, f)

    print(f"Charakter '{neuer_charakter.name}' gespeichert.")
def lade_charaktere(dateiname="charaktere.pkl"):
    if not os.path.exists(dateiname):
        print("Datei existiert nicht – leere Liste wird zurückgegeben.")
        return []

    if os.path.getsize(dateiname) == 0:
        print("Datei ist leer – leere Liste wird zurückgegeben.")
        return []

    with open(dateiname, "rb") as f:
        charakter_liste = pickle.load(f)

    print(f"{len(charakter_liste)} Charakter(e) geladen.")
    return charakter_liste


# Main Loops
def get_chrakter():
    while True:
        try:
            availeble_charakters = lade_charaktere()

            auswahl = input("Möchtest du eine Charakter erstellen(1) oder einen Charakter weiter Spielen(2)?")
            if auswahl == "1":
                name = input("Wie soll der Charakter heißen: ")
                if not any(c.name == name for c in availeble_charakters):
                    charakter = game_charackter(name)
                    speichere_charakter(charakter)
                    return charakter
                else:
                    print("Chrakter Name existirt schon")
            elif auswahl == "2":
                for n,c in enumerate(availeble_charakters):
                    print(f"{n}. {c.name}")
                n = int(input("Welchen Charakter möchtest du Spielen: "))
                charakter = availeble_charakters[n]    
                return charakter
        except:
            print("Fehler!!!")

def game_menu(charakter,maps):
    print("1. Shop")
    print("2. Level Spielen")
    inp = input(">>> ")

    if inp == "1":
        print("Shop")
    elif inp == "2":
        charakter.curent_map = maps[charakter.map_level]
        input(f"Level: {charakter.map_level} Name: {charakter.curent_map.name}")
        play_level(charakter)

def play_level(charakter):
    charakter.curent_map.print_map()

# Game Variablen
main = True
current_charakter = get_chrakter()
Maps = [
    game_map("First Level", spalten=5, zeilen=5)
]

while main:
    game_menu(current_charakter,Maps)