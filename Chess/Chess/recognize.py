from run_dictation import DictationArgs
from dictation.dictation_client import create_audio_stream, print_results
from dictation.service.dictation_settings import DictationSettings
from dictation.service.streaming_recognizer import StreamingRecognizer
import re


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
    print(command[0], '   ', command[1])
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