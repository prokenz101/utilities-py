from sys import argv
from importlib import import_module


def notification(
    title: str, subtitle: str, interval: int, icon=None, threaded=True
) -> None:
    win10toast = import_module("win10toast")
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(
        title, subtitle, icon_path=icon, duration=interval, threaded=threaded
    )


def indextest(notiflist: list, argvindex=2) -> None:
    try:
        test = argv[argvindex]
    except IndexError:
        notification(*notiflist)
        exit()


def notifcheck(notif: bool, tonotify: list) -> None:
    if notif:
        notification(*tonotify)


def copycheck(copy: bool, tocopy: str) -> None:
    if copy:
        import_module("pyperclip").copy(tocopy)


def pypercopy(tocopy: str):
    import_module("pyperclip").copy(tocopy)


def sleep(duration: float):
    import_module("time").sleep(duration)


def randint(a: int, b: int):
    return import_module("random").randint(a, b)


def call(cmd: str, shell=False):
    import_module("subprocess").call(cmd, shell=shell)


def typewrite(text: str, interval=0.0):
    import_module("pyautogui").typewrite(text, interval=interval)


def FailSafeException():
    return import_module("pyautogui").FailSafeException


def hotkey(*args, **kwargs):
    import_module("pyautogui").hotkey(*args, **kwargs)


def mouseDown(button: str, x=None, y=None):
    import_module("pyautogui").mouseDown(button=button)


def cbrt(num: float):
    return import_module("numpy").cbrt(num)


def open_new_tab(link: str):
    import_module("webbrowser").open_new_tab(link)


def lcm(*args, **kwargs):
    return import_module("math").lcm(*args, **kwargs)


def hcf_(*args, **kwargs):
    return import_module("math").gcd(*args, **kwargs)


def factorial(num: int):
    return import_module("math").factorial(num)


def Path():
    from pathlib import Path

    return Path


def finditer(expression: str, subject):
    return import_module("re").finditer(expression, subject)
