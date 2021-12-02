def autoclick() -> None:
    from .basicfunctions import Path, argv, sleep, notification, call
    from pathlib import Path

    AHKPATH = Path(R"autoclicker.ahk")
    print(AHKPATH)
    countindex = 4
    try:
        mousebutton = argv[3].title()
    except IndexError:
        pass

    try:
        AHKPATH.touch()
    except FileExistsError:
        AHKPATH.unlink(missing_ok=True)
        sleep(0.25)
        autoclick()

    try:
        interval = int(argv[2])
    except ValueError:
        mousebutton = argv[2].title()
        countindex -= 1
        interval = 0

    try:
        count = f", {argv[countindex]}"
    except IndexError:
        count = ""
    AHKPATH.write_text(
        f"""loop{count} {{
    MouseClick, {mousebutton}
    Sleep, {interval}
}}
ExitApp

F7::
ExitApp
Return
"""
    )

    notification("Autoclicking.", "Starting autoclicker. Press F7 to close.", 3)
    call(f"{AHKPATH}", shell=True)
    AHKPATH.unlink(missing_ok=True)
    notification("Stopped Autoclicker.", "The autoclicker was stopped.", 3)
