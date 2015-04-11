import unittest
from src.Board import Board

class testCreateEmptyBoard(unittest.TestCase):
    def testNormalDimensions():
        expected_board = [[0] *10] *10
        observed_board = Board.create_empty_board(10,10)
        unittest.assertEqual(expected_board, observed_board)

if __name__ == "__main__":
    unittest.main()