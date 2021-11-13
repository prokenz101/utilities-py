def emojify(words=None, notif=True, copy=True) -> str:
    from .basicfunctions import argv, indextest, copycheck, notifcheck

    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help emojify'.""",
            5,
        ]
    )
    converted = []
    special_char = {
        # fmt: off
        " ": ":black_large_square:",
        "?": ":question:", "!": ":exclamation:", "1": ":one:",
        "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:",
        "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:", "0": ":zero:",
        # fmt: on
    }
    for i in words:
        if "a" <= i.lower() <= "z":
            converted.append(f":regional_indicator_{i.lower()}:")
        elif i in special_char:
            converted.append(special_char[i])
        else:
            converted.append(i)

    copycheck(copy, " ".join(converted))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return " ".join(converted)
