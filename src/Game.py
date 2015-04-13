from Board import Board
import random
import re

class Game:
    def __init__(self, x, y, bombs, testing=False):
        self.hidden_cells = x * y
        self.x_dimension = x
        self.y_dimension = y
        self.total_bombs = bombs
        if not testing:
            self.create_board(x, y, bombs)

    def create_board(self, x, y, bombs, rand_func=random.random):
        self.board = Board(x, y)
        self.board.scatter_bombs(bombs, rand=rand_func)

    def is_win(self):
        return 0 <= self.hidden_cells <= self.total_bombs 

    def is_lose(self):
        return self.hidden_cells < 0

    def make_move(self, x, y):
        self.hidden_cells = self.board.reveal_location(x, y)

    def parse_move(self, move_string):
        move_string = move_string.strip("\n\r\t ")
        split_input = re.split("\s+", move_string)
        if len(split_input) == 2:
            try:
                coords = (int(split_input[0]), int(split_input[1]))
                if (coords[0] >= 0 and coords[0] < self.x_dimension and
                    coords[1] >= 0 and coords[1] < self.y_dimension):
                    return coords
            except ValueError:
                return None
        return None

    def run(self):
        while not (self.is_win() or self.is_lose()):
            print self.board
            move = raw_input("Your move (x y): ")
            coords = self.parse_move(move)
            if coords:
                self.make_move(coords[0], coords[1])
            else:
                print "Invalid input: %s" % move
        return self.is_win()