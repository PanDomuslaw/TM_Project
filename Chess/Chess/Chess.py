import chess
import chess.svg
from selenium import webdriver
from address_provider import AddressProvider
from os.path import join as opjoin
from run_dictation import DictationArgs
from recognize import recognize_speech, recognize_move, make_move_from_speech


board = chess.Board()
a = chess.svg.board(board=board)
file = open ("board.svg","w")
file.write(a)
file.close()

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("file:///C:/TM/TM_Project/Chess/Chess/board.svg")

#driver.fullscreen_window()
while(True):
    print(board.legal_moves)
    input('naciśnij enter, aby rozpoznać mowę')
    speech = recognize_speech()
    print('rozpoznano: ', speech)
    move = make_move_from_speech(speech, board)
    print(move)

    #x = input("Podaj ruch z: ")
    #y = input("Podaj ruch do: ")
    condition = True

    while condition:
        if move != -1:
            #print(move in board.legal_moves)
            board.push(move)
            break
        else:
            print("Podano niedozwolony ruch!")
            print(board.legal_moves)
            input('naciśnij enter, aby rozpoznać mowę')
            speech = recognize_speech()
            print('rozpoznano: ', speech)
            move = make_move_from_speech(speech, board)


    a = chess.svg.board(board=board)
    file = open ("board.svg","w")
    file.write(a)
    file.close()
    driver.refresh()
    #print(board)
    if board.is_game_over():
        print('koniec gry')
        break