import unittest
import random
from src.Board import Board

class testCreateEmptyBoard(unittest.TestCase):
    # Tests creating a board with dimensions that would be expected in a 
    # normal game
    def testNormalDimensions(self):
        expected_board = [[0] *10] *10
        observed_board = Board.create_empty_board(10, 10)
        self.assertEqual(expected_board, observed_board)

    # Tests creating a board that is much smaller than would be expected in a 
    # normal game
    def testSmallDimensions(self):
        expected_board = [[0]]
        observed_board = Board.create_empty_board(1, 1)
        self.assertEqual(expected_board, observed_board)

    # Tests creating a board with unequal x and y dimensions
    def testDifferentDimensions(self):
        expected_board = [[0] *3] *4
        observed_board = Board.create_empty_board(3, 4)
        self.assertEqual(expected_board, observed_board)

class testPlaceBomb(unittest.TestCase):
    # Tests the case of placing a single bomb on a board
    def testPlaceBomb(self):
        expected_board = [[1, 1], [-1, 1]]
        test_board = Board(2,2)
        test_board.place_bomb(0, 1)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

    # Tests the case of placing multiple bombs on a board
    def testPlaceMultipleBombs(self):
        expected_board = [[2, -1], [-1, 2]]
        test_board = Board(2,2)
        test_board.place_bomb(1, 0)
        test_board.place_bomb(0, 1)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

    # Tests placing a bomb on a board with different dimensions
    def testPlaceBombDifferentDimensionBoard(self):
        expected_board = [[0, 1, -1], [0, 1, 1]]
        test_board = Board(3, 2)
        test_board.place_bomb(2, 0)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

class testScatterBombs(unittest.TestCase):
    # Tests scattering a single bomb onto the board
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

# These tests compare expected & observed behavior of the board used to track
# what cells have been revealed in the game
class testRevealLocation(unittest.TestCase):
    # Tests a move that would only reveal a single location on the board
    # (i.e. on a bomb or on a cell adjacent to one)
    def testSingleCellReveal(self):
        random.seed(0xDEADBEEF)
        expected_board = [[False, True], [False, False]]
        test_board = Board(2,2)
        test_board.scatter_bombs(1, rand=random.random)
        test_board.reveal_location(1,0)
        observed_board = test_board.trackboard
        self.assertEqual(expected_board, observed_board)

    # Tests a move that would cascade and reveal multiple locations at once
    # (i.e. not next to or on a bomb)
    def testMultiCellReveal(self):
        random.seed(6702)
        expected_board = [[True, True, False], [True, True, False], 
            [False, False, False]]
        test_board = Board(3,3)
        test_board.scatter_bombs(4, random.random)
        test_board.reveal_location(0,0)
        observed_board = test_board.trackboard
        self.assertEqual(expected_board, observed_board)

    # Tests to ensure that the whole board would be revealed if no bombs are
    # placed on it
    def testFullBoardReveal(self):
        expected_board = [[True]*10]*10
        test_board = Board(10, 10)
        test_board.reveal_location(0,0)
        observed_board = test_board.trackboard
        self.assertEqual(expected_board, observed_board)

# These tests ensure that Board keeps track of how many squares have been
# revealed thus far correctly.  This is important to be able to determine
# winning condition (counter is less than the number of bombs) or the 
# losing condition (the counter is set to -1 if a bomb is triggered)
class testRevealLocationCounter(unittest.TestCase):
    # Sanity test, ensuring that the counter when a board is created is the
    # size of the board
    def testNoCellRevealCounter(self):
        expected_value = 25
        test_board = Board(5, 5)
        observed_value = test_board.to_pick
        self.assertEqual(expected_value, observed_value)

    # Test to ensure that revealing only one cell will decrement the counter
    # by one
    def testOneCellRevealCounter(self):
        random.seed(0xDEADBEEF)
        expected_value = 24
        test_board = Board(5, 5)
        test_board.scatter_bombs(5, rand=random.random)
        observed_value = test_board.reveal_location(2, 0)
        self.assertEqual(expected_value, observed_value)

    # Test to ensure that when multiple cells are revealed, the counter
    # decreases by the number of cells revealed.  In this case, 6 are revealed
    def testMulitCellRevealCounter(self):
        random.seed(0xDEADBEEF)
        expected_value = 19
        test_board = Board(5, 5)
        test_board.scatter_bombs(5, rand=random.random)
        observed_value = test_board.reveal_location(0, 4)
        self.assertEqual(expected_value, observed_value)

    # Test to ensure that when a bomb is revealed, the counter is set to -1
    def testBombReveal(self):
        random.seed(0xDEADBEEF)
        expected_value = -1
        test_board = Board(5, 5)
        test_board.scatter_bombs(5, rand=random.random)
        observed_value = test_board.reveal_location(0, 2)
        self.assertEqual(expected_value, observed_value)

