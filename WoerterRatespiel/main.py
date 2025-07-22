from funktion import *

# Game Variabeln
woerter_liste = [
    "Haus", "Schule", "Computer", "Baum", "Tisch", "Auto", "Fahrrad", "Straße",
    "Hund", "Katze", "Vogel", "Blume", "Sonne", "Mond", "Stern", "Wolke",
    "Buch", "Lampe", "Fenster", "Tür", "Brille", "Uhr", "Stuhl", "Hose",
    "Jacke", "Schwimmbad", "Freund", "Reise", "Kamera", "Flugzeug", "Fernseher",
    "Abenteuer", "Bibliothek", "Schmetterling", "Zahnarzt", "Schlüssel", "Schreibtisch",
    "Einkaufszentrum", "Wissenschaft", "Naturkatastrophe", "Fußball", "Regenschirm",
    "Schneeflocke", "Löwenzahn", "Glühbirne", "Mikrowelle", "Erinnerung", "Wasserfall",
    "Friedensvertrag", "Jahreszeit", "Landschaft", "Gewitter"
]


# Mainloop
main= True
while main:
    # Menu
    MenuPrint()
    menu_input = input("> ")
    if menu_input == "1":

        randomWort = getRandomWort(woerter_liste)
        WoeterRatespil(randomWort)

# Test