def tobinary(words, copy=True, notif=True) -> str:
    from .basicfunctions import copycheck, notifcheck

    converted = []
    for i in words:
        if i != " ":
            unicode_val = ord(i)
            converted.append(bin(unicode_val)[2:])
        else:
            converted.append("00100000")

    copycheck(copy, " ".join(converted))
    notifcheck(notif, ["Success!", "Binary message copied to clipboard.", 2])
    return " ".join(converted)


def totext(words, copy=True, notif=True) -> str:
    from .basicfunctions import copycheck, notifcheck

    words.replace("00100000", " ")
    converted = []
    words = words.split(" ")
    for i in words:
        if i != " ":
            unicode_val = int(i, 2)
            converted.append(chr(unicode_val))
        else:
            converted.append(" ")

    copycheck(copy, "".join(converted))
    notifcheck(notif, ["Success!", f"The message was: {''.join(converted)}", 10])
    return "".join(converted)


def binary(words=None, copy=True, notif=True) -> str:
    from .basicfunctions import argv, indextest

    indextest(
        [
            "Huh.",
            """It seems that you did not input any thing other than the command itself.
Try 'help binary' if you do not know what you are doing.""",
            5,
        ]
    )
    words = words or " ".join(argv[2:])
    if all(i in ("0", "1", " ") for i in words):
        var = totext(words, copy, notif)
        return var
    else:
        var = tobinary(words, copy, notif)
        return var
