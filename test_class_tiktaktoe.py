import unittest
from class_tiktaktoe import Board, Game

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_make_move_valid(self):
        self.assertTrue(self.board.make_move('X', 0, 0))
        self.assertEqual(self.board.board[0][0], 'X')
        

    def test_make_move_invalid(self):
        self.board.make_move('X', 0, 0)       
        self.assertFalse(self.board.make_move('O', 0, 0))  
        self.assertEqual(self.board.board[0][0], 'X')

    def test_check_winner_row(self):
        self.board.make_move('X', 0, 0)
        self.board.make_move('X', 0, 1)
        self.board.make_move('X', 0, 2)
        self.assertTrue(self.board.check_winner('X'))

    def test_check_winner_row(self):
        self.board.make_move('O', 0, 0)
        self.board.make_move('O', 1, 0)
        self.board.make_move('O', 2, 0)
        self.assertTrue(self.board.check_winner('O'))


    def test_check_winner_diagonal(self):
        self.board.make_move('X', 0, 0)
        self.board.make_move('X', 1, 1)
        self.board.make_move('X', 2, 2)
        self.assertTrue(self.board.check_winner('X'))

    def test_check_draw(self):
        moves = [
            ('X', 0, 0), ('O', 0, 1), ('X', 0, 2),
            ('O', 1, 0), ('X', 1, 1), ('O', 1, 2),
            ('O', 2, 0), ('X', 2, 1), ('O', 2, 2)
        ]
        for player, row, col in moves:
            self.board.make_move(player, row, col)
        self.assertTrue(self.board.check_draw())
        self.assertFalse(self.board.check_winner('X'))
        self.assertFalse(self.board.check_winner('O'))


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')


if __name__ == '__main__':
    unittest.main()


