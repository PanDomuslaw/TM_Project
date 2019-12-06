from recording import recording
from sarmata import sarmata
import chess.uci

print("Instrukcja: \n Nazewnictwo figur: pion, goniec, skoczek, hetman, wieża, król \n Gracz gra czarnymi (góra szachownicy). Powodzenia!")

board = chess.Board()
engine = chess.uci.popen_engine("stockfish-8-win\Windows\stockfish_8_x64.exe")
engine.uci()

bool = True
czy_zacz = False
while bool:

    engine.position(board)
    board.push(engine.go(movetime=2000)[0])
    print(board)

    print(board.legal_moves)
    print(board.pseudo_legal_moves)


    bool2 = True

    while bool2:

        recording(__name__)

        move_bez_spacji=sarmata(__name__)

        try:
            move = chess.Move.from_uci(move_bez_spacji)
            print(move)

            if (move in board.legal_moves):
                bool2 = False
            else:
                print('Niepoprawny ruch!')

        except ValueError:
            print('Niepoprawny ruch!')


    board.push(move)  # zadawanie ruchu

    if board.is_checkmate():
        print("SZACH MAT!")

    if board.is_check():
        print("SZACH!")

    if board.is_stalemate():
        print("PAT!")

    bool = ~board.is_game_over()