import os
import configparser
import json

SRC_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

REPOSITORY_DIR = os.path.normpath(os.path.join(SRC_DIR, os.pardir))

TEMP_DIR = os.path.normpath(os.path.join(REPOSITORY_DIR, 'temp'))

MODELS_DIR = os.path.normpath(os.path.join(REPOSITORY_DIR, 'models'))

CONFIG_DIR = os.path.normpath(os.path.join(REPOSITORY_DIR, 'config'))

# Parse settings.conf file
config = configparser.ConfigParser()
config.read(os.path.normpath(os.path.join(CONFIG_DIR, 'settings.conf')))
config.sections()

# Get Yandex secret data from config file (or env if linux)
# yandex = {
#     'OATH_TOKEN': config['Yandex']['OATH_TOKEN'],
#     'FOLDER_ID': config['Yandex']['FOLDER_ID']
# }

# For balaboba
HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Origin': 'https://yandex.ru',
    'Referer': 'https://yandex.ru/',
}

# Import messages from messages.json
messages_filepath = os.path.normpath(os.path.join(CONFIG_DIR, 'messages.json'))
with open(messages_filepath, 'r', encoding='utf-8') as mj:
    messages_json = json.load(mj)