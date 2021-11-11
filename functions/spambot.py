from .basicfunctions import (
    notification,
    argv,
    typewrite,
    hotkey,
    sleep,
    FailSafeException,
)


def spambot() -> None:
    notification("Spamming.", "Move mouse to corner of screen to stop.", 3)
    number = argv[2]
    interval_list = argv[::-1]
    word = argv[3:]
    last_of_spam = " ".join(word[::-1])

    if "--interval=" in last_of_spam:
        word = argv[3:-1]
    if argv[2] == "infinite":
        number = 100000
    interval = 0
    if "--interval=" in interval_list[0]:
        interval = int(interval_list[0][11:])

    try:
        for i in range(int(number)):
            typewrite(" ".join(word))
            hotkey("enter")
            sleep(interval)
    except FailSafeException:
        notification(
            "Spamming Stopped.",
            "Spamming was cancelled.",
            10,
        )
