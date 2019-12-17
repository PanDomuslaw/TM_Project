from run_dictation import DictationArgs
from dictation.dictation_client import create_audio_stream, print_results
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer
import re
import chess


def recognize_speech():
    args = DictationArgs()
    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)
            print('Recognizing...')
            results = recognizer.recognize(stream)
            return results[0]["transcript"]

def recognize_move(transcript):
    numax = []
    regularnum = [r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8']
    for i in range(1,9):
        numax.append(str(i))

    regularICAO = [r'alfa', r'brav?w?o', r'c?z?h?arlie?', r'delta', r'ec?ho', r'fox?k?s?trot?', r'golf', r'hotel?']
    letterax = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    command = re.split('na', transcript)
    try:
        print(command[0], '   ', command[1])
    except IndexError:
        return 'blad'

    for i in range(len(letterax)):
        a = re.search(regularICAO[i], command[0])
        b = re.search(regularICAO[i], command[1])
        na = re.search(regularnum[i], command[0])
        nb = re.search(regularnum[i], command[1])
        try:
            print(a.group(0))
            letFirst = letterax[i]
        except AttributeError:
            pass

        try:
            print(na.group(0))
            numFirst = numax[i]
        except AttributeError:
            pass

        try:
            print(b.group(0))
            letSecond = letterax[i]
        except AttributeError:
            pass

        try:
            print(nb.group(0))
            numSecond = numax[i]
        except AttributeError:
            pass
    try:
        return letFirst + numFirst + letSecond + numSecond
    except UnboundLocalError:
        return 'blad'

def make_move_from_speech(transcript, board):
    figures_name = [r'kr[óo]l', r'dama', r'hetman', r'kr[óo]lowa', r'goniec?', r'laufer', r'ko[ńn]', r'skoczek',
                   r'wie[żz]a', r'pione?k?']
    figures_sign = ['K', 'Q', 'Q', 'Q', 'B', 'B', 'N', 'N', 'R', 'P']

    numax = []
    regularnum = [r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8']
    for i in range(1,9):
        numax.append(str(i))

    regularICAO = [r'alfa', r'brav?w?o', r'c?z?h?arlie?', r'delta', r'ec?ho', r'fox?k?s?trot?', r'golf', r'hotel?']
    letterax = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    command = re.split('na', transcript)


    if len(command) != 2:
        print('nie wykryto słowa "na"\nproszę spróbować ponownie')
        return -1
    print(command[0], ' ', command[1])

    # wykrywanie, czy wypowiedziano nazwe figury
    f = 0
    for i in range(len(figures_name)):
        figure = re.search(figures_name[i], command[0])
        try:
            #print(figure.group(0))
            f = figure.group(0)
            f = figures_sign[i]
        except AttributeError:
            pass
    print(f)
    # jesli wykryto nazwe figury
    if f != 0:
        for i in range(len(letterax)):
            b = re.search(regularICAO[i], command[1])
            nb = re.search(regularnum[i], command[1])
            

            try:
                l = b.group(0)
                letSecond = letterax[i]
            except AttributeError:
                pass

            try:
                n = nb.group(0)
                numSecond = numax[i]
            except AttributeError:
                pass

            try:
                if f == 'P':
                    move = letSecond + numSecond
                else:
                    move = f + letSecond + numSecond
                
                #print('move: ',move)
                move = board.parse_san(move)
                if move in board.legal_moves:
                    return move
            except UnboundLocalError:
                pass
            except ValueError:
                pass

    #jesli nie wykryto nazwy figury, sprawdza wspolrzedne z i na
    else:
        for i in range(len(letterax)):
            a = re.search(regularICAO[i], command[0])
            b = re.search(regularICAO[i], command[1])
            na = re.search(regularnum[i], command[0])
            nb = re.search(regularnum[i], command[1])
            try:
                print(a.group(0))
                letFirst = letterax[i]
            except AttributeError:
                pass

            try:
                print(na.group(0))
                numFirst = numax[i]
            except AttributeError:
                pass

            try:
                print(b.group(0))
                letSecond = letterax[i]
            except AttributeError:
                pass

            try:
                print(nb.group(0))
                numSecond = numax[i]
            except AttributeError:
                pass
        try:
            return board.parse_uci(letFirst + numFirst + letSecond + numSecond)
        except UnboundLocalError:
            #print("1: nie wykryto prawidlowego ruchu \nproszę spróbować ponownie")
            return -1
    #print("2: nie wykryto prawidłowego ruchu \nproszę spróbować ponownie")
    return -1