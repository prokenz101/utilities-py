from .basicfunctions import argv, indextest, copycheck, notifcheck


def spacer(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    converted = []
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything to space out.
Try running 'help spacer' if you do not know what you are doing.""",
            5,
        ]
    )
    for i in words:
        converted.append(i)
        converted.append(" ")
    copycheck(copy, "".join(converted))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)
