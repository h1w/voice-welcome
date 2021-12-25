import os
import configparser

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