import random
import time
import threading
import os

# ANSI Escape Codes für Farben
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def spin_reel():
    symbols = ['🍋', '🍊', '🍉', '🍇', '🍓']
    return random.choice(symbols)

def display_reels(reels):
    print(' | '.join(reels))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("\n--- Slotmaschine Menü ---")
    print("1. Spiel starten")
    print("2. Einstellungen")
    print("3. Beenden")

def show_settings(auto_spin, bet_amount, balance):
    clear_screen()
    print("\n--- Einstellungen ---")
    print(f"Auto-Spinn: {'Aktiv' if auto_spin else 'Inaktiv'}")
    print(f"Einsatzbetrag: {bet_amount}€")
    print(f"Aktueller Kontostand: {balance}€")

def auto_spin_game(balance, bet_amount, stop_event):
    while balance > 0 and not stop_event.is_set():
        clear_screen()
        print(f"\nDein aktuelles Guthaben: {balance}€")
        
        # Drehe die Walzen
        reels = [spin_reel() for _ in range(3)]
        display_reels(reels)

        # Prüfe auf Gewinne
        if reels[0] == reels[1] == reels[2]:
            win_amount = bet_amount * 10
            print(f"{GREEN}Herzlichen Glückwunsch! Du hast {win_amount}€ gewonnen!{RESET}")
            balance += win_amount
            input("Drücke Enter, um fortzufahren...")
        else:
            print(f"{RED}Leider kein Gewinn.{RESET}")
            balance -= bet_amount  # Einsatzbetrag

        if balance <= 0:
            print("Du hast kein Guthaben mehr. Das Spiel endet.")
            break

        time.sleep(1)  # Warte 1 Sekunde zwischen den Spins

def auto_spin_game_continued(balance, bet_amount, stop_event):
    """
    Helper function to resume auto-spin after a win.
    """
    while balance > 0 and not stop_event.is_set():
        clear_screen()
        print(f"\nDein aktuelles Guthaben: {balance}€")

        # Drehe die Walzen
        reels = [spin_reel() for _ in range(3)]
        display_reels(reels)

        # Prüfe auf Gewinne
        if reels[0] == reels[1] == reels[2]:
            win_amount = bet_amount * 10
            print(f"{GREEN}Herzlichen Glückwunsch! Du hast {win_amount}€ gewonnen!{RESET}")
            balance += win_amount
            input("Drücke Enter, um fortzufahren...")
        else:
            print(f"{RED}Leider kein Gewinn.{RESET}")
            balance -= bet_amount  # Einsatzbetrag

        if balance <= 0:
            print("Du hast kein Guthaben mehr. Das Spiel endet.")
            break

        time.sleep(1)  # Warte 1 Sekunde zwischen den Spins

def main():
    print("Willkommen bei der Slotmaschine!")
    balance = 1000  # Startguthaben
    auto_spin = False
    bet_amount = 10

    while True:
        show_menu()
        choice = input("Wähle eine Option: ")

        if choice == '1':
            if auto_spin:
                print("Auto-Spinn ist aktiv. Bitte deaktiviere Auto-Spinn, bevor du das Spiel startest.")
            else:
                play_game = True
                while play_game and balance > 0:
                    clear_screen()
                    print(f"\nDein aktuelles Guthaben: {balance}€")

                    input("Drücke Enter, um die Walzen zu drehen...")

                    # Drehe die Walzen
                    reels = [spin_reel() for _ in range(3)]
                    display_reels(reels)

                    # Prüfe auf Gewinne
                    if reels[0] == reels[1] == reels[2]:
                        win_amount = bet_amount * 10
                        print(f"{GREEN}Herzlichen Glückwunsch! Du hast {win_amount}€ gewonnen!{RESET}")
                        balance += win_amount
                    else:
                        print(f"{RED}Leider kein Gewinn.{RESET}")
                        balance -= bet_amount  # Einsatzbetrag

                    # Warte auf Nutzereingabe, bevor der Bildschirm gelöscht wird
                    input("Drücke Enter, um fortzufahren...")

                    if balance <= 0:
                        print("Du hast kein Guthaben mehr. Das Spiel endet.")
                        break

                    if not auto_spin:
                        play_game = False

        elif choice == '2':
            while True:
                show_settings(auto_spin, bet_amount, balance)
                print("\nEinstellungen ändern:")
                print("1. Auto-Spinn umschalten")
                print("2. Einsatzbetrag ändern")
                print("3. Geld hinzufügen")
                print("4. Zurück zum Menü")

                setting_choice = input("Wähle eine Option: ")

                if setting_choice == '1':
                    auto_spin = not auto_spin
                    if auto_spin:
                        stop_event = threading.Event()
                        auto_spin_thread = threading.Thread(target=auto_spin_game, args=(balance, bet_amount, stop_event))
                        auto_spin_thread.start()
                        input("Auto-Spinn läuft. Drücke Enter, um zurück zum Menü zu gelangen.")
                        stop_event.set()
                        auto_spin_thread.join()
                    else:
                        print("Auto-Spinn wurde deaktiviert.")
                elif setting_choice == '2':
                    try:
                        new_bet_amount = int(input("Neuen Einsatzbetrag eingeben: "))
                        if new_bet_amount <= 0:
                            print("Der Einsatzbetrag muss positiv sein.")
                        else:
                            bet_amount = new_bet_amount
                    except ValueError:
                        print("Ungültiger Betrag. Bitte eine Zahl eingeben.")
                elif setting_choice == '3':
                    try:
                        additional_amount = int(input("Betrag hinzufügen: "))
                        if additional_amount <= 0:
                            print("Der hinzuzufügende Betrag muss positiv sein.")
                        else:
                            balance += additional_amount
                    except ValueError:
                        print("Ungültiger Betrag. Bitte eine Zahl eingeben.")
                elif setting_choice == '4':
                    break
                else:
                    print("Ungültige Auswahl. Bitte versuche es erneut.")

        elif choice == '3':
            print("Das Spiel wird beendet. Danke fürs Spielen!")
            break

        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()