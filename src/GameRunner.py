import sys
from Game import Game
from Exceptions import InvalidBoardException

def get_board_params(args=sys.argv):
    if len(args) != 4:
        return (None, None, None)
    arg1, arg2, arg3 = args[1:4]
    try:
        return_value = (int(arg1), int(arg2), int(arg3))
        if any(map(lambda x: x <= 0, return_value)):
            return (None, None, None)
        return return_value
    except ValueError:
        return (None, None, None)

if __name__ == "__main__":
    x, y, bombs = get_board_params()
    if not any([x, y, bombs]):
        print "Usage: python GameRunner.py <x-dimension> <y-dimension> <# of bombs>"
        sys.exit(-1)
    try:
        game = Game(x, y, bombs)
    except InvalidBoardException as e:
        print "Too many bombs: Board size is %d, bombs specified is %d" % (
            e.spaces, e.bombs)
        sys.exit(-1)

    victory_status = game.run()
    print game.board
    if victory_status:
        print "You win!"
    else:
        print "You lose, try again"