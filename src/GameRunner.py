import sys

def get_board_params(args=sys.argv):
    pass

if __name__ == "__main__":
    x, y, bombs = get_board_params()
    game = Game(x, y, bombs)
    print game.board
    victory_status = game.run()
    if victory_status:
        print "You win!"
    else:
        print "You lose, try again"