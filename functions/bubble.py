def bubble(words=None, notif=True, copy=True) -> str:
    from .basicfunctions import argv, indextest, copycheck, notifcheck

    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help bubble'.""",
            5,
        ]
    )
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
        if i in char:
            converted.append(char[i])
        else:
            converted.append(i)

    copycheck(copy, "".join(converted))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)
