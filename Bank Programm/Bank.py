# Bank Programm Geld
# Toni.T 2.10.24#

from funktionen import clear_console,PrintStarter,einzahl

# Varibalen
Guthaben = 0
main = True

# main loop
main = True
while main:
    PrintStarter()
    try:
        coice = int(input("Wählen sie eine auswahl (1-4): ")) 
    except ValueError:
         input("Ungülige Eingabe")
         continue

    if coice == 1:
        clear_console()
        try:
            geld = int(input("Was ist der Betrag den sie Hinzufügen wollen: "))
        except ValueError:
            print("Ungültige Eingabe...")
            continue

        if geld < 0 and abs(geld) > Guthaben:
            print("Nicht genug guthaben")
            input()
        else:
            Guthaben = einzahl(geld, Guthaben)
            input()

    elif coice == 2:
            clear_console()
            print(f"Sie haben ${Guthaben}")
            input("")

    elif coice == 4:
            main = False
    
    else:
         input("ungültige Eingabe... ")
