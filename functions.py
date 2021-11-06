from pynput.keyboard import Key, Controller
from time import sleep
from webbrowser import open_new_tab
from pathlib import Path
from subprocess import call
from notify2 import init, Notification
from datetime import datetime
from playsound import playsound
from random import choice
from string import ascii_letters
from re import finditer

keyboard = Controller()

encryption_dict = {
        "a": "ဂ", "b": "ဇ", "c": "⤓", "d": "⥳",
        "e": "❡", "f": "ᄑ", "g": "ᢂ", "h": "ᠷ",
        "i": "ង", "j": "ᕒ", "k": "ᔵ", "l": "ᥔ",
        "m": "ቤ", "n": "ᔇ", "o": "፨", "p": "፱",
        "q": "ᑴ", "r": "ን", "s": "᠉", "t": "ሤ",
        "u": "ᡧ", "v": "ቕ", "w": "ሠ", "x": "ᒂ",
        "y": "ᡆ", "z": "ᅆ"
    }


def notification(title, message):
    init("Utilities")
    notifier = Notification(title, message)
    notifier.show()


def sarcasm(contents):
    contents_list = []
    state = "upper"
    for i in contents:
        if state == "upper":
            contents_list.append(i.lower())
            state = "lower"
        elif state == "lower":
            contents_list.append(i.upper())
            state = "upper"

    return "".join(contents_list)


def spacer(contents):
    return " ".join(contents)


def spoilerspam(base_var):
    contents = []
    for i in base_var:
        contents.append(f"||{i}")

    return f'{"||".join(contents)}||'


def copypaste(contents):
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
        "shrug": "¯\_(ツ)_/¯", "angle symbol" : "∠"
        # fmt: on
    }
    for i in copypaste_dict:
        if contents in i:
            return copypaste_dict[i]


def titlecase(contents):
    return contents.title()


def emojify(contents):
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
    for i in contents:
        if "a" <= i.lower() <= "z":
            converted.append(f":regional_indicator_{i.lower()}:")

        elif i in special_char:
            converted.append(special_char[i])

        else:
            converted.append(i)

    return " ".join(converted)


def flipped(contents):
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
    for i in contents:
        if i in flipped_char:
            converted.append(flipped_char[i])
        else:
            converted.append(i)

    converted.reverse()
    return "".join(converted)


def exponent(contents):
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
    for i in contents:
        if i in superscript_char:
            converted.append(superscript_char[i])
        else:
            converted.append(i)

    return "".join(converted)


def fr_e():
    # invalid character error
    notification(
        "Hey!", "It seems you tried to input a character that we don't have."
    )
    exit()


def split(word):
    return [char for char in word]


def cursive(contents):
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
    for i in contents:
        if i in char:
            converted.append(char[i])
        else:
            converted.append(i)

    return "".join(converted)


def fraction(contents):
    converted = []
    char = {
        # fmt: off
        "0": ("⁰", "₀"), "1": ("¹", "₁"), "2": ("²", "₂"), 
        "3": ("³", "₃"), "4": ("⁴", "₄"), "5": ("⁵", "₅"),
        "6": ("⁶", "₆"), "7": ("⁷", "₇"), 
        "8": ("⁸", "₈"), "9": ("⁹", "₉"),
        "+": ("⁺", "₊"), "-": ("⁻", "₋"), "=": ("⁼", "₌"),
        "(": ("⁽", "₍"), ")": ("⁾", "₎"),
        "a": ("ᵃ", "ₐ"), "b": ("ᵇ", fr_e), "c": ("ᶜ", fr_e),
        "d": ("ᵈ", fr_e), "e": ("ᵉ", "ₑ"), "f": ("ᶠ", fr_e), 
        "g": ("ᵍ", fr_e), "h": ("ʰ", "ₕ"), "i": ("ⁱ", "ᵢ"), "j": ("ʲ", "ⱼ"), 
        "k": ("ᵏ", "ₖ"), "l": ("ˡ", "ₗ"), "m": ("ᵐ", "ₘ"), "n": ("ⁿ", "ₙ"),
        "o": ("ᵒ", "ₒ"), "p": ("ᵖ", "ₚ"), "r": ("ʳ", "ᵣ"), "s": ("ˢ", "ₛ"),
        "t": ("ᵗ", "ₜ"), "u": ("ᵘ", "ᵤ"), "v": ("ᵛ", "ᵥ"), "w": ("ʷ", fr_e), 
        "x": ("ˣ", "ₓ"), "y": ("ʸ", fr_e), "z": ("ᶻ", fr_e),
        # fmt: on
    }

    splitargv = split(contents[0])
    numerator = "".join(splitargv[: splitargv.index("/")])
    denominator = "".join(splitargv[splitargv.index("/") + 1 :])

    try:
        for i in char:
            for x in numerator:
                if i == x:
                    converted.append(char[i][0])

        converted.append("⁄")

        for i in char:
            for x in denominator:
                if i == x:
                    converted.append(char[i][1])

        return "".join(converted)

    except TypeError:
        fr_e()


