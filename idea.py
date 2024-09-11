def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Überprüft Zeilen
    for row in board:
        if all(s == player for s in row):
            return True
    # Überprüft Spalten
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Überprüft Diagonalen
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Spieler {current_player}, wähle eine Zeile (0, 1, 2): "))
            col = int(input(f"Spieler {current_player}, wähle eine Spalte (0, 1, 2): "))
            if board[row][col] != " ":
                print("Dieses Feld ist bereits belegt. Wähle ein anderes.")
                continue
            board[row][col] = current_player
        except (ValueError, IndexError):
            print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 0 und 2 ein.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Spieler {current_player} gewinnt!")
            break
        if is_draw(board):
            print_board(board)
            print("Das Spiel endet unentschieden!")
            break
        
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
