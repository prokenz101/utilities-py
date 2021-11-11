from .basicfunctions import argv, indextest, copycheck, notifcheck


def spoilerspam(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything to spam with spoilers.
Try running 'help spoilerspam' if you do not know what you are doing.""",
            5,
        ]
    )
    contents = []
    for i in words:
        contents.append(f"||{i}")
    copycheck(copy, "".join(f'{"||".join(contents)}||'))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return f'{"||".join(contents)}||'
