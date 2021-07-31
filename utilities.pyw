from sys import argv
from functions import *

instructions = {
    "-": googlesearch,
    "youtube": youtubesearch,
    "images": imagesearch,
    "toenglish": toenglish,
    "tofrench": tofrench,
    "toarabic": toarabic,
    "sarcasm": sarcasm,
    "spacer": spacer,
    "spoilerspam": spoilerspam,
    "copypaste": copypaste,
    "cp": copypaste,
    "discord": discord,
    "dsc": discord,
    "emojify": emojify,
    "spam": spambot,
    "extend": extend,
    "load": load,
    "backup": backup,
    "mcversion": mcversion,
    "done?": mccheck,
}

try:
    for i in instructions:
        if argv[1].startswith(i):
            instructions[i]()
except Exception as e:
    notification("An Error Has Occured.", str(e), 30)
