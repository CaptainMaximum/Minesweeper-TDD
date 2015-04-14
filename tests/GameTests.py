import unittest
import random
from src.Game import Game
from src.Board import Board
from src.Exceptions import InvalidBoardException

class testCreateBoard(unittest.TestCase):
    # Compares a board generated from the Board class directly with the board
    # created from the Game.create_board method
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

    # Test to ensure that the number of bombs placed is less than the number of
    # available cells.  If there were more, we would not be able to place all
    # of them and would have an infinite loop!
    # If we do specify too many bombs, we should raise an exception
    def testCreateTooManyBombs(self):
        # dummy_game is needed here because Game.__init__ needs an instance of
        # 'Game' passed in as the first argument
        dummy_game = Game(5, 5, 0, testing=True)
        self.assertRaises(InvalidBoardException, Game.__init__, *[dummy_game, 2, 2, 5, True])

# These tests test Game.is_win with winning, mid-game, and losing conditions
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

# These tests test Game.is_lose with mid-game and losing conditions
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

# These tests test Game.make_move to ensure that the game counter gets
# decremented correctly (it should match up with the board's counter
# of cells left to pick)
class testMakeMove(unittest.TestCase):
    def testMoveOneReveal(self):
        random.seed(0xDEADBEEF)
        game = Game(5, 5, 5, testing=True)
        game.create_board(5, 5, 5, rand_func=random.random)
        expected_value = 24
        game.make_move(0, 3)
        observed_value = game.hidden_cells
        self.assertEqual(expected_value, observed_value)

    def testMoveMultiReveal(self):
        random.seed(0xDEADBEEF)
        game = Game(5, 5, 5, testing=True)
        game.create_board(5, 5, 5, rand_func=random.random)
        expected_value = 19
        game.make_move(0, 4)
        observed_value = game.hidden_cells
        self.assertEqual(expected_value, observed_value)

    def testMoveBombReveal(self):
        random.seed(0xDEADBEEF)
        game = Game(5, 5, 5, testing=True)
        game.create_board(5, 5, 5, rand_func=random.random)
        expected_value = -1
        game.make_move(0, 2)
        observed_value = game.hidden_cells
        self.assertEqual(expected_value, observed_value)

# These tests test user input to ensure that it is valid (user input should
# match the regular expression "\s+[0-9]+\s+[0-9]+\s+", where \s is any 
# whitespace character)
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

    def testInvalidInputTooFewArguments(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = None
        observed_value = game.parse_move("3")
        self.assertEqual(expected_value, observed_value)

    def testInvalidInputTooManyArguments(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = None
        observed_value = game.parse_move("3 3 3")
        self.assertEqual(expected_value, observed_value)

    def testInvalidInputNotIntegers(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = None
        observed_value = game.parse_move("Not Numbers")
        self.assertEqual(expected_value, observed_value)

    def testInvalidInputOutOfBounds(self):
        game = Game(5, 5, 5, testing=True)
        expected_value = None
        observed_value = game.parse_move("20 -1")
        self.assertEqual(expected_value, observed_value)

# These tests test the Game.run to ensure it returns the correct exit value
# when game-ending conditions are present (the loop isn't actually run)
class testRun(unittest.TestCase):
    def testRunWin(self):
        game = Game(5, 5, 5, testing=True)
        game.hidden_cells = 5
        expected_value = True
        observed_value = game.run()
        self.assertEqual(expected_value, observed_value)

    def testRunLose(self):
        game = Game(5, 5, 5, testing=True)
        game.hidden_cells = -1
        expected_value = False
        observed_value = game.run()
        self.assertEqual(expected_value, observed_value)


if __name__ == "__main__":
    unittest.main()