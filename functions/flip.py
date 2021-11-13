def flipped(words=None, notif=True, copy=True) -> str:
    from .basicfunctions import argv, indextest, copycheck, notifcheck

    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help flip'.""",
            5,
        ]
    )
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
        if i in flipped_char:
            converted.append(flipped_char[i])
        else:
            converted.append(i)

    converted.reverse()
    copycheck(copy, "".join(converted))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)
