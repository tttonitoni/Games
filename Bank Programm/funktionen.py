import os

def clear_console():
    if os.name == 'nt':  # Für Windows
        os.system('cls')
    else:  # Für Unix-basierte Systeme (Linux/Mac)
        os.system('clear')

def einzahl(defGeld, defGuthaben):
    defGuthaben += defGeld  # Add the amount to the global Guthaben
    return defGuthaben

def PrintStarter():
    clear_console()
    print("Bank of Deutschland")
    print("1 Geld einzahlen/auszahlen")
    print("2 Guthaben anzeigen")
    print("3 ")
    print("4 Beenden")

def validinpu():
    None