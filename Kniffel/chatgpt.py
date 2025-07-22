import tkinter as tk
import random

class ZahlenDuell:
    def __init__(self, root):
        self.root = root
        self.root.title("Zahlenduell – Spieler vs Bot")

        self.target = random.randint(1, 10)
        self.player_score = 0
        self.bot_score = 0
        self.history = []  # Merkt sich Zielzahlen

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Wähle eine Zahl (1–10)", font=("Arial", 14)).pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        for i in range(1, 11):
            tk.Button(self.buttons_frame, text=str(i), width=4, command=lambda n=i: self.play_round(n)).grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Spieler: 0 | Bot: 0", font=("Arial", 12, "bold"))
        self.score_label.pack()

        self.restart_button = tk.Button(self.root, text="Neustarten", command=self.restart_game, state=tk.DISABLED)
        self.restart_button.pack(pady=10)

    def bot_choice(self):
        if not self.history:
            return random.randint(1, 10)
        avg = sum(self.history) / len(self.history)
        if avg < 5:
            return random.randint(1, int(avg)+2)
        else:
            return random.randint(int(avg)-2, 10)

    def play_round(self, player_number):
        target = random.randint(1, 10)
        self.history.append(target)

        bot_number = self.bot_choice()
        player_diff = abs(player_number - target)
        bot_diff = abs(bot_number - target)

        msg = f"Zielzahl: {target}\nDu: {player_number} | Bot: {bot_number}\n"

        if player_diff < bot_diff:
            self.player_score += 1
            msg += "✅ Du bekommst einen Punkt!"
        elif bot_diff < player_diff:
            self.bot_score += 1
            msg += "🤖 Bot bekommt einen Punkt!"
        else:
            msg += "⚖️ Unentschieden!"

        self.result_label.config(text=msg)
        self.score_label.config(text=f"Spieler: {self.player_score} | Bot: {self.bot_score}")

        if self.player_score >= 30:
            self.result_label.config(text=msg + "\n🎉 Du hast gewonnen!")
            self.disable_buttons()
        elif self.bot_score >= 30:
            self.result_label.config(text=msg + "\n💀 Bot hat gewonnen!")
            self.disable_buttons()

    def disable_buttons(self):
        for widget in self.buttons_frame.winfo_children():
            widget.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)

    def restart_game(self):
        self.player_score = 0
        self.bot_score = 0
        self.history.clear()
        self.result_label.config(text="")
        self.score_label.config(text="Spieler: 0 | Bot: 0")
        for widget in self.buttons_frame.winfo_children():
            widget.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    app = ZahlenDuell(root)
    root.mainloop()
