def titlecase(words=None, notif=True, copy=True) -> str:
    from .basicfunctions import argv, indextest, copycheck, notifcheck

    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help title'.""",
            5,
        ]
    )
    copycheck(copy, words.title())
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return words.title()
