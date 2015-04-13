import sys

def get_board_params(args=sys.argv):
    arg1 = args[1]
    arg2 = args[2]
    arg3 = args[3]
    return (int(arg1), int(arg2), int(arg3))

if __name__ == "__main__":
    x, y, bombs = get_board_params()
    game = Game(x, y, bombs)
    print game.board
    victory_status = game.run()
    if victory_status:
        print "You win!"
    else:
        print "You lose, try again"