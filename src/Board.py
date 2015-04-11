import random

class Board:
    @staticmethod
    def create_empty_board(x, y):
        new_board = []
        for i in range(0,y):
            new_board.append([0] *x)
        return new_board

    def __init__(self, x, y):
        self.board = self.create_empty_board(x, y)

    def place_bomb(self, x, y):
        self.board[y][x] = -1

    def scatter_bombs(self, quantity, rand=random.random):
        pass