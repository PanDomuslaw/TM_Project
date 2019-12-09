import chess
import chess.svg
from selenium import webdriver
from dictation.dictation_client import create_audio_stream, print_results
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer
from address_provider import AddressProvider
from os.path import join as opjoin
from run_dictation import DictationArgs


board = chess.Board()
a = chess.svg.board(board=board)

file = open ("board.svg","w")
file.write(a)
file.close()

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("file:///C:/Users/2octa/Desktop/Chess/Chess/board.svg")

#driver.fullscreen_window()
while(True):
    print(board.legal_moves)
    args = DictationArgs()
    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)
            print('Recognizing...')
            results = recognizer.recognize(stream)
            print(results[0]["transcript"])

    x = input("Podaj ruch z: ")
    y = input("Podaj ruch do: ")
    move = chess.Move(int(x), int(y))

    #print(move in board.legal_moves)
    condition = True
    
    while condition:
        if move in board.legal_moves:
            #print(move in board.legal_moves)
            board.push(move)
            break
        else:
            print("Podano niedozwolony ruch!")
            print(board.legal_moves)
            x = input("Podaj ruch z: ")
            y = input("Podaj ruch do: ")
            move = chess.Move(int(x), int(y))
    
    a = chess.svg.board(board=board)
    file = open ("board.svg","w")
    file.write(a)
    file.close()
    driver.refresh()
    #print(board)

    
           
           
    
