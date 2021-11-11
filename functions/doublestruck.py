from .basicfunctions import argv, indextest, copycheck, notifcheck


def doublestruck(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help doublestruck'.""",
            5,
        ]
    )
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
        if i in char:
            converted.append(char[i])
        else:
            converted.append(i)

    copycheck(copy, "".join(converted))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)
