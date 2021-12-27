from typing import Text
from VoiceRecognition import VoiceRecognition
from TextToSpeech import TextToSpeech_gTTS
from settings import CONFIG_DIR, TEMP_DIR, messages_json
import os
import json
from random import choice
from PlaySound import PlaySound

def play_welcome_message():
    welcome_msg = choice(messages_json['Welcome'])
    msg_filepath = os.path.normpath(os.path.join(TEMP_DIR, 'welcome_message.mp3'))
    gtts = TextToSpeech_gTTS()
    gtts.gTTS(welcome_msg, msg_filepath) # Текст в речь
    play_sound = PlaySound(msg_filepath)
    play_sound.play() # Произнести приветственное сообщение вслух

# Первое включение, произвести приветственное сообщение
play_welcome_message()

voice_recognition = VoiceRecognition()
# voice_recognition.recognitionFromMic_SR()
voice_recognition.recognitionFromMic_Vosk()