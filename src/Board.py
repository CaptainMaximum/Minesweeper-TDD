class Board:
    @staticmethod
    def create_empty_board(x, y):
        return [[0] *x] *y

    def __init__(self, x, y):
        self.board = create_empty_board(x, y)