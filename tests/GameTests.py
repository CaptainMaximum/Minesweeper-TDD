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

    def testLosingCondition(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = False
        game.hidden_cells = -1
        observed_value = game.is_win()
        self.assertEqual(expected_value, observed_value)

class testLoseSituation(unittest.TestCase):
    def testNotLose(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = False
        observed_value = game.is_lose()
        self.assertEqual(expected_value, observed_value)

    def testLose(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = True
        game.hidden_cells = -1
        observed_value = game.is_lose()
        self.assertEqual(expected_value, observed_value)

class testMakeMove(unittest.TestCase):
    def testMoveOneReveal(self):
        random.seed(0xDEADBEEF)
        game = Game(5, 5, 5, testing=True)
        game.create_board(5, 5, 5, rand_func=random.random)
        expected_value = 24
        game.make_move(3, 0)
        observed_value = game.hidden_cells
        self.assertEqual(expected_value, observed_value)

    def testMoveMultiReveal(self):
        random.seed(0xDEADBEEF)
        game = Game(5, 5, 5, testing=True)
        game.create_board(5, 5, 5, rand_func=random.random)
        expected_value = 19
        game.make_move(4, 0)
        observed_value = game.hidden_cells
        self.assertEqual(expected_value, observed_value)

    def testMoveBombReveal(self):
        random.seed(0xDEADBEEF)
        game = Game(5, 5, 5, testing=True)
        game.create_board(5, 5, 5, rand_func=random.random)
        expected_value = -1
        game.make_move(2, 0)
        observed_value = game.hidden_cells
        self.assertEqual(expected_value, observed_value)

class testParseMove(unittest.TestCase):
    def testValidInput(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = (3, 3)
        observed_value = game.parse_move("3 3")
        self.assertEqual(expected_value, observed_value)

    def testValidInputWithExtraSpaces(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = (3, 3)
        observed_value = game.parse_move("3 \t 3")
        self.assertEqual(expected_value, observed_value)

    def testValidInputWithOutsideSpaces(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = (3, 3)
        observed_value = game.parse_move("\t3 3  ")
        self.assertEqual(expected_value, observed_value)



if __name__ == "__main__":
    unittest.main()