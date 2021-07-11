from sys import argv
from functions import *

instructions = {
    '-': googlesearch,
    'youtube': youtubesearch,
    'images': imagesearch,
    'toenglish': toenglish,
    'tofrench': tofrench,
    'toarabic': toarabic,
    'sarcasm': sarcasm,
    'spacer': spacer,
    'spoilerspam': spoilerspam,
    'copypaste': copypaste,
    'cp': copypaste,
    'discord': discord,
    'dsc': discord,
    'emojify': emojify,
    'spam': spambot
}

try:
    for i in instructions:
        if argv[1].startswith(i):
            instructions[i]()
except Exception as e:
    typewrite(e)