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
    "emojify": emojify,
    "spam": spambot,
    "extend": extend,
    "mcprofiles": mcprofiles,
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
    "cbrt": cuberoot,
    "cuberoot": cuberoot,
    "hcf": hcf,
    "gcd": hcf,
    "lcm": lcm_,
    "bubbletext": bubbletext,
    "dbs": doublestruck,
    "doublestruck": doublestruck,
    "titlecase": titlecase,
    "cursive": cursive,
    "fraction": Fraction.fraction,
    "fc": Fraction.fraction,
    "randnum": randnum,
    "randint": randnum,
    "encyrpt": LanguageModifier.encrypt,
    "ecr": LanguageModifier.encrypt,
    "flip": flipped,
    "upside-down": flipped,
    "decrypt": LanguageModifier.decrypt,
    "dcr": LanguageModifier.decrypt,
    "superscript": exponent,
    "mp": mcprofiles,
}

try:
    for i in instructions:
        if argv[1].lower().startswith(i):
            instructions[i]()

except Exception as e:
    notification("An Error Has Occured.", str(e), 10)
