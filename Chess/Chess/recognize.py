from run_dictation import DictationArgs
from dictation.dictation_client import create_audio_stream, print_results
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer
import re
import chess
import wave
import pyaudio


def recognize_speech():
    args = DictationArgs()
    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)
            print('Recognizing...')
            results = recognizer.recognize(stream)
            #print(stream.data)
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
            #print(a.group(0))
            letFirst = letterax[i]
        except AttributeError:
            pass

        try:
            #print(na.group(0))
            numFirst = numax[i]
        except AttributeError:
            pass

        try:
            #print(b.group(0))
            letSecond = letterax[i]
        except AttributeError:
            pass

        try:
            #print(nb.group(0))
            numSecond = numax[i]
        except AttributeError:
            pass
    try:
        return letFirst + numFirst + letSecond + numSecond
    except UnboundLocalError:
        return 'blad'

def make_move_from_speech(transcript, board):
    """
    trascript - text (string)
    board - chess.Board() object
    return: Move object or -1
    reacts both on figure names (if exact) or coordinates
    roszada (O-O)/(O-O-O): reacts on 'roszada' word. If both are legal return long first (O-O-O)
    promotion: search figure name after 'promocja' word.
    """

    figures_name = [r'kr[óo]la?', r'dam[ay]', r'hetmana?', r'kr[óo]low[aą]', r'goniec', r'laufe?ra?', r'k?o[ńn]i?e?',
                   r'skocze?ka?', r'wie[żz][aęe]', r'pione?k?a?', r'jane?ka?', r'kierune?ka?u?']
    figures_sign = ['K', 'Q', 'Q', 'Q', 'B', 'B', 'N', 'N', 'R', 'P', 'P', 'P']

    numax = []
    regularnum = [r'1', r'2', r'3', r'4', r'5', r'6', r'7', r'8']
    for i in range(1,9):
        numax.append(str(i))

    regularICAO = [r'alfa', r'[bp]ra[vw]o', r'c[zh]ar[ln][iyo]e?', r'tarli', r'delta', r'ec?ho', r'fox?k?s?trot?', r'golf?', r'hotel?']
    letterax = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'g', 'h']

    # reakcja na słowo 'roszada'
    rosz = 0
    rosz = re.search(r'roszada', transcript)
    #print(rosz)
    try:
        if rosz.group(0) == 'roszada':
            try:
                return board.parse_san('O-O-O')
            except ValueError:
                pass
            try:
                return board.parse_san('O-O')
            except ValueError:
                #print('nie można wykonać roszady')
                return -1
    except AttributeError:
        pass

    command = re.split('na', transcript)

    prom_fig = 0
    promotion = re.split('promocja', transcript)

    if len(command) != 2:
        #print('nie wykryto słowa "na"\nproszę spróbować ponownie')
        return -1
    if len(promotion) == 2:
        print(command[0], ' ', command[1], 'promocja: ', promotion[1])
    else:
        print(command[0], ' ', command[1])

    # wykrywanie, czy wypowiedziano nazwe figury lub nazwę figury po promocji
    f = 0
    for i in range(len(figures_name)):
        figure = re.search(figures_name[i], command[0])
        try:
            prom_fig = re.search(figures_name, promotion[1])
            prom_fig = prom_fig.group(0)
            prom_fig = figures_sign[i]
        except IndexError:
            prom_fig = 0
            pass
        except AttributeError:
            pass
        try:
            #print(figure.group(0))
            f = figure.group(0)
            f = figures_sign[i]
        except AttributeError:
            pass

    #print(f)
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
                if prom_fig == 0:
                    if f == 'P':
                        move = letSecond + numSecond
                    else:
                        move = f + letSecond + numSecond
                else:
                    move = letSecond + numSecond + '=' + prom_fig

                
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
                letFirst = a.group(0)
                letFirst = letterax[i]
            except AttributeError:
                pass

            try:
                numFirst = na.group(0)
                numFirst = numax[i]
            except AttributeError:
                pass

            try:
                letSecond = b.group(0)
                letSecond = letterax[i]
            except AttributeError:
                pass

            try:
                numSecond = nb.group(0)
                numSecond = numax[i]
            except AttributeError:
                pass
        try:
            if prom_fig != 0:
                return board.parse_uci(letFirst + numFirst + letSecond + numSecond + '=' + prom_fig)
            return board.parse_uci(letFirst + numFirst + letSecond + numSecond)
        except UnboundLocalError:
            #print("1: nie wykryto prawidlowego ruchu \nproszę spróbować ponownie")
            return -1
        except ValueError:
            return -1
    #print("2: nie wykryto prawidłowego ruchu \nproszę spróbować ponownie")
    return -1