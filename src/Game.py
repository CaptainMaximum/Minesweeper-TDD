from Board import Board
import random

class Game:
    def __init__(self, x, y, bombs, testing=False):
        self.hidden_cells = x * y
        self.x_dimension = x
        self.y_dimension = y
        self.total_bombs = bombs
        if not testing:
            self.create_board(x, y, bombs)

    def create_board(self, x, y, bombs, rand=random.random):
        self.board = Board(5,5)
