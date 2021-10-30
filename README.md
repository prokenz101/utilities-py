# Utilities

simple utilities that I mostly made for myself

Please note: This is a project used by very few people, and I won't be adding features that I don't want or don't need.

**Note:** This is a python script but also requires [Autohotkey](https://autohotkey.com) so make sure you have both of those.

Python modules required: [pyperclip](https://pypi.org/project/pyperclip/), [pyautogui](https://pypi.org/project/PyAutoGUI/), [win10toast](https://pypi.org/project/win10toast/) and [numpy](https://pypi.org/project/numpy/).

## Installing
To install the script, just download the `consumer-edition` branch as a ZIP file and extract it.

Then, open `utilities.ahk` and double check your system tray to make sure the file is really open.

### Getting the modules required:
Change directory to the extracted folder and run
```bash
pip install -r requirements.txt
```

Once the modules have downloaded, type any command and press F8 to trigger the script.

Pressing F8 presses Ctrl + A, however, if you do not want it to select all (like if you want utilities to only read a part of the message), then you can use shift F8. So you select the text that you want utilities to read, and then press shift + f8 to trigger utilties on that specific text. You can view the [help center](https://github.com/prokenz101/utilities/blob/main/helpcenter.md) if you still do not understand.

Open [powertoys](https://github.com/microsoft/PowerToys) and type 'help' to view the helpcenter. Or alternatively you could view the help center [here](https://github.com/prokenz101/utilities/blob/main/helpcenter.md).

Although you could use anything which allows you to type. Powertoys is not necessary.

This is made **for windows only.** But a linux version might be on the way ;)

(Also, for some commands that open a browser, if it opens a browser that you don't want it to, then try adding your main browser to PATH in system environment variables.)
