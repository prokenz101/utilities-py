def factorial_(words=None, notif=True, copy=True):
    from .basicfunctions import argv, notifcheck, copycheck

    try:
        words = words or argv[2]
    except IndexError:
        notifcheck(
            notif,
            [
                "Huh.",
                """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help factorial'.""",
                5,
            ],
        )
        return
    for i in words:
        try:
            n = int(words);
            i = 1;
            v = 1;

            while i <= n:
                v *= i;
                i += 1;
            
            ans = v
        except ValueError:
            notifcheck(
                notif,
                [
                    "Huh",
                    "Either the number you entered was invalid, or something has gone fatally wrong.",
                    3,
                ],
            )
            return
        copycheck(copy, str(ans))
        notifcheck(notif, [str(ans), f"The Answer is {str(ans)}", 5])
        return ans
