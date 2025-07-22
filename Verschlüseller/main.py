# verschlüsselungs programm von bustaben
# Toni.T 26.10.24

from funktionen import verschlüseler, entverschlüseler, print_menu, clear,logo

main = True

while main:
    clear()
    print_menu()
    coice = input("-\> ")
    if coice == "1":
        clear()
        logo()
        text = input("Was wollen sie verschlüsseln: ")
        # text wird in liste umgewandelt
        text = list(text)
        # text geh in verschlüseler
        verschlüselter_text = verschlüseler(text)

        with open(r"ausgabe\verschüselt.txt", "w") as file:
            file.write("".join(verschlüselter_text))

        input("Text wurde verschlüselt")
    
    if coice == "2":
        clear()
        logo()
        text = input("Was wollen sie entverschlüsseln: ")
        # text wird in liste umgewandelt
        text = list(text)
        # text geh in entverschlüseler
        entschlüselter_text = entverschlüseler(text)

        with open(r"ausgabe\entschlüselt.txt", "w") as file:
            file.write("".join(entschlüselter_text))      

        input("Text wurde entverschlüselt")