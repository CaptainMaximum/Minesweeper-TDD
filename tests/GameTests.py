import unittest
import random
from src.Game import Game
from src.Board import Board

class testCreateBoard(unittest.TestCase):
    def testCreate(self):
        random.seed(0xDEADBEEF)
        compare_board = Board(5, 5)
        compare_board.scatter_bombs(5, rand=random.random)
        random.seed(0xDEADBEEF)
        game = Game(5, 5, 5, testing=True)
        game.create_board(5, 5, 5, rand_func=random.random)
        expected_board = compare_board.board
        observed_board = game.board.board
        self.assertEqual(expected_board, observed_board)

class testWinSituation(unittest.TestCase):
    def testNotWin(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = False
        observed_value = game.is_win()
        self.assertEqual(expected_value, observed_value)

    def testWin(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = True
        game.hidden_cells = 1
        observed_value = game.is_win()
        self.assertEqual(expected_value, observed_value)

if __name__ == "__main__":
    unittest.main()