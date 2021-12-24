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
        for key, value in self.answers.items():
            if Levenshtein.ratio(key.lower(), self.text.lower()) > 0.7:
                answer = random.choice(value)
        
        return answer

ac = AnswerChoice('Плотно и позавтракал')
b = ac.FindAnswer()
print(b)