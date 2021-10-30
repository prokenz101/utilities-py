from functions import *

instructions = {
    "help": helpcenter,
    "-": Search.googlesearch,
    "youtube": Search.youtubesearch,
    "yt": Search.youtubesearch,
    "images": Search.imagesearch,
    "translate": Translate.translate,
    "sarcasm": sarcasm,
    "spacer": spacer,
    "spoilerspam": spoilerspam,
    "copypaste": copypaste,
    "cp": copypaste,
    "emojify": emojify,
    "spam": spambot,
    "autoclick": autoclick,
    "tapemouse": tapemouse,
    "reverse": reverse,
    "exponent": exponent,
    "ep": exponent,
    "remind": reminder,
    "title": titlecase,
    "arrowmouse": arrowmouse,
    "format": formatter,
    "bubble": bubbletext,
    "bubbletext": bubbletext,
    "cbrt": cuberoot,
    "cuberoot": cuberoot,
    "hcf": hcf,
    "gcd": hcf,
    "lcm": lcm_,
    "dbs": doublestruck,
    "doublestruck": doublestruck,
    "cursive": cursive,
    "fraction": Fraction.fraction,
    "fc": Fraction.fraction,
    "randnum": randnum,
    "randint": randnum,
    "flip": flipped,
    "upside-down": flipped,
    "superscript": exponent,
}

try:
    for i in instructions:
        if argv[1].lower().startswith(i):
            instructions[i]()

except Exception as e:
    notification("An Error Has Occured.", str(e), 10)
