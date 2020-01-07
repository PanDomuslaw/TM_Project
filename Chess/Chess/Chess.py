from dictation.dictation_client import create_audio_stream, print_results
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer
from address_provider import AddressProvider
from os.path import join as opjoin
from run_dictation import DictationArgs
from recognize import recognize_speech, recognize_move, make_move_from_speech
import chess
import numpy as np
from selenium import webdriver
import pyaudio
import wave
import python.wave2ivec as w2i


def draw_pawns(data):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
    path_dict = {
        "r": "Graphics/r_bl.png",
        "n": "Graphics/n_bl.png",
        "b": "Graphics/b_bl.png",
        "q": "Graphics/q_bl.png",
        "k": "Graphics/k_bl_cus.png",
        "p": "Graphics/p_bl.png",
        "P": "Graphics/p_wh.png",
        "R": "Graphics/r_wh.png",
        "N": "Graphics/n_wh.png",
        "B": "Graphics/b_wh.png",
        "Q": "Graphics/q_wh.png",
        "K": "Graphics/k_wh_cus.png"
        }
    id = 0
    for i in data:
        if i != "/":
            if i in numbers:
                for j in range(0,int(i),1):
                    driver.execute_script("document.getElementById('"+ str(id) +"').innerHTML=' '")
                    id += 1 
            else:
                driver.execute_script("document.getElementById('"+ str(id) +"').innerHTML=' '")
                driver.execute_script("document.getElementById('"+ str(id) +"').innerHTML='<img src="+ path_dict[i] +" alt="'sdfgdfhg'" style="'width:100px; height:100px'">'")
                id +=1
        else:
            continue

def create_models(filepath, player):
    p = pyaudio.PyAudio()

    driver.execute_script("document.getElementById('player').innerHTML='"+ player +"'")
    driver.execute_script("document.getElementById('info').innerHTML='Tworzenie modeli graczy'")
    input('naciśnij enter, aby rozpoznać mowę')
    stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                frames_per_buffer=1024,
                input=True)
    frames = []
    for i in range(0, int(16000 / 1024 * 5)):
        data = stream.read(1024)
        frames.append(data)
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    wf = wave.open(filepath, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))
    wf.close()

def recognize_speaker():
     w, n_data = i_vector.process_wav("player.wav")
     i_vector.save_ivector_to_file("./in/player.ivec", w, n_data)
     s = i_vector.get_score_from_ivectors("./out/", "./in/")
     print(np.argmax(s))
     return np.argmax(s)


board = chess.Board()

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("file:///C:/Users/Borewicz/Desktop/TM_projekt/Chess/Chess/front_end.html")
draw_pawns(board.board_fen())

driver.execute_script("document.getElementById('info').innerHTML='Ładowanie modeli'")
i_vector = w2i.IVector()
#create_models("./wav/player1.wav","Gracz 1")
#create_models("./wav/player2.wav","Gracz 2")

#w, n_data = i_vector.process_wav("./wav/player1.wav")
#i_vector.save_ivector_to_file("./out/player_1.ivec", w, n_data)

#w, n_data = i_vector.process_wav("./wav/player2.wav")
#i_vector.save_ivector_to_file("./out/player_2.ivec", w, n_data)

driver.execute_script("document.getElementById('info').innerHTML=''")
driver.execute_script("document.getElementById('player').innerHTML=''")

#======================================================================================================
#======================================================================================================

player = 0
while(True):

    if player == 0:
        driver.execute_script("document.getElementById('player').innerHTML='Gracz 1'")
    else:
        driver.execute_script("document.getElementById('player').innerHTML='Gracz 2'")
    input('naciśnij enter, aby rozpoznać mowę')
    speech = recognize_speech()
    move = make_move_from_speech(speech, board)

    current_player = recognize_speaker()

    while True:
        if current_player == player:
            move = make_move_from_speech(speech, board)
            break
        else:
            driver.execute_script("document.getElementById('info').innerHTML='Zły gracz!'")
            input('naciśnij enter, aby rozpoznać mowę')
            speech = recognize_speech()
            move = make_move_from_speech(speech, board)
            current_player = recognize_speaker()

    driver.execute_script("document.getElementById('info').innerHTML=''")

    condition = True
    while condition:
        if move != -1:
            board.push(move)
            break
        else:
            driver.execute_script("document.getElementById('info').innerHTML='Podano zły ruch!'")
            input('naciśnij enter, aby rozpoznać mowę')
            speech = recognize_speech()
            move = make_move_from_speech(speech, board)
            current_player = recognize_speaker()

            while True:
                if current_player == player:
                    move = make_move_from_speech(speech, board)
                    break
            else:
                driver.execute_script("document.getElementById('info').innerHTML='Zły gracz!'")
                input('naciśnij enter, aby rozpoznać mowę')
                speech = recognize_speech()
                current_player = recognize_speaker()

            print('rozpoznano: ', speech)
            move = make_move_from_speech(speech, board)

    driver.execute_script("document.getElementById('info').innerHTML='Zły gracz!'")
    #driver.execute_script("document.getElementById('chess_data').innerHTML='"+board.board_fen()+"'")
    draw_pawns(board.board_fen())
    if player == 0:
        player = 1
    else:
        player = 0

    if board.is_game_over():
        condition = False;  
           
           
    
