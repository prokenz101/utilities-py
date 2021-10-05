from sys import argv
from pyautogui import FailSafeException, hotkey, typewrite, mouseDown
from pyperclip import copy as pypercopy
from time import sleep
from webbrowser import open_new_tab
from pathlib import Path
from subprocess import call
from re import finditer
from random import randint
from win10toast import ToastNotifier

def notification(title, subtitle, interval, icon=None, threaded=True):
    toaster = ToastNotifier()
    toaster.show_toast(title, subtitle, icon_path=icon, duration=interval)


def esc(interval=0.50):
    sleep(interval)
    hotkey("esc")
    sleep(interval)


def no_notifcheck(notif, tonotify):
    if notif == False: return
    elif notif: notification(tonotify[0], tonotify[1], tonotify[2])


def no_copycheck(copy, tocopy):
    if copy == False: return
    elif copy: pypercopy(tocopy)


class Search:
    @staticmethod
    def googlesearch():
        contents = "+".join(argv[1:])
        esc()
        open_new_tab(f"https://www.google.com/search?q={contents[1:]}")

    @staticmethod
    def youtubesearch():
        contents = "+".join(argv[2:])
        esc()
        open_new_tab(f"https://www.youtube.com/results?search_query={contents[0:]}")

    @staticmethod
    def imagesearch():
        contents = "+".join(argv[2:])
        esc()
        open_new_tab(
            f"https://www.google.com/search?q={contents[0:]}&safe=strict&tbm=isch&sxsrf=ALeKk029ouHDkHfq3RFVc8WpFzOvZZ8s4g%3A1624376552976&source=hp&biw=1536&bih=763&ei=6ATSYIOrOduJhbIPzda7yAs&oq=hello&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyBQgAELEDMgUIABCxAzICCAA6BwgjEOoCECc6BAgjECc6CAgAELEDEIMBUNIGWKcJYLELaABwAHgAgAGPAogByAqSAQUwLjEuNZgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img&ved=0ahUKEwiDv62byqvxAhXbREEAHU3rDrkQ4dUDCAc&uact=5"
        )


class Translate:
    @staticmethod
    def toenglish():
        contents = "%20".join(argv[3:])
        esc()
        open_new_tab(
            f"https://translate.google.com/?sl=auto&tl=en&text={contents}&op=translate"
        )

    @staticmethod
    def tofrench():
        contents = "%20".join(argv[3:])
        esc()
        open_new_tab(
            f"https://translate.google.com/?sl=en&tl=fr&text={contents[0:]}&op=translate"
        )

    @staticmethod
    def toarabic():
        contents = "%20".join(argv[3:])
        esc()
        open_new_tab(
            f"https://translate.google.com/?sl=en&tl=ar&text={contents[0:]}&op=translate"
        )

    @staticmethod
    def translate():
        languages = {
            "tofrench": Translate.tofrench,
            "f": Translate.tofrench,
            "french": Translate.tofrench,
            "toenglish": Translate.toenglish,
            "e": Translate.toenglish,
            "english": Translate.toenglish,
            "toarabic": Translate.toarabic,
            "a": Translate.toarabic,
            "arabic": Translate.toarabic,
        }
        for i in languages:
            if i == argv[2]: languages[i]()


def sarcasm(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    contents_list = []
    state = "upper"
    for i in words:
        if state == "upper":
            contents_list.append(i.lower())
            state = "lower"
        elif state == "lower":
            contents_list.append(i.upper())
            state = "upper"
    
    no_copycheck(copy, "".join(contents_list))
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(contents_list)


def reverse(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    no_copycheck(copy, words[::-1])
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])


