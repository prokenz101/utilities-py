from .basicfunctions import notification, indextest, argv, sleep


def reminder() -> None:
    def remind_notif(message, singular) -> None:
        if singular and message == None:
            sentence = f"Hey! You set a reminder for {argv[2][:-1]} {time_options[i][1]} and its time!"
        elif not singular and message == None:
            sentence = f"Hey! You set a reminder for {argv[2][:-1]} {time_options[i][1]}s and its time!"
        elif not message == None:
            sentence = f"Hey! Your reminder was: {message}"
        notification("Reminder!", sentence, 5)

    message = " ".join(argv[3:])
    indextest(
        [
            "Huh.",
            """It seems that you have not inputted anything at all.
If you don't know how to use the command, then run 'help remind'.""",
            5,
        ]
    )
    if message == "":
        message = None
    time_options = {"s": (1, "second"), "m": (60, "minute"), "h": (3600, "hour")}
    try:
        if float(argv[2][:-1]) == 1.0:
            one = True
        else:
            one = False
    except ValueError:
        notification("Huh.", "It seems that you have not inputted a number.", 5)

    for i in time_options:
        if argv[2].endswith(i):
            waiting_time = float(argv[2][:-1]) * time_options[i][0]
            sleep(waiting_time)
            remind_notif(message=message, singular=one)
