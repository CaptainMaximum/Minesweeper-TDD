import sys
from src.Game import Game

def get_board_params(args=sys.argv):
    if len(args) != 4:
        return None
    arg1, arg2, arg3 = args[1:4]
    return (int(arg1), int(arg2), int(arg3))

if __name__ == "__main__":
    x, y, bombs = get_board_params()
    game = Game(x, y, bombs)
    victory_status = game.run()
    if victory_status:
        print "You win!"
    else:
        print "You lose, try again"