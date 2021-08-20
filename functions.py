from sys import argv
from pyautogui import FailSafeException, hotkey, typewrite
from pyperclip import copy as pypercopy
from time import sleep
from webbrowser import open_new_tab
from os import system
from pathlib import Path
from win10toast import ToastNotifier


def notification(title, subtitle, interval, icon=None, threaded=True):
    toaster = ToastNotifier()
    toaster.show_toast(title, subtitle, icon_path=icon, duration=interval)


def esc(interval=0.50):
    sleep(interval)
    hotkey("esc")
    sleep(interval)


def googlesearch():
    contents = "+".join(argv[1:])
    esc()
    open_new_tab(f"https://www.google.com/search?q={contents[1:]}")


def youtubesearch():
    contents = "+".join(argv[1:])
    esc()
    open_new_tab(f"https://www.youtube.com/results?search_query={contents[8:]}")


def imagesearch():
    contents = "+".join(argv[1:])
    esc()
    open_new_tab(
        f"https://www.google.com/search?q={contents[7:]}&safe=strict&tbm=isch&sxsrf=ALeKk029ouHDkHfq3RFVc8WpFzOvZZ8s4g%3A1624376552976&source=hp&biw=1536&bih=763&ei=6ATSYIOrOduJhbIPzda7yAs&oq=hello&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyBQgAELEDMgUIABCxAzICCAA6BwgjEOoCECc6BAgjECc6CAgAELEDEIMBUNIGWKcJYLELaABwAHgAgAGPAogByAqSAQUwLjEuNZgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img&ved=0ahUKEwiDv62byqvxAhXbREEAHU3rDrkQ4dUDCAc&uact=5"
    )


def toenglish():
    contents = "%20".join(argv[2:])
    esc()
    open_new_tab(
        f"https://translate.google.com/?sl=auto&tl=en&text={contents}&op=translate"
    )


def tofrench():
    contents = "%20".join(argv[1:])
    esc()
    open_new_tab(
        f"https://translate.google.com/?sl=en&tl=fr&text={contents[11:]}&op=translate"
    )


def toarabic():
    contents = "%20".join(argv[1:])
    esc()
    open_new_tab(
        f"https://translate.google.com/?sl=en&tl=ar&text={contents[11:]}&op=translate"
    )


def sarcasm():
    contents = " ".join(argv[2:])
    contents_list = []
    state = "upper"
    for i in contents:
        if state == "upper":
            contents_list.append(i.lower())
            state = "lower"
        elif state == "lower":
            contents_list.append(i.upper())
            state = "upper"

    esc()
    pypercopy("".join(contents_list))
    notification("Success!", "Message copied to clipboard.", 2)


def spacer():
    contents = " ".join(argv[2:])
    esc()
    pypercopy(" ".join(contents))
    notification("Success!", "Message copied to clipboard.", 2)


def spoilerspam():
    base_var = " ".join(argv[2:])
    contents = []
    for i in base_var:
        contents.append(f"||{i}")

    esc()
    pypercopy(f'{"||".join(contents)}||')
    notification("Success!", "Message copied to clipboard.", 2)


def copypaste():
    copypaste_dict = {
        "aigu e": "é",
        "aigu E": "É",
        "grave a": "à",
        "grave e": "è",
        "grave u": "ù",
        "grave A": "À",
        "grave E": "È",
        "grave U": "Ù",
        "chapeau a": "â",
        "chapeau e": "ê",
        "chapeau i": "î",
        "chapeau o": "ô",
        "chapeau u": "û",
        "chapeau A": "Â",
        "chapeau E": "Ê",
        "chapeau I": "Î",
        "chapeau O": "Ô",
        "chapeau U": "Û",
        "trema e": "ë",
        "trema i": "ï",
        "trema u": "ü",
        "trema E": "Ë",
        "trema I": "Ï",
        "trema U": "Ü",
        "cedille c": "ç",
        "cedille C": "Ç",
        "3164": "ㅤ",
        "hangul filler": "ㅤ",
        "raised to 0": "⁰",
        "raised to 1": "¹",
        "square": "²",
        "cube": "³",
        "raised to 4": "⁴",
        "raised to 5": "⁵",
        "raised to 6": "⁶",
        "raised to 7": "⁷",
        "raised to 8": "⁸",
        "raised to 9": "⁹",
        "raised to n": "ⁿ",
        "divison": "÷",
        "multi": "×",
        "!=": "≠",
        "greater than or equal to": "≥",
        ">=": "≥",
        "lesser than or equal to": "≤",
        "<=": "≤",
        "shrug": "¯\_(ツ)_/¯",
    }
    for i in copypaste_dict:
        if " ".join(argv[2:]) in i:
            pypercopy(copypaste_dict[i])
            esc()
            notification("Success!", "Message copied to clipboard.", 2)


def goingidle():
    sleep(0.50)
    system("start C:\\Items\\Code\\utilities\\supplementary-ahks\\goingidle.ahk")
    sleep(12.5)
    hotkey("win", "m")


def imback():
    system("start C:\\Items\\Code\\utilities\\supplementary-ahks\\imback.ahk")


def randomaboutme():
    system("start C:\\Items\\Code\\utilities\\supplementary-ahks\\randomaboutme.ahk")


def discord():
    options = {
        "going idle": goingidle,
        "im back": imback,
        "random about me": randomaboutme,
    }

    for i in options:
        if " ".join(argv[2:]) in i:
            esc()
            options[i]()


