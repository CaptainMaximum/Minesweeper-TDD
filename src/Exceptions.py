class InvalidBoardException(Exception):
    '''Raised when the user specifies more bombs than there are spaces'''
    def __init__(self, spaces, bombs):
        self.spaces = spaces
        self.bombs = bombs