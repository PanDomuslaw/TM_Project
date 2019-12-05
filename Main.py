import chess
import chess.svg

board = chess.Board()

print(board.legal_moves)

print(board)

board.push_san("Nf3")
print(board)

board.push_san("a6")
print(board)

board.push_san("e3")
print(board)

board.push_san("a5")
print(board)


board.push_san("Bd3")
print(board)

board.push_san("a4")
print(board)

board.push_san("O-O")
print(board)

board.push_san("a3")
print(board)

print(board.legal_moves)
