from sys import argv
from math import gcd, lcm, factorial
from typing import Optional
from pyautogui import FailSafeException, hotkey, typewrite, mouseDown
from pyperclip import copy as pypercopy
from time import sleep
from webbrowser import open_new_tab
from pathlib import Path
from subprocess import call
from re import finditer
from random import randint
from win10toast import ToastNotifier
from numpy import cbrt

def notification(title: str, subtitle: str, interval: int, icon=None, threaded=True) -> None:
    toaster = ToastNotifier()
    toaster.show_toast(title, subtitle, icon_path=icon, duration=interval)


def esc(interval=0.50) -> None:
    sleep(interval)
    hotkey("esc")
    sleep(interval)


def indextest(notiflist: list, argvindex=2) -> None:
    try:
        test = argv[argvindex]
    except IndexError:
        notification(*notiflist)
        exit()


def notifcheck(notif: bool, tonotify: list) -> None:
    if notif: notification(*tonotify)


def copycheck(copy: bool, tocopy) -> None:
    if copy: pypercopy(tocopy)


def helpcenter() -> None:
    try:
        doubt = " ".join(argv[2:])
        test = argv[2]
    except IndexError:
        open_new_tab("https://github.com/prokenz101/utilities/blob/main/helpcenter.md")
        return
    aliases = {
        "-": "google-search", "youtube": "youtube-search", "yt": "youtube-search",
        "images": "image-search", "cp": "copypaste", "ep": "exponent",
        "bubble": "bubbletext", "cbrt": "cube-root", "gcd": "hcf",
        "dbs": "doublestruck", "fc": "fraction", "randint": "randnum",
        "upside-down": "flip", "superscript": "exponent",
    }
    regularcmds = (
        "help", "translate", "sarcasm", "spacer", "spoilerspam", "copypaste",
        "emojify","spam", "autoclick", "tapemouse", "reverse", "exponent",
        "remind", "title", "arrowmouse", "format", "bubble", "cuberoot", "hcf",
        "lcm", "doublestruck", "cursive", "fraction", "randnum", "randint", "flip",
        "factorial"
    )
    if doubt in aliases:
        open_new_tab(f"https://github.com/prokenz101/utilities/blob/main/helpcenter.md#{aliases[doubt]}")
        return
    else:
        if doubt in regularcmds:
            open_new_tab(f"https://github.com/prokenz101/utilities/blob/main/helpcenter.md#{doubt}")
        else:
            open_new_tab(f"https://github.com/prokenz101/utilities/blob/main/helpcenter.md")
            notification(
                "Was that what you wanted?",
                f"""Unfortunately, utilities couldn't understand what you meant by '{doubt}'.
Make sure to search for the exact same command that you used normally, like 'help exponent'.""",
            10,
        )


class Search:
    @staticmethod
    def googlesearch() -> None:
        contents = "+".join(argv[1:])
        esc()
        open_new_tab(f"https://www.google.com/search?q={contents[1:]}")

    @staticmethod
    def youtubesearch() -> None:
        contents = "+".join(argv[2:])
        esc()
        open_new_tab(f"https://www.youtube.com/results?search_query={contents[0:]}")

    @staticmethod
    def imagesearch() -> None:
        contents = "+".join(argv[2:])
        esc()
        open_new_tab(
            f"https://www.google.com/search?q={contents[0:]}&safe=strict&tbm=isch&sxsrf=ALeKk029ouHDkHfq3RFVc8WpFzOvZZ8s4g%3A1624376552976&source=hp&biw=1536&bih=763&ei=6ATSYIOrOduJhbIPzda7yAs&oq=hello&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyBQgAELEDMgUIABCxAzICCAA6BwgjEOoCECc6BAgjECc6CAgAELEDEIMBUNIGWKcJYLELaABwAHgAgAGPAogByAqSAQUwLjEuNZgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img&ved=0ahUKEwiDv62byqvxAhXbREEAHU3rDrkQ4dUDCAc&uact=5"
        )


