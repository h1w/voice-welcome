import Levenshtein
import json
from settings import CONFIG_DIR
import os
import random

class AnswerChoice:
    def __init__(self, text):
        self.text = text
        self.answers = self.LoadJson()
    
    def LoadJson(self):
        ANSWERS_FILE = os.path.normpath(os.path.join(CONFIG_DIR, 'answers.json'))
        
        with open(ANSWERS_FILE, 'r', encoding='utf-8') as f:
            answers = json.load(f)

        return answers
    
    def FindAnswer(self):
        answer = None
        for keys, value in self.answers.items():
            ok = False
            for key in keys.split(','):
                if Levenshtein.ratio(key.lower().strip(' '), self.text.lower()) > 0.7:
                    answer = random.choice(value)
                    ok = True
                    break
            if ok == True:
                break
        
        return answer