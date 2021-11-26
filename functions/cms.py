def cms(
    words=None, copy=True, notif=True
) -> str:  # comma seperator, seperates numbers with commas
    from .basicfunctions import argv, indextest, copycheck, notifcheck, notification

    words = words or "".join(argv[2:])
    try:
        words = int(words)
    except ValueError:
        notification("Huh.", "It appears you did not input an actual number.", 4)

    indextest(
        [
            "Huh.",
            """It seems that you didn't input anything for the comma seperator.
Try 'help cms' if you don't know what you are doing.""",
            5,
        ]
    )
    ans = f"{words:,}"
    copycheck(copy, ans)
    notifcheck(notif, ["Success!", "Number copied to clipboard.", 2])