class Translate:
    @staticmethod
    def toenglish() -> None:
        contents = "%20".join(argv[3:])
        esc()
        open_new_tab(
            f"https://translate.google.com/?sl=auto&tl=en&text={contents}&op=translate"
        )

    @staticmethod
    def to_other_language(language: str) -> None:
        contents = "%20".join(argv[3:])
        esc()
        open_new_tab(f"https://translate.google.com/?sl=en&tl={language}&text={contents}&op=translate")

    @staticmethod
    def translate() -> None:
        languages = {
            ("tofrench", "french", "f"): "fr", ("toarabic", "arabic", "a"): "ar",
            ("tospanish", "spanish", "s"): "es", ("todutch", "dutch", "d"): "nl",
            ("tochinese", "chinese", "c"): "zh-TW", ("tojapanese", "japanese", "j"): "ja",
        }
        english_dict = {
            "toenglish": Translate.toenglish,
            "e": Translate.toenglish,
            "english": Translate.toenglish
        }
        if argv[2] in english_dict:
            Translate.toenglish()
        else:
            for i in languages:
                if argv[2] in i:
                    Translate.to_other_language(languages[i])


def sarcasm(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything to 'sarcasmize'.
Try running 'help sarcasm' if you do not know what you are doing.""", 5])
    contents_list = []
    state = "upper"
    for i in words:
        if state == "upper":
            contents_list.append(i.lower())
            state = "lower"
        elif state == "lower":
            contents_list.append(i.upper())
            state = "upper"
    
    copycheck(copy, "".join(contents_list))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(contents_list)


def reverse(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything to reverse.
Try running 'help reverse' if you do not know what you are doing.""", 5])
    copycheck(copy, words[::-1])
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return words[::-1]


def spacer(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything to space out.
Try running 'help spacer' if you do not know what you are doing.""", 5])
    contents = words
    copycheck(copy, " ".join(contents))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return " ".join(contents)


def spoilerspam(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything to spam with spoilers.
Try running 'help spoilerspam' if you do not know what you are doing.""", 5])
    contents = []
    for i in words: contents.append(f"||{i}")
    copycheck(copy, "".join(f'{"||".join(contents)}||'))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return f'{"||".join(contents)}||'


def randnum(words=None, notif=True, copy=True) -> Optional[int]:
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help randnum'.""", 5])
    words = words or list(argv[2])
    try: 
        random_num = randint(int("".join(words[0:-1])), int(argv[3]))
    except ValueError:
        notification(
                "Hey!", "It seems that the number you inputted was not a number.", 3
            )
        return
    copycheck(copy, random_num)
    esc()
    notifcheck(notif, [str(random_num), f"The number was: {random_num}", 3])
    return random_num


def reminder() -> None:
    esc()
    def remind_notif(message, singular) -> None:
        if singular and message == None:
            sentence = f"Hey! You set a reminder for {argv[2][:-1]} {time_options[i][1]} and its time!"
        elif not singular and message == None:
            sentence = f"Hey! You set a reminder for {argv[2][:-1]} {time_options[i][1]}s and its time!"
        elif not message == None: sentence = f"Hey! Your reminder was: {message}"
        notification("Reminder!", sentence, 5)

    message = " ".join(argv[3:])
    indextest(["Huh.", """It seems that you have not inputted anything at all.
If you don't know how to use the command, then run 'help remind'.""", 5])
    if message == "": message = None    
    time_options = {"s": (1, "second"), "m": (60, "minute"), "h": (3600, "hour")}
    try:
        if float(argv[2][:-1]) == 1.0:
            one = True
        else:
            one = False
    except ValueError:
        notification("Huh.", "It seems that you have not inputted a number.", 5)

    for i in time_options:
        if argv[2].endswith(i):
            waiting_time = float(argv[2][:-1]) * time_options[i][0]
            sleep(waiting_time)
            remind_notif(message=message, singular=one)


