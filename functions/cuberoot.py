def cuberoot(words=None, notif=True, copy=True):
    from .basicfunctions import argv, notification, cbrt, notifcheck, copycheck

    try:
        words = words or argv[2]
    except IndexError:
        notification(
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help cuberoot'.""",
            5,
        )
    try:
        ans = float(cbrt(float(words)))
    except ValueError:
        notifcheck(notif, ["Huh.", "It seems that you did not input a number.", 3])
        return

    copycheck(copy, ans)
    notifcheck(notif, [str(ans), f"The cube root is {str(ans)}", 5])
    return ans
