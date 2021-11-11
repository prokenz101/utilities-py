from sys import argv
from functions import (
    helpcenter, search, translate,
    sarcasm, spacer, spoilerspam,
    copypaste, emojify, spambot,
    autoclick, tapemouse, reverse,
    exponent, reminder, titlecase,
    arrowmouse, bubble, factorial,
    cuberoot, hcf, lcm, doublestruck,
    cursive, fraction, randnum,
    flip, format
)


instructions = {
    "help": helpcenter.helpcenter, "-": search.Search.googlesearch,
    "youtube": search.Search.youtubesearch, "yt": search.Search.youtubesearch,
    "images": search.Search.imagesearch, "translate": translate.Translate.translate,
    "sarcasm": sarcasm.sarcasm, "spacer": spacer.spacer, "spoilerspam": spoilerspam.spoilerspam,
    "copypaste": copypaste.copypaste, "cp": copypaste.copypaste, "emojify": emojify.emojify,
    "spam": spambot.spambot, "autoclick": autoclick.autoclick, "tapemouse": tapemouse.tapemouse,
    "reverse": reverse.reverse, "exponent": exponent.exponent, "ep": exponent.exponent,
    "remind": reminder.reminder, "title": titlecase.titlecase, "arrowmouse": arrowmouse.arrowmouse,
    "bubble": bubble.bubble, "factorial": factorial.factorial_, "cbrt": cuberoot.cuberoot,
    "cuberoot": cuberoot.cuberoot, "hcf": hcf.hcf, "gcd": hcf.hcf, "lcm": lcm.lcm_,
    "dbs": doublestruck.doublestruck, "doublestruck": doublestruck.doublestruck, "cursive": cursive.cursive,
    "fraction": fraction.fraction, "fc": fraction.fraction, "randnum": randnum.randnum,
    "randint": randnum.randnum, "flip": flip.flipped, "upside-down": flip.flipped,
    "superscript": exponent.exponent, "format": format.formatter
}

try:
    for i in instructions:
        if argv[1].lower().startswith(i):
            instructions[i]()

except Exception as e:
    from win10toast import ToastNotifier

    toaster = ToastNotifier()
    toaster.show_toast("An Error Has Occured.", str(e), duration=10)
