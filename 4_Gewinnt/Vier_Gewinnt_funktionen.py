# Funktionen

import os



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printlogo():
    logo = r"""
         _  _       ___                  _                _   
        | || |     / _ \  ___ __      __(_) _ __   _ __  | |_ 
        | || |_   / /_\/ / _ \\ \ /\ / /| || '_ \ | '_ \ | __|
        |__   _| / /_\\ |  __/ \ V  V / | || | | || | | || |_ 
           |_|   \____/  \___|  \_/\_/  |_||_| |_||_| |_| \__|                                                    
"""
    print(logo)

def PrintMenue():
    clear()
    printlogo()
    print("Wikommen zu 4 Gewinnt")
    print()
    print("1 = Spiel staren     2 = Beenden")
    print()


def PrintSpielfeld(defmatrix):
    print("      -------------")
    for row in defmatrix:
        prow = ' '.join(row)
        print("     |" + prow + "|")
    print("     |-------------|")
    print("      0 1 2 3 4 5 6")

def ValidInputInt(text):
    zahlinput = input(text)
    try:
        zahlinput = int(zahlinput)
        if zahlinput > 6:
            print("Die Spalte gibt es Nicht")
            return None, False
        else:
            return zahlinput, True
    except:
        print("Nur Zahlen")
        return None, False

def get_vertikal_row_list(defmatrix, player_row):
    vertikalrowlist = [None]*6
    for index in range(len(defmatrix)):
        vertikalrowlist[index] = defmatrix[index][player_row]
    return vertikalrowlist

def get_add_pos_in_matrix(vertikalrowlist,):
    for pos in range(len(vertikalrowlist)):
        if vertikalrowlist[pos] == 'O':
            return pos -1
        elif vertikalrowlist[pos] == 'X':
            return pos -1
    return pos


def check_winner(board, player):
    rows = 6
    cols = 7

    # Horizontal check
    for row in range(rows):
        for col in range(cols - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # Vertical check
    for row in range(rows - 3):
        for col in range(cols):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # Diagonal check (bottom-left to top-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

    # Diagonal check (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    return False


def vier_gewinnt():
            # game variabeln
        game_over = False
        runde = 0
        Spielfeld = [
            ['.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.'],
        ]

        clear()
        printlogo()
        PrintSpielfeld(Spielfeld)

        while not game_over:

            player = "X" if runde % 2 == 0 else "O"

            richtigerinput = False
            while not richtigerinput:
                player_row, ValidInputStatus = ValidInputInt(f"{player} wähle eine Spalte(0-6): ")
                if  ValidInputStatus == False:
                    continue

                vertikalrowlist = get_vertikal_row_list(Spielfeld, player_row)

                if '.' not in vertikalrowlist:
                    print("Die Reihe ist leider voll")
                else:
                    richtigerinput = True

            addpos = get_add_pos_in_matrix(vertikalrowlist)
            Spielfeld[addpos][player_row] = player
            runde += 1
            clear()
            printlogo()
            PrintSpielfeld(Spielfeld)

            if check_winner(Spielfeld, player):
                input(f"{player} hat Gewonnen")
                game_over = True
            