def copypaste(words=None, notif=True, copy=True) -> Optional[str]:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input a valid key.
If you do not know how to use this command, try running 'help cp'.""", 5])
    copypaste_dict = {
        # fmt: off
        "aigu e": "é", "aigu E": "É", "grave a": "à",
        "grave e": "è", "grave u": "ù", "grave A": "À",
        "grave E": "È", "grave U": "Ù", "chapeau a": "â",
        "chapeau e": "ê", "chapeau i": "î", "chapeau o": "ô",
        "chapeau u": "û", "chapeau A": "Â", "chapeau E": "Ê",
        "chapeau I": "Î", "chapeau O": "Ô", "chapeau U": "Û",
        "trema e": "ë", "trema i": "ï", "trema u": "ü", "bullet": "•",
        "trema E": "Ë", "trema I": "Ï", "trema U": "Ü",
        "cedille c": "ç", "cedille C": "Ç", "3164": "ㅤ",
        "hangul filler": "ㅤ", "divison": "÷", "divide": "÷", "multi": "×",
        "!=": "≠", "congruence": "≅", "greater than or equal to": "≥",
        ">=": "≥", "lesser than or equal to": "≤", "<=": "≤",
        "shrug": R"¯\_(ツ)_/¯", "trademark": "™️", "copyright": "©️",
        "music": "♩♪♫♬", "csprint": """using System;

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
    i = copypaste_dict.get(words)
    if i:
        copycheck(copy, i)
    else:
        esc()
        notification("Welp.", "It seems that utilities could not understand what word you were trying to copypaste.", 3)
        return

    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return i


