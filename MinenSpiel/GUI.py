import tkinter as tk
import random
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
        self.board = []
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.reset_button = tk.Button(root, text="🔄 Neues Spiel", command=self.reset_game)
        self.reset_button.pack(pady=5)
        self.init_board()

    def init_board(self):
        self.board = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]

        for widget in self.frame.winfo_children():
            widget.destroy()

        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(self.frame, width=3, height=1)
                btn.grid(row=r, column=c)
                btn.bind('<Button-1>', partial(self.left_click, r, c))
                btn.bind('<Button-3>', partial(self.right_click, r, c))
                self.board[r][c].button = btn

        self.place_mines()
        self.calculate_adjacent_mines()

    def reset_game(self):
        print("\n🔁 Spiel wird zurückgesetzt...\n")
        self.init_board()

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
            #messagebox.showinfo("Game Over", f"💥 Du hast eine Mine bei ({r},{c}) getroffen!")
        else:
            if cell.adjacent_mines > 0:
                btn.config(text=str(cell.adjacent_mines), relief=tk.SUNKEN, state=tk.DISABLED)
            else:
                btn.config(text="", relief=tk.SUNKEN, state=tk.DISABLED)
                self.reveal_adjacent(r, c)
            if self.check_win():
                self.show_all_mines()
                messagebox.showinfo("Sieg!", "🏆 Du hast alle Minen vermieden!")

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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("🧨 Minesweeper – Manuell & Resetfähig")
    game = MinesweeperGUI(root, rows=10, cols=10, mines=10)
    root.mainloop()
