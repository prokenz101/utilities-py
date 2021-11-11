from .basicfunctions import argv, sleep, mouseDown, notification, FailSafeException


def tapemouse() -> None:
    try:
        if argv[3].startswith("wait="):
            sleep(int(argv[3][5:]))
    except IndexError:
        pass
    try:
        mouseDown(button=argv[2].lower())
        notification(
            f"Taping {argv[2].title()} Mouse Button.",
            f"The {argv[2]} mouse button has been taped down.",
            3,
        )
    except FailSafeException:
        notification(
            "Couldn't Start TapeMouse.",
            "The tapemouse was stopped due to FailSafeException.",
            3,
        )
