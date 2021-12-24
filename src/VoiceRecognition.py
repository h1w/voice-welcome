from vosk import Model, KaldiRecognizer
from settings import MODELS_DIR, TEMP_DIR
import os
import sys
import queue
import sounddevice as sd
from TextToSpeech import TextToSpeech
import json
from PlaySound import PlaySound
from AnswerChoice import AnswerChoice
import threading
import Levenshtein

q = queue.Queue()

MODEL_NAME = 'vosk-model-small-ru-0.22'

model = Model(os.path.normpath(os.path.join(MODELS_DIR, MODEL_NAME)))

kaldi_fs = 48000
fs = 44100
blocksize = 8000
dtype = 'int16'
channels = 1

ps_thread = None
lock = threading.Lock()

outfile_abspath = os.path.normpath(os.path.join(TEMP_DIR, 'output.wav'))

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def playingsound(result):
    with lock:
        if result != "":
            answerchoice = AnswerChoice(result)
            answer = answerchoice.FindAnswer()
            if answer != None:
                texttospeech = TextToSpeech(answer, outfile_abspath)
                texttospeech.GetVoiceFromText()
                
                playsound = PlaySound(outfile_abspath)
                playsound.play()


with sd.RawInputStream(samplerate=fs, blocksize=blocksize, dtype=dtype, channels=channels, callback=callback):
    rec = KaldiRecognizer(model, kaldi_fs)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())['text']
            print('RES', result)

            # Check on stop words
            # stop_words = ['прекрати', 'стой', 'стоп', 'остановись']
            # for stop_word in stop_words:
            #     if Levenshtein.ratio(result, stop_word) > 0.7:
            #         # ps_thread.do_run = False
            #         pass # Kill the thread

            if ps_thread == None or not ps_thread.is_alive():
                ps_thread = threading.Thread(target=playingsound, args=(result, ))
                ps_thread.start()

        else:
            print('PART', json.loads(rec.PartialResult())["partial"])