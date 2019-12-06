
import chess.uci


board = chess.Board()
engine = chess.uci.popen_engine("stockfish-8-win\Windows\stockfish_8_x64.exe")
engine.uci()
engine.position(board)

bool = True
while bool:

    board.push(engine.go(movetime=2000)[0])
    print(board)

    print(board.legal_moves)

    #to by trzeba zmienić na input głosowy
    move=input('Jaki jest Twój ruch? : ' )

    board.push_san(move)

    if board.is_checkmate():
        print("SZACH MAT!")

    if board.is_check():
        print("SZACH!")

    if board.is_stalemate():
        print("PAT!")

    bool=~board.is_game_over()
