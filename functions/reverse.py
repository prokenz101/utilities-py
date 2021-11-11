from .basicfunctions import argv, indextest, copycheck, notifcheck


def reverse(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything to reverse.
Try running 'help reverse' if you do not know what you are doing.""",
            5,
        ]
    )
    copycheck(copy, words[::-1])
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return words[::-1]
