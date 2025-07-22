import random
import time
import os

# 🧼 Terminal clear für bessere Optik
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 💸 Startguthaben
balance = 100

def print_balance():
    print(f"\n💰 Aktuelles Guthaben: {balance}€\n")

def slot_machine():
    global balance
    cost = 10
    symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
    print("\n🎰 Willkommen an der Slotmaschine!")
    if balance < cost:
        print("Nicht genug Guthaben!")
        return

    balance -= cost
    print("Ziehen...")

    time.sleep(1)
    reel = [random.choice(symbols) for _ in range(3)]
    print(" | ".join(reel))

    if reel.count(reel[0]) == 3:
        win = 100
        print("💥 JACKPOT! Drei Gleiche!")
    elif len(set(reel)) == 2:
        win = 30
        print("✨ Zwei Gleiche! Gut gemacht!")
    else:
        win = 0
        print("😢 Leider verloren.")

    balance += win
    print(f"💵 Gewinn: {win}€")

def dice_game():
    global balance
    cost = 5
    print("\n🎲 Höher oder Niedriger?")
    if balance < cost:
        print("Nicht genug Guthaben!")
        return

    balance -= cost
    current = random.randint(1, 6)
    print(f"🟢 Aktuelle Zahl: {current}")

    choice = input("Wird die nächste Zahl höher (h) oder niedriger (n)? ").lower()
    next_roll = random.randint(1, 6)
    print(f"🔴 Nächste Zahl: {next_roll}")

    if (choice == 'h' and next_roll > current) or (choice == 'n' and next_roll < current):
        win = 15
        print("✅ Richtig geraten!")
        balance += win
        print(f"💵 Gewinn: {win}€")
    elif next_roll == current:
        print("⚖️ Gleichstand. Kein Gewinn, kein Verlust.")
        balance += cost  # zurückzahlen
    else:
        print("❌ Falsch geraten. Einsatz verloren.")

def blackjack():
    global balance
    cost = 15
    print("\n🃏 Blackjack Light")
    if balance < cost:
        print("Nicht genug Guthaben!")
        return

    balance -= cost

    def draw_card():
        return random.randint(2, 11)

    player = draw_card() + draw_card()
    dealer = draw_card() + draw_card()

    print(f"🧑 Deine Karten: {player}")
    while player < 21:
        choice = input("Noch eine Karte? (j/n): ").lower()
        if choice == 'j':
            card = draw_card()
            print(f"➡️ Gezogene Karte: {card}")
            player += card
            print(f"🧑 Neue Summe: {player}")
        else:
            break

    if player > 21:
        print("💥 BUST! Über 21.")
        return

    print(f"🤖 Dealer hat: {dealer}")
    while dealer < 17:
        dealer += draw_card()
        print(f"Dealer zieht... Neue Summe: {dealer}")
        time.sleep(1)

    if dealer > 21 or player > dealer:
        win = 40
        print("🏆 Gewonnen!")
        balance += win
        print(f"💵 Gewinn: {win}€")
    elif player == dealer:
        print("⚖️ Unentschieden. Einsatz zurück.")
        balance += cost
    else:
        print("❌ Verloren.")

def casino_menu():
    while True:
        print("\n🎰 Willkommen im Python-Mini-Casino 🎰")
        print_balance()
        print("1. Slotmaschine")
        print("2. Würfelspiel")
        print("3. Blackjack")
        print("4. Guthaben aufladen (+50€)")
        print("5. Verlassen")

        choice = input("Wähle dein Spiel: ")

        clear()

        if choice == '1':
            slot_machine()
        elif choice == '2':
            dice_game()
        elif choice == '3':
            blackjack()
        elif choice == '4':
            global balance
            balance += 50
            print("💳 Guthaben wurde aufgeladen.")
        elif choice == '5':
            print("🎉 Danke fürs Spielen! Bis zum nächsten Mal.")
            break
        else:
            print("❗ Ungültige Eingabe.")

        input("\n🔁 Drücke Enter für das Menü...")
        clear()

# 🚀 Starte das Casino
casino_menu()
