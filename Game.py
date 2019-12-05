import chess
import re

class Game:

    def __init__(self):
        self._board = chess.Board()

    def move(self, pos):
        if pos in self._board.legalmoves():
            self._board.push_san(pos)
        else:
            for i in self._board.legalmoves():
                # matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)



hksdfub = Game()
