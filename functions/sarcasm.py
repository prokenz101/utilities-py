from .basicfunctions import indextest, argv, copycheck, notifcheck


def sarcasm(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything to 'sarcasmize'.
Try running 'help sarcasm' if you do not know what you are doing.""",
            5,
        ]
    )
    contents_list = []
    state = "upper"
    for i in words:
        if state == "upper":
            contents_list.append(i.lower())
            state = "lower"
        elif state == "lower":
            contents_list.append(i.upper())
            state = "upper"

    copycheck(copy, "".join(contents_list))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(contents_list)
