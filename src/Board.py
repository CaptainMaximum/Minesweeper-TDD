import random

class Board:
    @staticmethod
    def create_empty_board(x, y, value=0):
        new_board = []
        for i in range(0,y):
            new_board.append([value] *x)
        return new_board

    def __init__(self, x, y):
        self.x_dimension = x
        self.y_dimension = y
        self.board = self.create_empty_board(x, y)
        # trackboard keeps track of what cells have been revealed so far
        self.trackboard = self.create_empty_board(x, y, value=False)

    def sum_surrounding(self, x, y):
        for i in range(-1, 2):
            if (x + i >= 0 and x + i < self.x_dimension):
                for k in range(-1, 2):
                    if (y + k >= 0 and y + k < self.y_dimension and self.board[x+i][y+k] != -1):
                        if not (i == 0 and k == 0):
                            self.board[x+i][y+k] += 1

    def place_bomb(self, x, y):
        self.board[x][y] = -1
        self.sum_surrounding(x,y)

    def scatter_bombs(self, quantity, rand=random.random):
        while quantity > 0:
            place_x = int(rand() * self.x_dimension)
            place_y = int(rand() * self.y_dimension)
            if self.board[place_x][place_y] != -1:
                self.place_bomb(place_x, place_y)
                quantity -= 1

    def reveal_location(self, x, y):
        if x < 0 or x >= self.x_dimension or y < 0 or   \
            y >= self.y_dimension or self.trackboard[x][y]:
            return
        self.trackboard[x][y] = True
        if self.board[x][y] == -1:
            return
        if self.board[x][y] == 0:
            self.reveal_location(x-1, y)
            self.reveal_location(x+1, y)
            self.reveal_location(x-1, y-1)
            self.reveal_location(x+1, y+1)
            self.reveal_location(x, y-1)
            self.reveal_location(x, y+1)
            self.reveal_location(x+1, y-1)
            self.reveal_location(x-1, y+1)

    def __str__(self):
        board_string = "   "
        for i in range(0, self.x_dimension):
            board_string += " %d" % i
        for i in range(0, self.y_dimension):
            board_string += "\n%d: |" % i
            for j in range(0, self.x_dimension):
                board_string += "_|"
        return board_string