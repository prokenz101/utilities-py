from .basicfunctions import argv, indextest, call, notification, hotkey


def arrowmouse() -> None:
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help arrowmouse'.""",
            5,
        ]
    )
    if argv[2] == "enable":
        call(R"start functions\arrowmouse.ahk", shell=True)
        notification(
            "Enabled.",
            "Arrow mouse has been enabled. Use 'arrowmouse disable' to disable.",
            3,
        )
    elif argv[2] == "disable":
        hotkey("f15")
        notification(
            "Disabled.",
            "Arrow mouse has been disabled.",
            3,
        )
