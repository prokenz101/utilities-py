from sys import argv
from functions import *
from pyautogui import typewrite

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
    'discord': discord
}

for i in instructions:
    if argv[1].startswith(i):
        instructions[i]()