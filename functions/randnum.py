from .basicfunctions import (
    argv,
    indextest,
    copycheck,
    notifcheck,
    randint,
    notification,
)


def randnum(words=None, notif=True, copy=True):
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help randnum'.""",
            5,
        ]
    )
    words = words or list(argv[2])
    try:
        random_num = randint(int("".join(words[0:-1])), int(argv[3]))
    except ValueError:
        notification(
            "Hey!", "It seems that the number you inputted was not a number.", 3
        )
        return
    copycheck(copy, random_num)
    notifcheck(notif, [str(random_num), f"The number was: {random_num}", 3])
    return random_num
