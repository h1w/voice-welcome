# from playsound import playsound
import wave
from playsound import playsound
import pygame

pygame.mixer.init()

class PlaySound:
    def __init__(self, abspath):
        self.filename_abspath = abspath
    
    def play(self):
        try:
            # playsound(self.filename_abspath)
            pygame.mixer.music.load(self.filename_abspath)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        except Exception as e:
            print("ERROR", e)
            pass