# from playsound import playsound
import wave
from playsound import playsound

class PlaySound:
    def __init__(self, abspath):
        self.filename_abspath = abspath
    
    def play(self):
        try:
            playsound(self.filename_abspath)
        except Exception as e:
            print("ERROR", e)
            pass