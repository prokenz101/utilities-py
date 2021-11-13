def hcf(words=None, notif=True, copy=True):
    from .basicfunctions import argv, indextest, notifcheck, hcf_, copycheck

    words = words or argv[2:]
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help hcf'.""",
            5,
        ]
    )
    argv2 = []
    for i in words:
        try:
            argv2.append(int(i))
        except ValueError:
            notifcheck(
                notif,
                [
                    "Huh.",
                    "Either the number you entered was not a number, or something has gone fatally wrong.",
                    3,
                ],
            )
            return
    ans = hcf_(*argv2)
    copycheck(copy, ans)
    notifcheck(notif, [str(ans), f"The HCF is {str(ans)}", 5])
    return ans