def titlecase(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help title'.""", 5])
    copycheck(copy, words.title())
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    esc()
    return words.title()


def emojify(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help emojify'.""", 5])
    converted = []
    special_char = {
        " ": ":black_large_square:",
        "?": ":question:", "!": ":exclamation:", "1": ":one:",
        "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:",
        "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:", "0": ":zero:",
    }
    for i in words:
        if "a" <= i.lower() <= "z": converted.append(f":regional_indicator_{i.lower()}:")
        elif i in special_char: converted.append(special_char[i])
        else: converted.append(i)

    copycheck(copy, " ".join(converted))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return " ".join(converted)


def flipped(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help flip'.""", 5])
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
    copycheck(copy, "".join(converted))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def exponent(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help exponent'.""", 5])
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
        "(": "⁽", ")": "⁾", " ": " "
        # fmt: on
    }
    for i in words:
        if i in superscript_char: converted.append(superscript_char[i])
        else: converted.append(i)

    copycheck(copy, "".join(converted))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def cursive(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help cursive'.""", 5])
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
    for i in words:
        if i in char: converted.append(char[i])
        else: converted.append(i)

    copycheck(copy, "".join(converted))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def doublestruck(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help doublestruck'.""", 5])
    converted = []
    char = {
        # fmt: off
        "a": "𝕒", "b": "𝕓", "c": "𝕔", "d": "𝕕", "e": "𝕖",
        "f": "𝕗", "g": "𝕘", "h": "𝕙", "i": "𝕚", "j": "𝕛",
        "k": "𝕜", "l": "𝕝", "m": "𝕞", "n": "𝕟", "o" : "𝕠",
        "p": "𝕡", "q": "𝕢", "r": "𝕣", "s": "𝕤", "t": "𝕥",
        "u": "𝕦", "v": "𝕧", "w": "𝕨", "x": "𝕩", "y": "𝕪",
        "z": "𝕫", "A": "𝔸", "B": "𝔹", "C": "ℂ", "D": "𝔻",
        "E": "𝔼", "F": "𝔽", "H": "ℍ", "I": "𝕀", "J": "𝕁",
        "K": "𝕂", "L": "𝕃", "M": "𝕄", "N": "ℕ", "O": "𝕆",
        "P": "ℙ", "Q": "ℚ", "R": "ℝ", "S": "𝕊", "T": "𝕋",
        "U": "𝕌", "V": "𝕍", "W": "𝕎", "X": "𝕏", "Y": "𝕐",
        "Z": "ℤ", "1": "𝟙", "2": "𝟚", "3": "𝟛", "4": "𝟜",
        "5": "𝟝", "6": "𝟞", "7": "𝟟", "8": "𝟠", "9": "𝟡", "0": "𝟘"
        # fmt: on
    }
    for i in words:
        if i in char: converted.append(char[i])
        else: converted.append(i)

    copycheck(copy, "".join(converted))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def bubble(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help bubble'.""", 5])
    converted = []
    char = {
        # fmt: off
        "a": "ⓐ", "b": "ⓑ", "c": "ⓒ", "d": "ⓓ", "e": "ⓔ",
        "f": "ⓕ", "g": "ⓖ", "h": "ⓗ", "i": "ⓘ", "j": "ⓙ",
        "k": "ⓚ", "l": "ⓛ", "m": "ⓜ", "n": "ⓝ", "o": "ⓞ",
        "p": "ⓟ", "q": "ⓠ", "r": "ⓡ", "s": "ⓢ", "t": "ⓣ",
        "u": "ⓤ", "v": "ⓥ", "w": "ⓦ", "x": "ⓧ", "y": "ⓨ",
        "z": "ⓩ", "A": "Ⓐ", "B": "Ⓑ", "C": "Ⓒ", "D": "Ⓓ",
        "E": "Ⓔ", "F": "Ⓕ", "G": "Ⓖ", "H": "Ⓗ", "I": "Ⓘ",
        "J": "Ⓙ", "K": "Ⓚ", "L": "Ⓛ", "M": "Ⓜ", "O": "Ⓞ",
        "N": "Ⓝ", "P": "Ⓟ", "Q": "Ⓠ", "R": "Ⓡ", "S": "Ⓢ",
        "T": "Ⓣ", "U": "Ⓤ", "V": "Ⓥ", "W": "Ⓦ", "X": "Ⓧ",
        "Y": "Ⓨ", "Z": "Ⓩ", "1": "①", "2": "②", "3": "③",
        "4": "④", "5": "⑤", "6": "⑥", "7": "⑦", "8": "⑧",
        "9": "⑨", "0": "⓪"
        # fmt: on
    }
    for i in words:
        if i in char: converted.append(char[i])
        else: converted.append(i)

    copycheck(copy, "".join(converted))
    esc()
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)


def arrowmouse() -> None:
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help arrowmouse'.""", 5])
    if argv[2] == "enable":
        call(R"start supplementary-ahks\arrowmouse.ahk", shell=True)
        notification(
            "Enabled.",
            "Arrow mouse has been enabled. Use 'arrowmouse disable' to disable.",
            3,
        )
    elif argv[2] == "disable":
        hotkey("f15")
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
            "Hey!", """It seems you tried to input a character that's not supported.
For more information, please view our help center by typing 'help fc'.""", 3
        )
        exit()

    @staticmethod
    def fraction(words=None, notif=True, copy=True) -> str:
        words = words or " ".join(argv[2:])
        indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help fraction'.""", 5])
        converted = []
        char: dict[str, tuple[str, str]] = {
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
        
        slash_split = words.split('/')
        numerator = slash_split[0]
        denominator = slash_split[1]

        try:
            for x in numerator:
                i = char.get(x)
                if i: converted.append(i[0])

            converted.append("⁄")

            for x in denominator:
                i = char.get(x)
                if i: converted.append(i[1])

            copycheck(copy, "".join(converted))

        except TypeError: Fraction.fr_e()

        esc()
        errored = False
        notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
        if errored == False: return "".join(converted)


def spambot() -> None:
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


def autoclick() -> None:
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
    notification("Stopped Autoclicker.", "The autoclicker was stopped.", 3)


def tapemouse() -> None:
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


def cuberoot(words=None, notif=True, copy=True) -> Optional[float]:
    try:
        words = words or argv[2]
    except IndexError:
        notification("Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help cuberoot'.""", 5)
    try:
        ans = float(cbrt(float(words)))
    except ValueError:
        notifcheck(notif, ["Huh.", "It seems that you did not input a number.", 3])
        return
    
    copycheck(copy, ans)
    esc()
    notifcheck(notif, [str(ans), f"The cube root is {str(ans)}", 5])
    return ans


def hcf(words=None, notif=True, copy=True) -> Optional[int]:
    words = words or argv[2:]
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help hcf'.""", 5])
    argv2 = []
    for i in words:
        try:
            argv2.append(int(i))
        except ValueError:
            notifcheck(notif, [
                "Huh.",
                "Either the number you entered was not a number, or something has gone fatally wrong.",
                3,
            ]
        )
            return
    ans = gcd(*argv2)
    copycheck(copy, ans)
    esc()
    notifcheck(notif, [str(ans), f"The HCF is {str(ans)}", 5])
    return ans


def lcm_(words=None, notif=True, copy=True) -> Optional[int]:
    words = words or argv[2:]
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help lcm'.""", 5])
    argv2 = []
    for i in words:
        try:
            argv2.append(int(i))
        except ValueError:
            esc()
            notifcheck(notif, [
                "Huh.",
                "Either the number you entered was not a number, or something has gone fatally wrong.",
                3,
            ]
        )
            return
    ans = lcm(*argv2)
    copycheck(copy, ans)
    esc()
    notifcheck(notif, [str(ans), f"The LCM is {str(ans)}", 5])
    return ans


def factorial_(words=None, notif=True, copy=True) -> Optional[int]:
    try:
        words = words or argv[2]
    except IndexError:
        notifcheck(notif, ["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help factorial'.""", 5])
        return
    for i in words:
        try:
            ans = factorial(int(words))
        except ValueError:
            esc()
            notifcheck(notif, [
                "Huh",
                "Either the number you entered was invalid, or something has gone fatally wrong.",
                3,
            ]
        )
            return
        copycheck(copy, ans)
        esc()
        notifcheck(notif, [str(ans), f"The Answer is {str(ans)}", 5])
        return ans

def formatter() -> str:
    argv2 = " ".join(argv[2:])
    indextest(["Huh.", """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help format'.""", 5])
    converted = ""
    functions = {
        # fmt: off
        "sarcasm": sarcasm, "spacer": spacer, "spoilerspam": spoilerspam, "copypaste": copypaste,
        "cp": copypaste, "emojify": emojify, "reverse": reverse,
        "exponent": exponent, "ep": exponent, "title": titlecase, "titlecase": titlecase,
        "cursive": cursive, "fraction": Fraction.fraction, "fc": Fraction.fraction,
        "flip": flipped, "upside-down": flipped, "superscript": exponent,
        "bubble": bubble, "bubbletext": bubble, "doublestruck": doublestruck, "dbs": doublestruck,
        "cbrt": cuberoot, "cuberoot": cuberoot, "lcm": lcm_, "hcf": hcf, "gcd": hcf,
        "factorial": factorial_
        # fmt: on
    }
    formatdict = {}
    formattables = finditer(r'\{([\w \d/]+)\}', argv2)
    for i in formattables:
        command = i.groups()[0]
        splitcommand = command.split(" ")
        output = functions[splitcommand[0]](" ".join(splitcommand[1:]), copy=False, notif=False)
        formatdict[command] = output

    converted = argv2.format(**formatdict)
    copycheck(True, converted)
    esc()
    notifcheck(True, ["Success!", "Message copied to clipboard.", 2])
    return converted
