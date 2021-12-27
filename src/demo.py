from typing import Text
from VoiceRecognition import VoiceRecognition
from TextToSpeech import TextToSpeech_gTTS
from settings import CONFIG_DIR, TEMP_DIR
import os
import json
from random import choice
from PlaySound import PlaySound
import time

# Import messages from messages.json
messages_filepath = os.path.normpath(os.path.join(CONFIG_DIR, 'messages.json'))
with open(messages_filepath, 'r', encoding='utf-8') as mj:
    messages_json = json.load(mj)

def play_welcome_message():
    welcome_msg = choice(messages_json['Welcome'])
    msg_filepath = os.path.normpath(os.path.join(TEMP_DIR, 'welcome_message.wav'))
    gtts = TextToSpeech_gTTS()
    gtts.gTTS(welcome_msg, msg_filepath) # Текст в речь
    play_sound = PlaySound(msg_filepath)
    play_sound.play() # Произнести приветственное сообщение вслух

# Первое включение, произвести приветственное сообщение
play_welcome_message()

voice_recognition = VoiceRecognition()
# voice_recognition.recognitionFromMic_SR()
voice_recognition.recognitionFromMic_Vosk()