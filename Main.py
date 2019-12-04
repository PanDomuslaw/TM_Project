import chess
import chess.svg
import jupyter

board = chess.Board()

print(board.legal_moves)

print(board)

board.push_san("e4")
print(board)


chess.svg.piece(chess.Piece.from_symbol("R"))

chess.svg.board(board=board)
