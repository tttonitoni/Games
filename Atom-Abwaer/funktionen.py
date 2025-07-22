import time

def begrüßung():
    print("📞 *Ring* *Ring*")
    print("Verteidigungsministerium: Guten Tag, hier ist das Verteidigungsministerium. Wie kann ich Ihnen helfen?")
    time.sleep(2)
    print("Sie: 'Eine Atomrakete ist auf dem Weg nach Deutschland! Wir müssen sie abwehren!'")
    time.sleep(2)
    print("Ministerium: 'Verstanden! Wir brauchen einen Abwehrcode, um die Rakete zu stoppen.'")

def menü():
    print("\nWählen Sie ein Thema, um weitere Informationen zu erhalten:")
    print("1. Woher kommt die Bedrohung?")
    print("2. Wie funktioniert die Abwehranlage?")
    print("3. Gibt es Zugangscodes?")
    print("4. Code eingeben und die Bombe abwehren")
    return input("Geben Sie die Nummer Ihrer Auswahl ein: ")

def thema_1(code):
    print("\nMinisterium: 'Die Bedrohung kommt aus dem Osten, von einer abtrünnigen Gruppe.'")
    time.sleep(2)
    print("Sie: 'Haben wir den Standort bestätigt?'")
    time.sleep(2)
    print("Ministerium: 'Ja, der Standort ist bestätigt. Die zweite Ziffer des Codes ist: 4.'")
    code[1] = '4'

def thema_2(code):
    print("\nMinisterium: 'Die Abwehranlage besteht aus mehreren Schichten, die aktiviert werden müssen.'")
    time.sleep(2)
    print("Ministerium: 'Die dritte Ziffer des Codes lautet: 6.'")
    code[2] = '6'

def thema_3(code):
    print("\nMinisterium: 'Es gibt vier Ziffern im Abwehrcode, jede mit einer Information verknüpft.'")
    time.sleep(2)
    print("Ministerium: 'Die erste Ziffer lautet: 2, und die letzte Ziffer lautet: 8.'")
    code[0] = '2'
    code[3] = '8'

def code_eingeben(code):
    eingegebener_code = input("\nGeben Sie den Abwehrcode ein (vier Ziffern): ")
    richtiger_code = ''.join(code)
    if eingegebener_code == richtiger_code:
        print("\nMinisterium: 'Code korrekt! Die Rakete wurde abgewehrt. Deutschland ist gerettet!' 🎉")
    else:
        print("\nMinisterium: 'Falscher Code! Die Rakete hat ihr Ziel erreicht. Deutschland ist zerstört.' 💥")
