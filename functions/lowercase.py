def lowercase(words=None, copy=True, notif=True) -> str:
    from .basicfunctions import argv, indextest, notifcheck, copycheck

    indextest(
        [
            "Huh.",
            """It appears you did not input anything for uppercase.
If you do not know what you are doing, try 'help lower'""",
            5,
        ]
    )
    words = words or " ".join(argv[2:])
    words_upper = words.lower()
    copycheck(copy, words_upper)
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return words_upper
