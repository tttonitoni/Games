import tkinter as tk
import random
import time
from functools import partial
from tkinter import messagebox

class Cell:
    def __init__(self):
        self.is_mine = False
        self.adjacent_mines = 0
        self.revealed = False
        self.flagged = False
        self.button = None

class MinesweeperGUI:
    def __init__(self, root, rows=10, cols=10, mines=10):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.total_mines = mines
        self.board = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.bot = None

        self.create_ui()
        self.place_mines()
        self.calculate_adjacent_mines()

        self.root.after(1000, self.start_bot)  # Start Bot nach 1 Sekunde

    def create_ui(self):
        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(self.root, width=3, height=1)
                btn.grid(row=r, column=c)
                btn.bind('<Button-1>', partial(self.left_click, r, c))
                btn.bind('<Button-3>', partial(self.right_click, r, c))
                self.board[r][c].button = btn

    def left_click(self, r, c, event=None):
        cell = self.board[r][c]
        if cell.flagged or cell.revealed:
            return
        self.reveal_cell(r, c)

    def right_click(self, r, c, event=None):
        self.toggle_flag(r, c)

    def toggle_flag(self, r, c):
        cell = self.board[r][c]
        if cell.revealed:
            return
        cell.flagged = not cell.flagged
        cell.button.config(text='🚩' if cell.flagged else '', fg='red')

    def place_mines(self):
        placed = 0
        while placed < self.total_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            cell = self.board[r][c]
            if not cell.is_mine:
                cell.is_mine = True
                placed += 1

    def calculate_adjacent_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c].is_mine:
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.board[nr][nc].is_mine:
                                count += 1
                self.board[r][c].adjacent_mines = count

    def reveal_cell(self, r, c):
        cell = self.board[r][c]
        if cell.revealed or cell.flagged:
            return
        cell.revealed = True
        btn = cell.button
        if cell.is_mine:
            btn.config(text='💣', bg='red')
            self.show_all_mines()
            print(f"💥 Bot hat eine Mine bei ({r}, {c}) getroffen. Game Over.")
            messagebox.showinfo("Game Over", "💥 Der Bot hat eine Mine getroffen!")
            self.root.quit()
        else:
            if cell.adjacent_mines > 0:
                btn.config(text=str(cell.adjacent_mines), relief=tk.SUNKEN, state=tk.DISABLED)
            else:
                btn.config(text="", relief=tk.SUNKEN, state=tk.DISABLED)
                self.reveal_adjacent(r, c)
            if self.check_win():
                self.show_all_mines()
                print("🏆 Der Bot hat gewonnen!")
                messagebox.showinfo("Sieg!", "🏆 Der Bot hat alle Minen umgangen!")
                self.root.quit()

    def reveal_adjacent(self, r, c):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if (dr == 0 and dc == 0) or not (0 <= nr < self.rows and 0 <= nc < self.cols):
                    continue
                self.reveal_cell(nr, nc)

    def show_all_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board[r][c]
                if cell.is_mine:
                    cell.button.config(text='💣', bg='gray')

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board[r][c]
                if not cell.revealed and not cell.is_mine:
                    return False
        return True

    def start_bot(self):
        self.bot = MinesweeperBot(self)
        self.bot.run()

class MinesweeperBot:
    def __init__(self, game):
        self.game = game
        self.rows = game.rows
        self.cols = game.cols

    def run(self):
        self.make_safe_first_move()

        while True:
            changed = self.think()
            if not changed:
                print("🤔 Keine sicheren Züge mehr. Bot versucht zu raten.")
                if not self.guess_move():
                    print("❌ Kein Feld mehr zum Raten. Bot beendet sich.")
                    break
            self.game.root.update()
            time.sleep(0.3)

    def make_safe_first_move(self):
        r, c = self.rows // 2, self.cols // 2
        print(f"🟢 Starte mit sicherem Erstzug auf ({r}, {c})")
        self.game.reveal_cell(r, c)
        self.game.root.update()
        time.sleep(0.5)

    def think(self):
        changed = False
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.game.board[r][c]
                if not cell.revealed or cell.adjacent_mines == 0:
                    continue

                neighbors = self.get_neighbors(r, c)
                hidden = [(nr, nc) for nr, nc in neighbors if not self.game.board[nr][nc].revealed and not self.game.board[nr][nc].flagged]
                flags = [(nr, nc) for nr, nc in neighbors if self.game.board[nr][nc].flagged]

                if len(hidden) > 0 and cell.adjacent_mines - len(flags) == len(hidden):
                    for nr, nc in hidden:
                        if not self.game.board[nr][nc].flagged:
                            print(f"🚩 Setze Flagge auf ({nr}, {nc})")
                            self.game.toggle_flag(nr, nc)
                            changed = True

                elif cell.adjacent_mines == len(flags) and len(hidden) > 0:
                    for nr, nc in hidden:
                        if not self.game.board[nr][nc].revealed and not self.game.board[nr][nc].flagged:
                            print(f"🟢 Decke sicheres Feld auf ({nr}, {nc})")
                            self.game.reveal_cell(nr, nc)
                            changed = True
        return changed

    def guess_move(self):
        candidates = []
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.game.board[r][c]
                if not cell.revealed and not cell.flagged:
                    candidates.append((r, c))

        if candidates:
            r, c = random.choice(candidates)
            print(f"🎲 Raten: Versuche Feld ({r}, {c})")
            self.game.reveal_cell(r, c)
            self.game.root.update()
            time.sleep(0.4)
            return True
        return False

    def get_neighbors(self, r, c):
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if (dr != 0 or dc != 0) and 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbors.append((nr, nc))
        return neighbors

if __name__ == "__main__":
    root = tk.Tk()
    root.title("🤖 Minesweeper Bot mit Ratefunktion")
    game = MinesweeperGUI(root, rows=10, cols=10, mines=10)
    root.mainloop()
