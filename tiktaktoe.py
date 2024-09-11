
board = [['_' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()



def check_winner(board, player):
    
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(all(cell != '_' for cell in row) for row in board)


def make_move(board, player, row, col):
    if board[row][col] == '_':
        board[row][col] = player
        return True
    else:
        print("Invalid move, try again.")
        return False


def play_game():
    current_player = 'X'
    while True:
        print_board(board)
        try:
           
            row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
           
            if make_move(board, current_player, row, col):
              
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
         
                elif check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
         
                current_player = 'O' if current_player == 'X' else 'X'
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 2.")


play_game()











