from settings import MODELS_DIR, TEMP_DIR, HEADERS
import os
from vosk import Model, KaldiRecognizer
import sys
import queue
import json
import sounddevice as sd
import speech_recognition as sr
from TextToSpeech import TextToSpeech_gTTS
from PlaySound import PlaySound
from AnswerChoice import AnswerChoice
import threading
import AssistantFunctions as AF
import urllib.request
import time
import Levenshtein

MODEL_NAME = 'vosk-model-small-ru-0.22'

class VoiceRecognition:
    def __init__(self):
        self.q = queue.Queue()
        self.model = Model(os.path.normpath(os.path.join(MODELS_DIR, MODEL_NAME)))
        
        self.kaldi_fs = 48000
        self.fs = 44100
        self.blocksize = 8000
        self.dtype = 'int16'
        self.channels = 1

        self.ps_thread = None
        self.lock = threading.Lock()

        self.outfile_abspath = os.path.normpath(os.path.join(TEMP_DIR, 'output.wav'))

        # for speech_recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Assistant mode
        # 1 - Обычный режим
        # 2 - Режим балабобы
        self.assistant_mode = 1

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def playingsound(self, result):
        with self.lock:
            if result != "":
                answer = ""
                # Если режим ассистента не стандартный
                if self.assistant_mode == 2:
                    if Levenshtein.ratio(result, 'хватит болтать') > 0.7:
                        self.assistant_mode = 1
                        answer = "Включен стандартный режим. Чтобы со мной поговорить, скажите: давай поболтаем"
                    else:
                        payload = json.dumps({
                            "query": result,
                            "intro": 4,
                            "filter": 0
                        }, ensure_ascii=False)
                        req = urllib.request.Request(
                            "https://zeapi.yandex.net/lab/api/yalm/text3",
                            data=payload.encode('utf8'),
                            headers=HEADERS
                        )
                        resp = urllib.request.urlopen(req)
                        jsn = json.loads(resp.read().decode('utf8'))
                        answer = jsn['text']

                # Если режим ассистента стандартный
                answerchoice = ""
                if self.assistant_mode == 1:
                    answerchoice = AnswerChoice(result)
                    answer = answerchoice.FindAnswer()

                # Проверить, подразумевается ли, что ответ должен быть через функцию { FUNC:функция} 
                if ('FUNC:' in answer):
                    afunc = answer.split(':')[1]
                    if afunc == "GetTime":
                        answer = AF.GetTime()
                    elif afunc == "GetData":
                        answer = AF.GetData()
                    elif afunc == "GetFullDataTime":
                        answer = AF.GetData()
                    elif afunc == "WhatDay":
                        answer = AF.GetData()
                
                # Сменить режим
                if ('MODE:' in answer):
                    afunc = answer.split(':')[1]
                    if (afunc == "balaboba"):
                        answer = "Включен режим БАЛАБОБЫ. Если хотите прекратить, скажите: хватит болтать"
                        self.assistant_mode = 2
                    elif (afunc == "default"):
                        answer = "Включен стандартный режим. Чтобы со мной поговорить, скажите: давай поболтаем"
                        self.assistant_mode = 1

                if answer != None:
                    texttospeech = TextToSpeech_gTTS()
                    texttospeech.gTTS(answer, self.outfile_abspath)
                    
                    playsound = PlaySound(self.outfile_abspath)
                    playsound.play()
            time.sleep(2)
    
    def recognitionFromMic_Vosk(self):
        with sd.RawInputStream(samplerate=self.fs, blocksize=self.blocksize, dtype=self.dtype, channels=self.channels, callback=self.callback):
            rec = KaldiRecognizer(self.model, self.kaldi_fs)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())['text']
                    print('RES', result)

                    if self.ps_thread == None or not self.ps_thread.is_alive(): # Не разрешать потоку запускаться, пока он не закончил предыдущую озвучку
                        self.ps_thread = threading.Thread(target=self.playingsound, args=(result, ))
                        self.ps_thread.start()

                else:
                    print('PART', json.loads(rec.PartialResult())["partial"])
    
    def recognitionFromMic_SR(self):
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        
        while True:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
        
            # set up the response object
            response = {
                "success": True,
                "error": None,
                "transcription": None
            }

            # try recognizing the speech in the recording
            # if a RequestError or UnknownValueError exception is caught,
            #     update the response object accordingly
            try:
                response["transcription"] = self.recognizer.recognize_google(audio, language='ru-ru')
            except sr.RequestError:
                # API was unreachable or unresponsive
                response["success"] = False
                response["error"] = "API unavailable"
            except sr.UnknownValueError:
                # speech was unintelligible
                response["error"] = "Не удалось распознать речь"
                response["success"] = False

            if response["error"]:
                print("[ERROR]:", response["error"])
            if response["success"] == True:
                # Речь распозналась
                #print(response["transcription"])
                result = response["transcription"]
                print("[INFO]: Result of recognition:", result)
                if self.ps_thread == None or not self.ps_thread.is_alive(): # Не разрешать потоку запускаться, пока он не закончил предыдущую озвучку
                    self.ps_thread = threading.Thread(target=self.playingsound, args=(result, ))
                    self.ps_thread.start()
