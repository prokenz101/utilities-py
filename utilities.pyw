from sys import argv
from functions import *

instructions = {
    "translate": translate,
    "help": help,
    "sarcasm": sarcasm,
    "spacer": spacer,
    "spoilerspam": spoilerspam,
    "copypaste": copypaste,
    "cp": copypaste,
    "emojify": emojify,
    "spam": spambot,
    "extend": extend,
    "autoclick": autoclick,
    "tapemouse": tapemouse,
    "exponent": exponent,
    "ep": exponent,
    "title": titlecase,
    "titlecase": titlecase,
    "cursive": cursive,
    "fraction": fraction,
    "fc": fraction,
    "flip": flipped,
    "upside-down": flipped,
    "superscript": exponent,
}

try:
    notification(argv[1])
    for i in instructions:
        if argv[1].lower() == i:
            instructions[i]()
            notification("func has run", interval=1)

except Exception as e:
    notification("An Error Has Occured.", str(e), 10)
    print(e)
