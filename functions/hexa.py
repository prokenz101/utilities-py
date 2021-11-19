def totext(words: str, notif=True, copy=True):
    from .basicfunctions import notifcheck, copycheck

    text = bytearray.fromhex(words).decode()
    notifcheck(notif, ["Success!", f"The message was: {text}", 2])
    copycheck(copy, text)
    return text


def tohexa(words: str, copy=True, notif=True):
    from .basicfunctions import notifcheck, copycheck

    converted = []
    words.split()
    for i in words:
        unicode_val = ord(i)
        converted.append(hex(unicode_val)[2:])

    notifcheck(notif, ["Success!", "Hexadecimal message copied to clipboard.", 2])
    copycheck(copy, " ".join(converted))
    return " ".join(converted)


def hexadecimal(words=None, copy=True, notif=True):
    from .basicfunctions import argv, indextest

    indextest(
        [
            "Huh.",
            """It seems that you did not input anything for hexademical to work.
Try 'help hexa' if you do not know what you are doing.""",
            5,
        ]
    )
    words = words or " ".join(argv[2:])
    for i in argv[2:]:
        if len(i) == 2  and i[0].isnumeric() and not i[1] >= "g":
            totext(words, copy, notif)
        else:
            tohexa(words, copy, notif)
