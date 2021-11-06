from pynput.keyboard import Key, Controller
from pyperclip3 import copy, paste
from subprocess import call

keyboard = Controller()

with keyboard.pressed(Key.ctrl):
    keyboard.press("a")
    keyboard.release("a")
    keyboard.press("c")
    keyboard.release("c")


mod = __import__("functions")
contents = paste().decode("utf-8").split()

instruction = contents[0]
try:
    output = getattr(mod, instruction)(" ".join(contents[1:]))
    copy(output)
    with keyboard.pressed(Key.ctrl):
        keyboard.press("v")
        keyboard.release("v")

except TypeError:
    pass
except Exception as e:
    with keyboard.pressed(Key.backspace):
        pass
    getattr(mod, "notification")("An Error has Occurred.", f"{e}")
    copy(f"{e}")