from techmo_sarmata_pyclient.utils.wave_loader import load_wave
from techmo_sarmata_pyclient.service.sarmata_settings import SarmataSettings
from techmo_sarmata_pyclient.service.sarmata_recognize import SarmataRecognizer
from techmo_sarmata_pyclient.service.asr_service_pb2 import ResponseStatus
from address_provider import AddressProvider
import os


def print_results(responses):
    if responses is None:
        print("Empty results - None object")
        return

    for response in responses:
        if response is None:
            print("Empty results - skipping response")
            continue

        print("Received response with status: {}".format(ResponseStatus.Name(response.status)))



        if response.error:
            print("[ERROR]: {}".format(response.error))



        for n, res in enumerate(response.results):
            transcript = " ".join([word.transcript for word in res.words])
            print("[{}.] {} /{}/ ({})".format(n, transcript, res.semantic_interpretation, res.confidence))

            if n == 0:
                print("hallo, dalej przekazuję:", res.semantic_interpretation)
                move = res.semantic_interpretation
                return move

def sarmata(__name__):
    ap = AddressProvider()


    wave_file = "waves/chess_command.wav"  # nagranie
    grammar_file = "grammars/chess.abnf"  # gramatyka
    address = ap.get("sarmata")

    audio = load_wave(wave_file)

    settings = SarmataSettings()
    session_id = os.path.basename(wave_file)
    settings.set_session_id(session_id)
    settings.load_grammar(grammar_file)

    recognizer = SarmataRecognizer(address)
    results = recognizer.recognize(audio, settings)


    move = print_results(results)  # zapis ruchu - move = nasz ruch

    if move==None :
        move=""

    #wypisuje komendę (string) rozpoznaną - ze spacjami
    #print("długośc ruchu", len(move))

    i = 0
    move_bez_spacji = ""

    while i < len(move):

        if move[i] != " ":
            move_bez_spacji = move_bez_spacji + move[i]

        i = i + 1

    #wypisuje komendę po usunięciu spacji i długość tej komedy (stringa)
    #print("bez spacji: ", move_bez_spacji, "długość: ", len(move))

    return move_bez_spacji
