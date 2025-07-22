import time, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    clear()
    text = """
     ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
    ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
    print(text)
 
main = True
zeit = 0

while main:
    logo()
    print("Entschlüselter Text")
    # Datei öffnen und lesen
    with open(r"ausgabe\entschlüselt.txt", "r") as file:
        inhalt = file.read()
        if not inhalt:  # prüft, ob die Datei leer ist
            print("Die Datei ist leer.")
        else:
            print(inhalt)
    time.sleep(1)