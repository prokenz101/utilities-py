# Utilities

simple utilities that I mostly made for myself

This is a project used by very few people, and I won't be adding features that I don't want or don't need.

**Note:** This is a python script but also requires [Autohotkey](https://autohotkey.com) so make sure you have both of those.

Python modules required: [pyperclip](https://pypi.org/project/pyperclip/), [pyautogui](https://pypi.org/project/PyAutoGUI/), [win10toast](https://pypi.org/project/win10toast/) and [numpy](https://pypi.org/project/numpy/).

## Installing
### Method 1:
Download the ZIP file of utilities and extract it.
Then, open `utilities.ahk` and double check your system tray to make sure the file is really open.

### Method 2:
If you have [git](https://git-scm.com/) installed on your pc, then you can change directory to your preferred installation spot, then run:
```bash
git clone https://github.com/prokenz101/utilities
```
This is usually the preferred way of getting utilities, as if there is an update, you can just do `git pull` instead of having to download a new ZIP file each time.

### **Getting the modules required**:
Change directory to the extracted folder and run
```bash
pip install -r requirements.txt
```

Once the modules have downloaded, type any command and press F8 to trigger the script.

Pressing F8 presses Ctrl + A, however, if you do not want it to select all (like if you want utilities to only read a part of the message), then you can use shift F8. So you select the text that you want utilities to read, and then press shift + f8 to trigger utilties on that specific text. You can view the [help center](https://github.com/prokenz101/utilities/blob/main/helpcenter.md) if you still do not understand.

Open [powertoys](https://github.com/microsoft/PowerToys) and type any command to see if it works. If you do not know any commands, then visit the help center above.

Although you could use anything which allows you to type. Powertoys is not necessary.

**This branch is designed for windows only.** If you want a linux version of it, click [here](https://github.com/prokenz101/utilities/tree/linux-edition).

MacOS will most likely never be supported, as i have no plans for it, and dislike it altogether.

(Also, for some commands that open a browser, if it opens a browser that you don't want it to, then try adding your main browser to PATH in system environment variables.)
