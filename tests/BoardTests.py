import unittest
import random
from src.Board import Board

class testCreateEmptyBoard(unittest.TestCase):
    def testNormalDimensions(self):
        expected_board = [[0] *10] *10
        observed_board = Board.create_empty_board(10, 10)
        self.assertEqual(expected_board, observed_board)

    def testSmallDimensions(self):
        expected_board = [[0]]
        observed_board = Board.create_empty_board(1, 1)
        self.assertEqual(expected_board, observed_board)

    def testDifferentDimensions(self):
        expected_board = [[0] *3] *4
        observed_board = Board.create_empty_board(3, 4)
        self.assertEqual(expected_board, observed_board)

class testPlaceBomb(unittest.TestCase):
    def testPlaceBomb(self):
        expected_board = [[0, -1], [0, 0]]
        test_board = Board(2,2)
        test_board.place_bomb(1, 0)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

    def testPlaceMultipleBombs(self):
        expected_board = [[0, -1], [-1, 0]]
        test_board = Board(2,2)
        test_board.place_bomb(1, 0)
        test_board.place_bomb(0, 1)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

class testScatterBombs(unittest.TestCase):
    def testNormalScatter(self):
        # Fake out the random number generator
        random.seed(0xDEADBEEF)
        expected_board = [[-1,0],[0,0]]
        test_board = Board(2,2)
        test_board.scatter_bombs(1, rand=random.random)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)


if __name__ == "__main__":
    unittest.main()