import random
import string

def passwort_generator():
    print("Willkommen zum Passwort-Generator!")
    
    try:
        laenge = int(input("Gib die gewünschte Länge des Passworts ein: "))
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")
        return
    
    if laenge < 6:
        print("Für die Sicherheit sollte das Passwort mindestens 6 Zeichen lang sein.")
        return

    # Zeichen, die im Passwort verwendet werden können
    zeichen = string.ascii_letters + string.digits + string.punctuation
    
    # Erstellen des Passworts
    passwort = ''.join(random.choice(zeichen) for i in range(laenge))
    print(f"Dein generiertes Passwort: {passwort}")

# Tool starten
passwort_generator()
