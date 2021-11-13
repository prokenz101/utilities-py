def spambot() -> None:
    from .basicfunctions import (
        notification,
        argv,
        typewrite,
        hotkey,
        sleep,
    )
    from pyautogui import FailSafeException

    number = argv[2]
    interval_list = argv[::-1]
    word = argv[3:]

    if "--interval=" in " ".join(word[::-1]):
        word = argv[3:-1]
    if argv[2] == "infinite":
        number = 999999999999  # 999 billion is basically infinity like cmon no one is gonna get that far
    interval = 0
    if "--interval=" in interval_list[0]:
        interval = int(interval_list[0][11:])

    try:
        notification("Spamming.", "Move mouse to corner of screen to stop.", 3)
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
