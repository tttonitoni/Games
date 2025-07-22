import tkinter as tk
from tkinter import messagebox
import random

# 🎰 Mini-Casino GUI
class MiniCasinoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Mini-Python-Casino")
        self.balance = 100

        self.create_main_ui()

    def create_main_ui(self):
        self.balance_label = tk.Label(self.root, text=f"Guthaben: {self.balance}€", font=("Arial", 16))
        self.balance_label.pack(pady=10)

        tk.Button(self.root, text="🎰 Slotmaschine", width=20, command=self.play_slots).pack(pady=5)
        tk.Button(self.root, text="🎲 Würfelspiel", width=20, command=self.play_dice).pack(pady=5)
        tk.Button(self.root, text="🃏 Blackjack", width=20, command=self.play_blackjack).pack(pady=5)
        tk.Button(self.root, text="💳 Guthaben +50€", width=20, command=self.add_balance).pack(pady=5)
        tk.Button(self.root, text="🚪 Verlassen", width=20, command=self.root.quit).pack(pady=10)

    def update_balance(self):
        self.balance_label.config(text=f"Guthaben: {self.balance}€")

    def add_balance(self):
        self.balance += 50
        self.update_balance()
        messagebox.showinfo("Aufgeladen", "Guthaben wurde um 50€ erhöht!")

    def play_slots(self):
        cost = 10
        if self.balance < cost:
            messagebox.showwarning("Nicht genug!", "Du brauchst mindestens 10€.")
            return

        self.balance -= cost
        symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
        result = [random.choice(symbols) for _ in range(3)]

        result_text = " | ".join(result)
        win = 0

        if result.count(result[0]) == 3:
            win = 100
            message = "💥 JACKPOT! Drei Gleiche!"
        elif len(set(result)) == 2:
            win = 30
            message = "✨ Zwei Gleiche! Gut gemacht!"
        else:
            message = "😢 Leider verloren."

        self.balance += win
        self.update_balance()
        messagebox.showinfo("Slotmaschine", f"{result_text}\n\n{message}\nGewinn: {win}€")

    def play_dice(self):
        cost = 5
        if self.balance < cost:
            messagebox.showwarning("Nicht genug!", "Du brauchst mindestens 5€.")
            return

        self.balance -= cost
        current = random.randint(1, 6)
        guess = tk.simpledialog.askstring("Würfelspiel", f"Aktuelle Zahl: {current}\nWird die nächste höher (h) oder niedriger (n)?")

        if not guess or guess.lower() not in ['h', 'n']:
            self.balance += cost
            return

        next_roll = random.randint(1, 6)
        result_msg = f"Zahl war: {next_roll}\n"

        if (guess == 'h' and next_roll > current) or (guess == 'n' and next_roll < current):
            win = 15
            self.balance += win
            result_msg += f"✅ Richtig geraten! Gewinn: {win}€"
        elif next_roll == current:
            self.balance += cost
            result_msg += "⚖️ Gleichstand! Einsatz zurück."
        else:
            result_msg += "❌ Falsch geraten. Verlust."

        self.update_balance()
        messagebox.showinfo("Würfelspiel", result_msg)

    def play_blackjack(self):
        cost = 15
        if self.balance < cost:
            messagebox.showwarning("Nicht genug!", "Du brauchst mindestens 15€.")
            return

        self.balance -= cost
        self.update_balance()

        def draw_card(): return random.randint(2, 11)

        player = draw_card() + draw_card()
        dealer = draw_card() + draw_card()

        while player < 21:
            hit = messagebox.askyesno("Blackjack", f"Deine Summe: {player}\nNoch eine Karte ziehen?")
            if hit:
                player += draw_card()
            else:
                break

        result = ""
        if player > 21:
            result = f"💥 BUST! Deine Summe: {player}\nVerloren!"
        else:
            while dealer < 17:
                dealer += draw_card()
            if dealer > 21 or player > dealer:
                win = 40
                self.balance += win
                result = f"🏆 Gewonnen!\nDeine: {player} | Dealer: {dealer}\n+{win}€"
            elif player == dealer:
                self.balance += cost
                result = f"⚖️ Unentschieden.\nBeide: {player}\nEinsatz zurück."
            else:
                result = f"❌ Dealer gewinnt.\nDeine: {player} | Dealer: {dealer}"

        self.update_balance()
        messagebox.showinfo("Blackjack Ergebnis", result)


# 🏁 Start der App
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniCasinoApp(root)
    root.mainloop()
