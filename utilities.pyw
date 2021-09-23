from sys import argv
from functions import *

instructions = {
    "-": Search.googlesearch,
    "youtube": Search.youtubesearch,
    "images": Search.imagesearch,
    "translate": Translate.translate,
    "sarcasm": sarcasm,
    "spacer": spacer,
    "spoilerspam": spoilerspam,
    "copypaste": copypaste,
    "cp": copypaste,
    "discord": Discord.discord,
    "dsc": Discord.discord,
    "emojify": emojify,
    "spam": spambot,
    "extend": extend,
    "mcprofiles": mcprofiles,
    "autoclick": autoclick,
    "tapemouse": tapemouse,
    "exponent": exponent,
    "ep": exponent,
    "title": titlecase,
    "titlecase": titlecase,
    "cursive": cursive,
    "fraction": Fraction.fraction,
    "fc": Fraction.fraction,
    "randnum": randnum,
    "randint": randnum,
    "encyrpt": LanguageModifier.encrypt,
    "ecr": LanguageModifier.encrypt,
    "flip": flipped,
    "decrypt": LanguageModifier.decrypt,
    "dcr": LanguageModifier.decrypt,
    "upside-down": flipped,
    "superscript": exponent,
    "mp": mcprofiles,
}

try:
    for i in instructions:
        if argv[1].lower().startswith(i):
            instructions[i]()

except Exception as e:
    notification("An Error Has Occured.", str(e), 10)
    print(e)