# These tests ensure that the squares surrounding a bomb placement are summed
# correctly
class testSumSurrounding(unittest.TestCase):
    # Tests the placement of a single bomb
    def testLoneCell(self):
        expected_board = [[1,1,1],[1,0,1],[1,1,1]]
        test_board = Board(3,3)
        test_board.sum_surrounding(1,1)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

    # Tests the placement of two bombs where the sums of cells between them
    # will be stacked and added correctly
    def testCollidingSums(self):
        expected_board = [[0, 2, 0], [1, 2, 1], [0, 0, 0]]
        test_board = Board(3,3)
        test_board.sum_surrounding(0, 0)
        test_board.sum_surrounding(2, 0)
        observed_board = test_board.board
        self.assertEqual(expected_board, observed_board)

class testToString(unittest.TestCase):
    def testNoReveal(self):
        expected_board = "    0 1 2 3 4\n" +  \
                         "0: |_|_|_|_|_|\n" + \
                         "1: |_|_|_|_|_|\n" + \
                         "2: |_|_|_|_|_|\n" + \
                         "3: |_|_|_|_|_|\n" + \
                         "4: |_|_|_|_|_|"
        test_board = Board(5,5)
        observed_board = str(test_board)
        self.assertEqual(expected_board, observed_board)

    def testOneReveal(self):
        random.seed(0xDEADBEEF)
        expected_board = "    0 1 2 3 4\n" +  \
                         "0: |_|_|1|_|_|\n" + \
                         "1: |_|_|_|_|_|\n" + \
                         "2: |_|_|_|_|_|\n" + \
                         "3: |_|_|_|_|_|\n" + \
                         "4: |_|_|_|_|_|"

        test_board = Board(5,5)
        test_board.scatter_bombs(5, rand=random.random)
        test_board.reveal_location(2, 0)
        observed_board = str(test_board)
        self.assertEqual(expected_board, observed_board)

    def testEmptyCellReveal(self):
        random.seed(0xDEADBEEF)
        expected_board = "    0 1 2 3 4\n" +  \
                         "0: |_|_|1| | |\n" + \
                         "1: |_|_|2|1| |\n" + \
                         "2: |_|_|_|2|1|\n" + \
                         "3: |_|_|_|_|_|\n" + \
                         "4: |_|_|_|_|_|"
        test_board = Board(5,5)
        test_board.scatter_bombs(5, rand=random.random)
        test_board.reveal_location(4,0)
        observed_board = str(test_board)
        self.assertEqual(expected_board, observed_board)

    def testBombCellReveal(self):
        random.seed(0xDEADBEEF)
        expected_board = "    0 1 2 3 4\n" +  \
                         "0: |_|_|_|_|_|\n" + \
                         "1: |_|_|_|_|_|\n" + \
                         "2: |*|_|_|_|_|\n" + \
                         "3: |_|_|_|_|_|\n" + \
                         "4: |_|_|_|_|_|"
        test_board = Board(5,5)
        test_board.scatter_bombs(5, rand=random.random)
        test_board.reveal_location(0,2)
        observed_board = str(test_board)
        self.assertEqual(expected_board, observed_board)

    def testHugeBoard(self):
        expected_board = "    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9\n" +
                         "0: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "1: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "2: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "3: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "4: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "5: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "6: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "7: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "8: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "9: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "0: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "1: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "2: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "3: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "4: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "5: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "6: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "7: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "8: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|\n" +
                         "9: |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|"
        test_board = Board(20, 20)
        observed_board = str(test_board)
        self.assertEqual(expected_board, observed_board)

if __name__ == "__main__":
    unittest.main()