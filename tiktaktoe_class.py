class Board:
    def __init__(self):
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def make_move(self, player, row, col):
        if self.board[row][col] == '_':
            self.board[row][col] = player
            return True
        else:
            print("Invalid move, try again.")
            return False

    def check_winner(self, player):
        for row in self.board:
            if all(s == player for s in row):
                return True
        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(all(cell != '_' for cell in row) for row in self.board)
class abc:
    def __init__(instanz, value):
        instanz.value = 5

    def show_value(instanz):
        print(f"The Value is {instanz.vlaue}")




class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'O'

    def play_game(self):
        while True:
            self.board.print_board()
            try:
                row = int(input(f"Player {self.current_player}, enter the row (0, 1, 2): "))
                col = int(input(f"Player {self.current_player}, enter the column (0, 1, 2): "))
                if self.board.make_move(self.current_player, row, col):
                    if self.board.check_winner(self.current_player):
                        self.board.print_board()
                        print(f"Player {self.current_player} wins!")
                        break
                    elif self.board.check_draw():
                        self.board.print_board()
                        print("It's a draw!")
                        break
                    self.switch_player()
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 2.")



game = Game()
game.play_game()
