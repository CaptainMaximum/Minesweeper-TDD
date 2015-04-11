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
        expected_board = [[1, -1], [1, 1]]
        test_board = Board(2,2)
        test_board.place_bomb(0, 1)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

    def testPlaceMultipleBombs(self):
        expected_board = [[2, -1], [-1, 2]]
        test_board = Board(2,2)
        test_board.place_bomb(1, 0)
        test_board.place_bomb(0, 1)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

class testScatterBombs(unittest.TestCase):
    def testNormalScatter(self):
        # Fake out the random number generator
        random.seed(0xDEADBEEF)
        expected_board = [[-1,1],[1,1]]
        test_board = Board(2,2)
        test_board.scatter_bombs(1, rand=random.random)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

    # Tests a scatter that should generate the same spot to place a bomb on.
    # What we want in this case is for scatter_bombs to skip over that position
    # and pick a new spot to place a bomb in
    def testDuplicateSpotScatter(self):
        random.seed(3)
        expected_board = [[2,-1],[-1,2]]
        test_board = Board(2,2)
        test_board.scatter_bombs(2, rand=random.random)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

class testRevealLocation(unittest.TestCase):
    def testSingleCellReveal(self):
        random.seed(0xDEADBEEF)
        expected_board = [[False, False], [True, False]]
        # board generated: [[-1,0], [0,0]]
        test_board = Board(2,2)
        test_board.scatter_bombs(1, rand=random.random)
        test_board.reveal_location(1,0)
        observed_board = test_board.trackboard
        self.assertEqual(expected_board, observed_board)

    def testMultiCellReveal(self):
        random.seed(6702)
        expected_board = [[True, True, False], [True, True, False], 
            [False, False, False]]
        test_board = Board(3,3)
        test_board.scatter_bombs(4, random.random)
        test_board.reveal_location(0,0)
        observed_board = test_board.trackboard
        self.assertEqual(expected_board, observed_board)
        
    def testFullBoardReveal(self):
        expected_board = [[True]*10]*10
        test_board = Board(10, 10)
        test_board.reveal_location(0,0)
        observed_board = test_board.trackboard
        assertEqual(expected_board, observed_board)

class testSumSurrounding(unittest.TestCase):
    def testLoneCell(self):
        expected_board = [[1,1,1],[1,0,1],[1,1,1]]
        test_board = Board(3,3)
        test_board.sum_surrounding(1,1)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

    def testCollidingSums(self):
        expected_board = [[0, 2, 0], [1, 2, 1], [0, 0, 0]]
        test_board = Board(3,3)
        test_board.sum_surrounding(0,0)
        test_board.sum_surrounding(0,2)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

if __name__ == "__main__":
    unittest.main()