def extend(contents):
    extendables = {
        "widepeepohappy": ":widepeepohappy1::widepeepohappy2::widepeepohappy3::widepeepohappy4:",
        "widepeeposad": ":widepeeposad1::widepeeposad2::widepeeposad3::widepeeposad4:",
    }

    for i in extendables:
        if i in contents.lower():
            return extendables[i]


def encrypt(contents):
    msg = contents.lower()
    result = ""
    for ch in msg:
        try:
            result += encryption_dict[ch]
        except KeyError:
            result += ch

    return result


def get_key(val):
    for key_, value in encryption_dict.items():
        if val == value:
            return key_

    raise KeyError


def decrypt(contents):
    msg = contents
    result = ""
    for ch in msg:
        try:
            result += get_key(ch)
        except KeyError:
            result += ch

    with keyboard.pressed(Key.backspace):
        pass
    notification("Decrypted Message", result)


def reverse(contents):
    return contents[::-1]


def alarmset(contents):
    with keyboard.pressed(Key.backspace):
        pass
    with keyboard.pressed(Key.esc):
        pass

    curr_hour = datetime.now().hour
    curr_min = datetime.now().minute
    curr_sec = datetime.now().second

    if contents[3] == "pm":
        if contents[1] != "12":
            alarm_hour = int(contents[1]) + 12
    else:
        alarm_hour = int(contents[1])
    alarm_min = int(contents[2])

    waiting_hour = alarm_hour - curr_hour
    waiting_min = alarm_min - curr_min

    if waiting_min < 0:
        waiting_min += 60

    notification("Alarm", f"Your alarm has been set for {contents[1]}:{contents[2]} {contents[3]}")

    waiting_time = (waiting_hour * 60 * 60) + (waiting_min * 60) - curr_sec
    sleep(waiting_time - 7)

    playsound(r"alarm_sound.mp3", block=False)
    notification("Alarm", "Time's up kid")


def seizure(contents):
    letters = ascii_letters
    converted = ""
    letters += " "
    for _ in range(int(contents[1])):
        converted += choice(letters)
    return converted


def formatter(contents : str):
    functions = {
        "sarcasm": sarcasm, "spacer": spacer, "spoilerspam": spoilerspam, "copypaste": copypaste,
        "cp": copypaste, "emojify": emojify, "extend": extend, "reverse": reverse,
        "exponent": exponent, "ep": exponent, "title": titlecase, "titlecase": titlecase,
        "cursive": cursive, "fraction": fraction, "fc": fraction, "encrypt": encrypt, "flip": flipped,
        "decrypt": decrypt, "exponent": exponent,
    }
    format_dict = {}
    formattables = finditer(r'\{([\w \d/]+)\}', contents)
    for i in formattables:
        func = i.groups()[0].split()[0]
        output = functions[func](" ".join(i.groups()[0].split()[1:]))
        format_dict[i.groups()[0]] = output
    
    converted = contents.format(**format_dict)
    return converted