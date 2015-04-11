import random

class Board:
    @staticmethod
    def create_empty_board(x, y):
        new_board = []
        for i in range(0,y):
            new_board.append([0] *x)
        return new_board

    def __init__(self, x, y):
        self.x_dimension = x
        self.y_dimension = y
        self.board = self.create_empty_board(x, y)

    def place_bomb(self, x, y):
        self.board[y][x] = -1

    def scatter_bombs(self, quantity, rand=random.random):
        while quantity > 0:
            place_x = int(rand() * self.x_dimension)
            place_y = int(rand() * self.y_dimension)
            if self.board[place_y][place_x] == 0:
                self.place_bomb(place_x, place_y)
                quantity -= 1

