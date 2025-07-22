import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines_count = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.visible = [['.' for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.generate_board()

    def generate_board(self):
        while len(self.mines) < self.mines_count:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r, c) not in self.mines:
                self.mines.add((r, c))
                self.board[r][c] = '*'

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != '*':
                    self.board[r][c] = str(self.count_adjacent_mines(r, c))

    def count_adjacent_mines(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.board[nr][nc] == '*':
                        count += 1
        return count

    def print_visible(self):
        print("\n   " + " ".join([str(i) for i in range(self.cols)]))
        for idx, row in enumerate(self.visible):
            print(f"{idx:2} " + " ".join(row))
        print()

    def reveal(self, row, col):
        if self.visible[row][col] != '.':
            return

        if self.board[row][col] == '*':
            self.visible[row][col] = '*'
            self.show_all_mines()
            self.print_visible()
            print("💥 Boom! Du bist auf eine Mine getreten.")
            exit()

        self._reveal_recursive(row, col)

    def _reveal_recursive(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        if self.visible[row][col] != '.':
            return

        self.visible[row][col] = self.board[row][col]
        if self.board[row][col] == '0':
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr != 0 or dc != 0:
                        self._reveal_recursive(row + dr, col + dc)

    def show_all_mines(self):
        for r, c in self.mines:
            self.visible[r][c] = '*'

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.visible[r][c] == '.' and self.board[r][c] != '*':
                    return False
        return True

def play_game():
    print("=== Minesweeper ===")
    rows = int(input("Anzahl der Reihen: "))
    cols = int(input("Anzahl der Spalten: "))
    mines = int(input("Anzahl der Minen: "))

    game = Minesweeper(rows, cols, mines)

    while True:
        game.print_visible()
        try:
            r = int(input("Zeile wählen: "))
            c = int(input("Spalte wählen: "))
            if not (0 <= r < rows and 0 <= c < cols):
                print("Ungültige Koordinaten.")
                continue
            game.reveal(r, c)
            if game.check_win():
                game.print_visible()
                print("🏆 Glückwunsch! Du hast alle Minen gefunden!")
                break
        except ValueError:
            print("Bitte gültige Zahlen eingeben.")
        except KeyboardInterrupt:
            print("\nSpiel beendet.")
            break

if __name__ == "__main__":
    play_game()
