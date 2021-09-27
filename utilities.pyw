from sys import argv
from functions import *

instructions = {
    "translate": translate,
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
    "encrypt": encrypt,
    "decrypt": decrypt,
    "reverse" : reverse
}
try:
    for i in instructions:
        if argv[1].lower().startswith(i):
            instructions[i]()

except Exception as e:
    notification("An Error Has Occured.", str(e), 10)
    print(e)