def titlecase():
    esc()
    pypercopy(" ".join(argv[2:]).title())
    notification("Success!", "Message copied to clipboard.", 2)


def emojify():
    converted = []
    special_char = {
        " ": ":black_large_square:",
        "?": ":question:",
        "!": ":exclamation:",
        "1": ":one:",
        "2": ":two:",
        "3": ":three:",
        "4": ":four:",
        "5": ":five:",
        "6": ":six:",
        "7": ":seven:",
        "8": ":eight:",
        "9": ":nine:",
        "0": ":zero:",
    }
    for i in " ".join(argv[2:]):
        if "a" <= i.lower() <= "z":
            converted.append(f":regional_indicator_{i.lower()}:")

        elif i in special_char:
            converted.append(special_char[i])

    pypercopy(" ".join(converted))
    esc()
    notification("Success!", "Message copied to clipboard.", 2)


def spambot():
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

    esc()

    try:
        for i in range(int(number)):
            typewrite(" ".join(word))
            hotkey("enter")
            sleep(interval)
    except FailSafeException:
        notification("Spamming Stopped.", "Spamming was cancelled.", 10)


def autoclick():
    esc()
    supplement_ahk_path = Path(
        R"C:\Items\Code\utilities\supplementary-ahks\autoclicker.ahk"
    )
    countindex = 4
    try:
        mousebutton = argv[3].title()
    except IndexError:
        pass

    try:
        supplement_ahk_path.touch()
    except FileExistsError:
        supplement_ahk_path.unlink(missing_ok=True)
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

    supplement_ahk_path.write_text(f"""loop{count} {{
    MouseClick, {mousebutton}
    Sleep, {interval}
}}

ExitApp

F7::
ExitApp
Return
""")
    
    system(f"start {supplement_ahk_path}")


def extend():
    extendables = {
        "widepeepohappy": ":widepeepoHappy1::widepeepoHappy2::widepeepoHappy3::widepeepoHappy4:",
        "widepeeposad": ":widepeepoSad1::widepeepoSad2::widepeepoSad3::widePeepoSad4:",
        "widepeepoblanket": ":widepeepoBlanket1::widepeepoBlanket2::widepeepoBlanket3::widepeepoBlanket4:",
        "dogeburger": ":dogeburger1::dogeburger2::dogeburger3:",
        "amongpat": ":amongpat_green: :AmongPat_yellow: :amongpat_red:",
    }

    for i in extendables:
        if i in " ".join(argv[2:]).lower():
            pypercopy(extendables[i])
            esc()
            notification("Success!", "Message copied to clipboard.", 2)


def mcpstart(func, filepath=R"C:\Items\Code\mc-profiles\mc-profiles.pyw", params=""):
    esc()
    system(f"start {filepath} {func} {params}")


def mcprofiles():
    options = (
        "backup",
        "mcversion",
        "done?",
        "ebackup",
        "eload",
    )
    arg = argv[2]
    if arg == "load":
        mcpstart("load", params=" ".join(argv[2:]))
    elif arg in options:
        mcpstart(" ".join(argv[2:]))


# ahk modes

ahkmodes = {
    "utoyou": "\n::u::you",
    "autocorrect": Path(R"C:\Items\Code\typing-utilities\autocorrect.ahk").read_text(),
}

# incomplete
# incomplete
# incomplete

def enable():
    customahkpath = Path(R"C:\Items\Code\utilities\supplementary-ahks\customahk.ahk")
    customahkpath.touch(exist_ok=True)
    for i in ahkmodes:
        if not i in Path(R"C:\Items\Code\utilities\enabledmodes").read_text():
            if argv[3] == i:
                customahktext = customahkpath.read_text()
                customahksplit = customahktext.split("\n")
                customahksplit.append(ahkmodes[i])
                customahkpath.write_text("\n".join(customahksplit))
                enabledmodes = Path(R"C:\Items\Code\utilities\enabledmodes")
                if Path(R"C:\Items\Code\utilities\enabledmodes").read_text() == "":
                    system(
                        R"start C:\Items\Code\utilities\supplementary-ahks\customahk.ahk"
                    )

                enabledmodes.touch(exist_ok=True)
                enabledmodes.write_text(f"{enabledmodes.read_text()}\n{i}")
                notification("Enabled.", f"Enabled '{i}' mode.", 3)

        else:
            notification("Hey!", "That mode is already enabled.", 3)
            exit()


def disable():
    customahkpath = Path(R"C:\Items\Code\utilities\supplementary-ahks\customahk.ahk")
    # continue from here


def ahkclear():
    system('powershell.exe -c "Get-Process autohotkey | Stop-Process"')
    system(R"start C:\Items\Code\utilities\utilities.ahk")
    Path(R"C:\Items\Code\utilities\enabledmodes").write_text("")
    try:
        Path(R"C:\Items\Code\utilities\supplementary-ahks\customahk.ahk").unlink()
    except FileNotFoundError:
        notification("File does not exist.", "It seems that no ahk file exists.", 3)
        # notification("Cleared All Files.", "The program has deleted all AHKs.", 3)


def ahk():
    possibilities = {"enable": enable, "disable": disable, "clearall": ahkclear}
    for i in possibilities:
        if argv[2] == i:
            esc()
            possibilities[i]()