def spacer(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    contents = words
    no_copycheck(copy, " ".join(contents))
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return " ".join(contents)


def spoilerspam(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    contents = []
    for i in words: contents.append(f"||{i}")
    no_copycheck(copy, "".join(f'{"||".join(contents)}||'))
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return f'{"||".join(contents)}||'


def randnum(num=None, notif=True, copy=True):
    num = num or list(argv[2])
    try: random_num = randint(int("".join(num[0:-1])), int(argv[3]))
    except ValueError: notification(
                "Hey!", "It seems that the number you inputted was not a number.", 3
            )
    no_copycheck(copy, random_num)
    esc()
    no_notifcheck(notif, ["Success!", f"The number was: {random_num}", 3])
    return random_num


def reminder():
    esc()
    def remind_notif(message, singular):
        if singular == True and message == None:
            sentence = f"Hey! You set a reminder for {argv[2][:-1]} {time_options[i][1]} and its time!"
        elif singular == False and message == None:
            sentence = f"Hey! You set a reminder for {argv[2][:-1]} {time_options[i][1]}s and its time!"
        elif not message == None: sentence = f"Hey! Your reminder was: {message}"

        notification("Reminder!", sentence, 5)

    message = " ".join(argv[3:])
    
    if message == "": message = None

    time_options = {"s": (1, "second"), "m": (60, "minute"), "h": (3600, "hour")}
    
    if float(argv[2][:-1]) == 1: one = True
    else: one = False

    for i in time_options:
        if argv[2].endswith(i):
            waiting_time = float(argv[2][:-1]) * time_options[i][0]
            sleep(waiting_time)
            remind_notif(message=message, singular=one)


def drinkwater(): # an alarm which reminds me to drink water every hour
    drinkwaterstate = Path(R"drinkwateron")
    if argv[2] == "enable": 
        try: drinkwaterstate.touch()
        except FileExistsError: notification("Hey!", "It seems that DrinkWater is already enabled.")
        notification("Enabled.", "You will now be reminded to drink water every 2 hours.", 3)
        while True:
            sleep(7200)
            if drinkwaterstate.exists(): notification(
                    "Drink Water!",
                    "An hour is up, it's time to go and drink water again.",
                    5
                )
            else: break
    if argv[2].lower() == "disable":
        try: drinkwaterstate.unlink()
        except FileNotFoundError:
            notification("Hey!", "It seems that DrinkWater is already disabled.", 3)
            exit()
        
        notification("Disabled.", "DrinkWater has been disabled.", 3)


def copypaste(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    copypaste_dict = {
        # fmt: off
        "aigu e": "é", "aigu E": "É", "grave a": "à",
        "grave e": "è", "grave u": "ù", "grave A": "À",
        "grave E": "È", "grave U": "Ù", "chapeau a": "â",
        "chapeau e": "ê", "chapeau i": "î", "chapeau o": "ô",
        "chapeau u": "û", "chapeau A": "Â", "chapeau E": "Ê",
        "chapeau I": "Î", "chapeau O": "Ô", "chapeau U": "Û",
        "trema e": "ë", "trema i": "ï", "trema u": "ü",
        "trema E": "Ë", "trema I": "Ï", "trema U": "Ü",
        "cedille c": "ç", "cedille C": "Ç", "3164": "ㅤ",
        "hangul filler": "ㅤ", "divison": "÷", "multi": "×",
        "!=": "≠", "congruence": "≅", "greater than or equal to": "≥",
        ">=": "≥", "lesser than or equal to": "≤", "<=": "≤",
        "shrug": "¯\_(ツ)_/¯", "trademark": "™️", "copyright": "©️",
        "csprint": """using System;

namespace Code
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("");
        }
    }
}"""
        # fmt: on
    }
    for i in copypaste_dict:
        if words in i:
            no_copycheck(copy, copypaste_dict[i])
            break

    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return copypaste_dict[i]


def titlecase(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    no_copycheck(copy, words.title())
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    esc()
    return words.title()


def emojify(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    converted = []
    special_char = {
        " ": ":black_large_square:",
        "?": ":question:",
        "!": ":exclamation:",
        "1": ":one:",
        "2": ":two:",
        "3": ":three:",
        "4": ":four:",
        "5": ":five:",
        "6": ":six:",
        "7": ":seven:",
        "8": ":eight:",
        "9": ":nine:",
        "0": ":zero:",
    }
    for i in words:
        if "a" <= i.lower() <= "z": converted.append(f":regional_indicator_{i.lower()}:")
        elif i in special_char: converted.append(special_char[i])
        else: converted.append(i)

    pypercopy(" ".join(converted))
    notification("Success!", "Message copied to clipboard.", 2)
    no_copycheck(copy, " ".join(converted))
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return " ".join(converted)


class LanguageModifier:
    @staticmethod
    def encrypt(words=None, notif=True, copy=True):
        words = words or " ".join(argv[2:])
        encrpytion_dict = {
            # fmt: off
            "a": "ဂ", "b": "ဇ", "c": "⤓", "d": "⥳",
            "e": "❡", "f": "ᄑ", "g": "ᢂ", "h": "ᠷ",
            "i": "ង", "j": "ᕒ", "k": "ᔵ", "l": "ᥔ",
            "m": "ቤ", "n": "ᔇ", "o": "፨", "p": "፱",
            "q": "ᑴ", "r": "ን", "s": "᠉", "t": "ሤ",
            "u": "ᡧ", "v": "ቕ", "w": "ሠ", "x": "ᒂ",
            "y": "ᡆ", "z": "ᅆ"
            # fmt: on
        }
        converted = []
        for i in words.lower():
            if i in encrpytion_dict: converted.append(encrpytion_dict[i])
            else: converted.append(i)

        no_copycheck(copy, "".join(converted))
        no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
        return "".join(converted)

    @staticmethod
    def decrypt(words=None, notif=True, copy=True):
        words = words or " ".join(argv[2:])
        failed_num = 0
        decrpytion_dict = {
            # fmt: off
            "ဂ": "a", "ဇ": "b", "⤓": "c", "⥳": "d",
            "❡": "e", "ᄑ": "f", "ᢂ": "g", "ᠷ": "h",
            "ង": "i", "ᕒ": "j", "ᔵ": "k", "ᥔ": "l",
            "ቤ": "m", "ᔇ": "n", "፨": "o", "፱": "p",
            "ᑴ": "q", "ን": "r", "᠉": "s", "ሤ": "t",
            "ᡧ": "u", "ቕ": "v", "ሠ": "w", "ᒂ": "x",
            "ᡆ": "y", "ᅆ": "z", " ": " "
            # fmt: on
        }
        converted = []
        for i in words:
            if i in decrpytion_dict: converted.append(decrpytion_dict[i])
            else: failed_num += 1

        no_copycheck(copy, "".join(converted))
        if failed_num == len("".join(argv[2:])): no_notifcheck(
                notif,
                [
                    "Failed.",
                    "Message could not be decrypted.",
                    3,
                ]
            )
        else: no_notifcheck(
                    notif,
                    [
                        "Message Decrypted.",
                        f" Your message was: {''.join(converted)}",
                        10,
                    ],
            )
        return "".join(converted)


def flipped(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    converted = []
    flipped_char = {
        # fmt: off
        "a": "ɐ", "b": "q", "c": 'ɔ', "d": "p", "e": "ǝ",
        "f": "ɟ", "g": "ƃ", "h": "ɥ", "i": "ᴉ", "j": "ɾ",
        "k": "ʞ", "l": "l", 'm': "ɯ", 'n': "u", 'o': "o",
        'p': "d", 'r': "ɹ", 's': "s", 't': "ʇ",'u': "n",
        'v': "ʌ", 'w': "ʍ", 'x': "x", 'y': "ʎ", 'z': "z",
        "A": "∀", "B": "q", "C": "Ɔ", "D": "p", "E": "Ǝ",
        "F": "Ⅎ", "G": "פ", "H": "H", "I": "I", "J": "ſ",
        "K": "ʞ", "L": "˥", "M": "W", "N": "N", "O": "O",
        "P": "Ԁ", "Q": "Q", "R": "ɹ", "S": "S", "T": "┴",
        "U": "∩", "V": "Λ", "W": "M", "X": "X", "Y": "⅄", "Z": "Z"
        # fmt: on
    }
    for i in words:
        if i in flipped_char: converted.append(flipped_char[i])
        else: converted.append(i)

    converted.reverse()
    no_copycheck(copy, "".join(converted))
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def exponent(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    converted = []
    superscript_char = {
        # fmt: off
        "-": "⁻", "=": "⁼", "+": "⁺",
        "1": "¹", "2": "²", "3": "³",
        "4": "⁴", "5": "⁵", "6": "⁶",
        "7": "⁷", "8": "⁸", "9": "⁹", "0": "⁰",
        "a": "ᵃ", "b": "ᵇ", "c": 'ᶜ', "d": "ᵈ", "e": "ᵉ",
        "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ",
        "k": "ᵏ", "l": "ˡ", 'm': "ᵐ", 'n': "ⁿ", 'o': "ᵒ",
        'p': "ᵖ", 'r': "ʳ", 's': "ˢ", 't': "ᵗ",'u': "ᵘ",
        'v': "ᵛ", 'w': "ʷ", 'x': "ˣ", 'y': "ʸ", 'z': "ᶻ",
        "(": "⁽", ")": "⁾"
        # fmt: on
    }
    for i in words:
        if i in superscript_char: converted.append(superscript_char[i])
        else: converted.append(i)

    no_copycheck(copy, "".join(converted))
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def cursive(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    converted = []
    char = {
        # fmt: off
        "a": "𝓪", "b": "𝓫", "c": '𝓬', "d": "𝓭", "e": "𝓮",
        "f": "𝓯", "g": "𝓰", "h": "𝓱", "i": "𝓲", "j": "𝓳",
        "k": "𝓴", "l": "𝓵", 'm': "𝓶", 'n': "𝓷", 'o': "𝓸",
        'p': "𝓹", "q": "𝓺", 'r': "𝓻", 's': "𝓼", 't': "𝓽",
        'u': "𝓾", 'v': "𝓿", 'w': "𝔀", 'x': "𝔁", 'y': "𝔂",
        "A": "𝓐", "B": "𝓑", "C": "𝓒", "D": "𝓓", "E": "𝓔", 
        "F": "𝓕", "G": "𝓖", "H": "𝓗", "I": "𝓘", "J": "𝓙",
        "K": "𝓚", "L": "𝓛", "M": "𝓜", "N": "𝓝", "O": "𝓞",
        "P": "𝓟", "Q": "𝓠", "R": "𝓡", "S": "𝓢", "T": "𝓣",
        "U": "𝓤", "V": "𝓥", "W": "𝓦", "Y": "𝓨", "X": "𝓧",
        "Z": "𝓩", 'z': "𝔃", " ": " "
        # fmt: on
    }
    base_num = 0
    for i in words:
        if i in char: converted.append(char[i])
        else: converted.append(i)

    no_copycheck(copy, "".join(converted))
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def arrowmouse():
    if argv[2] == "enable":
        call(R"start supplementary-ahks\arrowmouse.ahk", shell=True)
        notification(
            "Enabled.",
            "Arrow mouse has been enabled. Use 'arrowmouse disable' to disable.",
            3,
        )
    elif argv[2] == "disable":
        hotkey("f13")
        notification(
            "Disabled.",
            "Arrow mouse has been disabled.",
            3,
        )
    esc()


class Fraction:
    @staticmethod
    def fr_e():
        # invalid character error
        notification(
            "Hey!", "It seems you tried to input a character that we don't have.", 3
        )
        exit()

    @staticmethod
    def fraction(words=None, notif=True, copy=True):
        words = words or " ".join(argv[2:])
        converted = []
        char = {
            # fmt: off
            "0": ("⁰", "₀"), "1": ("¹", "₁"), "2": ("²", "₂"), 
            "3": ("³", "₃"), "4": ("⁴", "₄"), "5": ("⁵", "₅"),
            "6": ("⁶", "₆"), "7": ("⁷", "₇"), 
            "8": ("⁸", "₈"), "9": ("⁹", "₉"),
            "+": ("⁺", "₊"), "-": ("⁻", "₋"), "=": ("⁼", "₌"),
            "(": ("⁽", "₍"), ")": ("⁾", "₎"),
            "a": ("ᵃ", "ₐ"), "b": ("ᵇ", Fraction.fr_e), "c": ("ᶜ", Fraction.fr_e),
            "d": ("ᵈ", Fraction.fr_e), "e": ("ᵉ", "ₑ"), "f": ("ᶠ", Fraction.fr_e), 
            "g": ("ᵍ", Fraction.fr_e), "h": ("ʰ", "ₕ"), "i": ("ⁱ", "ᵢ"), "j": ("ʲ", "ⱼ"), 
            "k": ("ᵏ", "ₖ"), "l": ("ˡ", "ₗ"), "m": ("ᵐ", "ₘ"), "n": ("ⁿ", "ₙ"),
            "o": ("ᵒ", "ₒ"), "p": ("ᵖ", "ₚ"), "r": ("ʳ", "ᵣ"), "s": ("ˢ", "ₛ"),
            "t": ("ᵗ", "ₜ"), "u": ("ᵘ", "ᵤ"), "v": ("ᵛ", "ᵥ"), "w": ("ʷ", Fraction.fr_e),
            "x": ("ˣ", "ₓ"), "y": ("ʸ", Fraction.fr_e), "z": ("ᶻ", Fraction.fr_e),
            # fmt: on
        }
        splitargv = list(words)
        numerator = "".join(splitargv[: splitargv.index("/")])
        denominator = "".join(splitargv[splitargv.index("/") + 1 :])

        try:
            for i in char:
                for x in numerator:
                    if i == x: converted.append(char[i][0])

            converted.append("⁄")

            for i in char:
                for x in denominator:
                    if i == x: converted.append(char[i][1])

            no_copycheck(copy, "".join(converted))

        except TypeError: Fraction.fr_e()

        esc()
        errored = False
        no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
        if errored == False: return "".join(converted)


def spambot():
    # fmt: off
    notification("Spamming.", "Move mouse to corner of screen to stop.", 3)
    number = argv[2]
    interval_list = argv[::-1]
    word = argv[3:]
    last_of_spam = " ".join(word[::-1])

    if "--interval=" in last_of_spam: word = argv[3:-1]
    if argv[2] == "infinite": number = 100000
    interval = 0
    if "--interval=" in interval_list[0]: interval = int(interval_list[0][11:])

    esc()

    try:
        for i in range(int(number)):
            typewrite(" ".join(word))
            hotkey("enter")
            sleep(interval)
    except FailSafeException: notification(
            "Spamming Stopped.",
            "Spamming was cancelled.",
            10,
        )
    # fmt: on


def autoclick():
    # fmt: off
    esc()
    AHKPATH = Path(R"supplementary-ahks\autoclicker.ahk")
    countindex = 4
    try: mousebutton = argv[3].title()
    except IndexError: pass

    try: AHKPATH.touch()
    except FileExistsError:
        AHKPATH.unlink(missing_ok=True)
        sleep(0.25)
        autoclick()

    try: interval = int(argv[2])
    except ValueError:
        mousebutton = argv[2].title()
        countindex -= 1
        interval = 0

    try: count = f", {argv[countindex]}"
    except IndexError: count = ""
    # fmt: on
    AHKPATH.write_text(
        f"""loop{count} {{
    MouseClick, {mousebutton}
    Sleep, {interval}
}}
ExitApp

F7::
ExitApp
Return
"""
    )

    notification("Autoclicking.", "Starting autoclicker. Press F7 to close.", 3)
    call(f"{AHKPATH}", shell=True)
    AHKPATH.unlink(missing_ok=True)


def tapemouse():
    esc()
    # fmt: off
    try:
        if argv[3].startswith("wait="): sleep(int(argv[3][5:]))
    except IndexError: pass
    try:
        mouseDown(button=argv[2].lower())
        notification(
            f"Taping {argv[2].title()} Mouse Button.",
            f"The {argv[2]} mouse button has been taped down.",
            3,
        )
    except FailSafeException: notification(
                "Couldn't Start TapeMouse.",
                "The tapemouse was stopped due to FailSafeException.",
                3,
            )


def extend(words=None, notif=True, copy=True):
    words = words or " ".join(argv[2:])
    extendables = {
        "widepeepohappy": ":widepeepohappy1::widepeepohappy2::widepeepohappy3::widepeepohappy4:",
        "widepeeposad": ":widepeeposad1::widepeeposad2::widepeeposad3::widepeeposad4:",
    }

    for i in extendables:
        if i in words.lower():
            no_copycheck(copy, extendables[i])
            break
    
    esc()
    no_notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return extendables[i]


def formatter():
    argv2 = " ".join(argv[2:])
    converted = ""
    functions = {
        # fmt: off
        "sarcasm": sarcasm, "spacer": spacer, "spoilerspam": spoilerspam, "copypaste": copypaste,
        "cp": copypaste, "emojify": emojify, "extend": extend, "reverse": reverse,
        "exponent": exponent, "ep": exponent, "title": titlecase, "titlecase": titlecase,
        "cursive": cursive, "fraction": Fraction.fraction, "fc": Fraction.fraction,
        "randnum": randnum, "randint": randnum, "encyrpt": LanguageModifier.encrypt,
        "ecr": LanguageModifier.encrypt, "flip": flipped, "decrypt": LanguageModifier.decrypt,
        "dcr": LanguageModifier.decrypt, "upside-down": flipped, "superscript": exponent,
        # fmt: on
    }
    formatdict = {}
    formattables = finditer(r'\{([\w \d/]+)\}', argv2)
    for i in formattables:
        command = i.groups()[0]
        splitcommand = command.split(" ")
        output = functions[splitcommand[0]](" ".join(splitcommand[1:]), copy=False, notif=False)
        formatdict[command] = output

    converted = " ".join(argv[2:]).format(**formatdict)
    no_copycheck(True, converted)
    esc()
    no_notifcheck(True, ["Success!", "Message copied to clipboard.", 2])
    return converted


def mcprofiles():
    esc()
    if argv[2] == "done?":
        call(R"python C:\Items\Code\mc-profiles\ifexists.pyw", shell=True)
        sleep(1)
        exit()

    call(
        f"python C:\\Items\\Code\\mc-profiles\\mc-profiles.pyw {''.join(argv[2:])}",
        shell=True,
    )
