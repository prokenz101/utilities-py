from sys import argv
from pyautogui import FailSafeException, hotkey, mouseDown, write
from time import sleep
from webbrowser import open
from pathlib import Path
from subprocess import call
from win10toast import ToastNotifier


def notification(title, subtitle, interval, icon=None, threaded=True):
    toaster = ToastNotifier()
    toaster.show_toast(title, subtitle, icon_path=icon, duration=interval)


def esc(interval=0.50):
    sleep(interval)
    hotkey("esc")
    sleep(interval)


def toenglish():
    contents = "%20".join(argv[3:])
    esc()
    open(
        f"https://translate.google.com/?sl=auto&tl=en&text={contents}&op=translate"
    )


def tofrench():
    contents = "%20".join(argv[3:])
    esc()
    open(
        f"https://translate.google.com/?sl=en&tl=fr&text={contents[0:]}&op=translate"
    )


def toarabic():
    contents = "%20".join(argv[3:])
    esc()
    open(
        f"https://translate.google.com/?sl=en&tl=ar&text={contents[0:]}&op=translate"
    )


def translate():
    languages = {
        "tofrench": tofrench,
        "f": tofrench,
        "toenglish": toenglish,
        "e": toenglish,
        "toarabic": toarabic,
        "a": toarabic,
    }
    for i in languages:
        if i == argv[2]:
            languages[i]()


def sarcasm():
    contents = " ".join(argv[2:])
    contents_list = []
    state = "upper"
    for i in contents:
        if state == "upper":
            contents_list.append(i.lower())
            state = "lower"
        elif state == "lower":
            contents_list.append(i.upper())
            state = "upper"

    write("".join(contents_list))
    esc()
    notification("Success!", "Message Typed.", 2)


def spacer():
    contents = " ".join(argv[2:])
    write(" ".join(contents))
    esc()
    notification("Success!", "Message Typed.", 2)


def spoilerspam():
    base_var = " ".join(argv[2:])
    contents = []
    for i in base_var:
        contents.append(f"||{i}")

    write(f'{"||".join(contents)}||')
    esc()
    notification("Success!", "Message Typed.", 2)


def copypaste():
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
        "shrug": "¯\_(ツ)_/¯",
        # fmt: on
    }
    for i in copypaste_dict:
        if " ".join(argv[2:]) in i:
            write(copypaste_dict[i])

    esc()
    notification("Success!", "Message Typed.", 2)


def titlecase():
    write(" ".join(argv[2:]).title())
    esc()
    notification("Success!", "Message Typed.", 2)


def emojify():
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
    for i in " ".join(argv[2:]):
        if "a" <= i.lower() <= "z":
            converted.append(f":regional_indicator_{i.lower()}:")

        elif i in special_char:
            converted.append(special_char[i])

        else:
            converted.append(i)

    write(" ".join(converted))
    esc()
    notification("Success!", "Message Typed.", 2)


def flipped():
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
    for i in " ".join(argv[2:]):
        if i in flipped_char:
            converted.append(flipped_char[i])
        else:
            converted.append(i)

    converted.reverse()
    write("".join(converted))
    esc()
    notification("Success!", "Message Typed.", 2)


def exponent():
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
    for i in " ".join(argv[2:]):
        if i in superscript_char:
            converted.append(superscript_char[i])
        else:
            converted.append(i)

    write("".join(converted))
    esc()
    notification("Success!", "Message Typed.", 2)


def fr_e():
    # invalid character error
    notification(
        "Hey!", "It seems you tried to input a character that we don't have.", 3
    )
    exit()


def split(word):
    return [char for char in word]


def cursive():
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
    for i in " ".join(argv[2:]):
        if i in char:
            converted.append(char[i])
        else:
            converted.append(i)

    write("".join(converted))
    esc()
    notification("Success!", "Message Typed.", 2)


def fraction():
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

    splitargv = split(argv[2])
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

        write("".join(converted))

    except TypeError:
        fr_e()

    esc()
    notification("Success!", "Message Typed.", 2)


def spambot():
    notification("Spamming.", "Move mouse to corner of screen to stop.", 3)
    number = argv[2]
    interval_list = argv[::-1]
    word = argv[3:]
    last_of_spam = " ".join(word[::-1])

    if "--interval=" in last_of_spam:
        word = argv[3:-1]

    if argv[2] == "infinite":
        number = 100000

    interval = 0
    if "--interval=" in interval_list[0]:
        interval = int(interval_list[0][11:])

    esc()

    try:
        for i in range(int(number)):
            write(" ".join(word))
            hotkey("enter")
            sleep(interval)
    except FailSafeException:
        notification("Spamming Stopped.", "Spamming was cancelled.", 10)


def autoclick():
    esc()
    AHKPATH = Path(
        R"C:\Users\user\Downloads\PythonFiles\utilities\AutoClicker\autoclicker.ahk"
    )
    countindex = 4
    try:
        mousebutton = argv[3].title()
    except IndexError:
        pass

    try:
        AHKPATH.touch()
    except FileExistsError:
        AHKPATH.unlink(missing_ok=True)
        sleep(0.25)
        autoclick()

    try:
        interval = int(argv[2])
    except ValueError:
        mousebutton = argv[2].title()
        countindex -= 1
        interval = 0

    try:
        count = f", {argv[countindex]}"
    except IndexError:
        count = ""

    AHKPATH.write_text(
        f"""loop{count} {{
    MouseClick, {mousebutton}
    Sleep, {interval}
}}
FileDelete C:\\Items\\Code\\utilities\\supplementary-ahks\\autoclicker.ahk
ExitApp

F7::
FileDelete C:\\Items\\Code\\utilities\\supplementary-ahks\\autoclicker.ahk
ExitApp
Return
"""
    )

    call(f"{AHKPATH}", shell=True)
    notification("Autoclicking.", "Starting autoclicker. Press F7 to close.", 3)


def tapemouse():
    esc()
    try:
        if argv[3].startswith("wait="):
            sleep(int(argv[3][5:]))
    except IndexError:
        pass
    try:
        mouseDown(button=argv[2].lower())
        notification(
            f"Taping {argv[2].title()} Mouse Button.",
            f"The {argv[2]} mouse button has been taped down.",
            3,
        )
    except FailSafeException:
        notification(
            "Couldn't Start TapeMouse.",
            "The tapemouse was stopped due to FailSafeException.",
            3,
        )


def extend():
    extendables = {
        "widepeepohappy": ":widepeepohappy1::widepeepohappy2::widepeepohappy3::widepeepohappy4:",
        "widepeeposad": ":widepeeposad1::widepeeposad2::widepeeposad3::widepeeposad4:",
    }

    for i in extendables:
        if i in " ".join(argv[2:]).lower():
            write(extendables[i])
            esc()
            notification("Success!", "Message Typed.", 2)
