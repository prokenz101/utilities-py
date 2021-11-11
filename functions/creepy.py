from .basicfunctions import argv, indextest, copycheck, notifcheck


def creepy(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help creepy'.""",
            5,
        ]
    )
    converted = []
    char = {
        # fmt: off
        "a": "á̷͍̖̐̐͘", "b": "ḃ̶̢̹̖", "c": "c̸̢̧̰̙͔̲̿̈́͌̉̀͘", "d": "d̸͉͛̈́̊̍͘", "e": "ḗ̸̫̽",
        "f": "f̸̡̹̱̹̺͋͒͋", "g": "g̴̼̙̜͒̄̈́̚͝", "h": "h̴̜̕", "i": "í̸͓̬͚̘̆", "j": "j̶̯͋̋͋",
        "k": "k̴̛̰̻͈͘͘͜", "l": "l̸͔̠̝̪̯͇͐̓͆", "m": "m̴̲̗͗̽̂͌", "n": "n̸͈͇̳̈̾̿̄ͅ", "o": "o̵̧̜̖͈̲͔͂͋́͝",
        "p": "p̶̡̯̳͓̣͂̈́́͘", "q": "q̴̡͓̭̠̂͋̈́̔", "r": "r̶͍̎", "s": "s̴͈͎̙̘̱̋ͅ", "t": "ţ̶̠̜̙͚̎͗",
        "u": "ų̸̙̭͋ͅ", "v": "v̶̗͂̑̕̚", "w": "w̸͉͂̈́̅̌̊", "x": "x̴͕̞̙̮͐͐͒", "y": "ÿ̵̠͍̪̠̩́",
        "z": "z̶̞͖̓̚", "A": "A̷̡͍̩͉̱̹͑̒̀̑͝", "B": "B̵̯̭̄̀̾̑", "C": "C̷̗̽͛", "D": "D̴͖͈̯̜̭̊̓̏͆̆͘",
        "E": "Ḙ̷̦̠̍", "F": "F̶̛̮̤̈́̿̈́͂̂", "G": "Ĝ̶̨̢̺̻̹̦̅͆̈́͗", "H": "H̸̼͖̦̗͛͗͐̿̀̀ͅ", "I": "Į̶̛̩͙̭͕́̌̏̚",
        "J": "J̷̜̀͆̄͛̆", "K": "Ḵ̴̨̧̨͔̾", "L": "Ḻ̶̰̱̹͎͈̔", "M": "M̵̠̲̞̿̋̐̕̕͝", "N": "Ṅ̷̻",
        "O": "O̸̞̍̐", "P": "P̵͈͊͋͂͗͝", "Q": "Q̸̡͉̥̱͕̩̄̈́", "R": "R̵̻̺̯͗̇͜", "S": "S̴͖̬̀̇̃͋̈",
        "T": "T̵͓̫̠̈́̂̀̓́̍ͅ", "U": "Ụ̷̡͚̻͇͆͑̉͋͝", "V": "V̴̟̪͓͓̩̳̄̀͌̾̕", "W": "W̵̞̯͛̿", "X": "X̷͈͍̬́",
        "Y": "Ỳ̶̖̣͌͜", "Z": "Z̴̗͈̬̱̩̆̊͗", " ": " "
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
