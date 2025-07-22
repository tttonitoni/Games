import random

# Initialisierung des Spielfelds
def create_board():
    return [[0 for _ in range(7)] for _ in range(6)]

# Spielfeld ausgeben
def print_board(board):
    for row in board:
        print(" | ".join(str(cell) for cell in row))
    print("-" * 29)

# Prüfen, ob ein Zug gültig ist
def is_valid_move(board, col):
    return board[0][col] == 0

# Zug ausführen
def make_move(board, col, piece):
    for row in reversed(board):
        if row[col] == 0:
            row[col] = piece
            return

# Prüfen auf Gewinnbedingung
def check_for_win(board, piece):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == piece:
                return True
    for row in range(rows - 3):
        for col in range(cols):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == piece:
                return True
    for row in range(rows - 3):
        for col in range(cols - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == piece:
                return True
    for row in range(3, rows):
        for col in range(cols - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == piece:
                return True
    return False

# Einfache KI-Logik
def get_ai_move(board, computer_piece, player_piece):
    rows, cols = len(board), len(board[0])

    # Gewinnzug für den Computer prüfen
    for col in range(cols):
        temp_board = [row[:] for row in board]
        if is_valid_move(temp_board, col):
            make_move(temp_board, col, computer_piece)
            if check_for_win(temp_board, computer_piece):
                return col

    # Blockiere den Spieler, wenn er im nächsten Zug gewinnen könnte
    for col in range(cols):
        temp_board = [row[:] for row in board]
        if is_valid_move(temp_board, col):
            make_move(temp_board, col, player_piece)
            if check_for_win(temp_board, player_piece):
                return col

    # Sonst eine zufällige Spalte wählen
    while True:
        col = random.randint(0, cols - 1)
        if is_valid_move(board, col):
            return col

# Hauptspiel-Funktion
def play_game(against_computer=False):
    board = create_board()
    game_over = False
    turn = 0  # 0 für Spieler 1, 1 für Spieler 2 oder Computer

    while not game_over:
        print_board(board)
        
        # Spielerauswahl
        if turn == 0:
            col = int(input("Spieler 1, wähle eine Spalte (0-6): "))
            piece = 1
        else:
            if against_computer:
                col = get_ai_move(board, 2, 1)
                print(f"Computer wählt Spalte {col}")
                piece = 2
            else:
                col = int(input("Spieler 2, wähle eine Spalte (0-6): "))
                piece = 2

        # Gültigen Zug ausführen
        if is_valid_move(board, col):
            make_move(board, col, piece)
            if check_for_win(board, piece):
                print_board(board)
                if against_computer and turn == 1:
                    print("Der Computer gewinnt!")
                else:
                    print(f"Spieler {piece} gewinnt!")
                game_over = True
            turn = (turn + 1) % 2
        else:
            print("Ungültiger Zug, bitte erneut versuchen.")

# Hauptmenü
def main():
    while True:
        mode = input("Wähle den Spielmodus: 1 - Spieler gegen Spieler, 2 - Spieler gegen Computer: ")
        if mode == '1':
            play_game(against_computer=False)
            break
        elif mode == '2':
            play_game(against_computer=True)
            break
        else:
            print("Ungültige Auswahl, bitte wähle 1 oder 2.")

main()