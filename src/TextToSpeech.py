import requests
import os
from settings import TEMP_DIR, yandex
from utils import ConvertPcmToWav

class TextToSpeech:
    def __init__(self, text, output_name):
        self.OATH_TOKEN = yandex['OATH_TOKEN']
        self.FOLDER_ID = yandex['FOLDER_ID']
        self.IAM_TOKEN = self.getIAMToken()
        self.text = text
        self.name = 'output.pcm'
        self.output_name = output_name

    def getIAMToken(self):
        data = "{\"yandexPassportOauthToken\":\"%s\"}" % self.OATH_TOKEN
        request = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', data=data)
        IAM_TOKEN = request.json()["iamToken"]

        return IAM_TOKEN

    def getVoiceToBin(self):
        url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

        headers = {
            'Authorization': 'Bearer ' + self.IAM_TOKEN,
        }

        data = {
            "text": self.text,
            "lang": "ru-RU",
            "speed": 1,
            "voice": "filipp",
            "emotion": "good",
            'folderId': self.FOLDER_ID,
            'format': 'lpcm'
        }

        with requests.post(url, headers=headers, data=data, stream=True) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

            for chunk in resp.iter_content(chunk_size=None):
                yield chunk

    def GetVoiceFromText(self):
        with open(os.path.normpath(os.path.join(TEMP_DIR, self.name)), 'wb') as f:
            for audio_content in self.getVoiceToBin():
                f.write(audio_content)
        
        ConvertPcmToWav(os.path.normpath(os.path.join(TEMP_DIR, self.name)), self.output_name)