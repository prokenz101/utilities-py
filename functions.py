from sys import argv
from pyautogui import hotkey, typewrite
from pyperclip import copy as pypercopy
from time import sleep
from webbrowser import open_new_tab
from os import system

def help_():
    typewrite("notepad", interval=0.08)
    sleep(0.50)
    hotkey("enter")
    sleep(0.50)
    pypercopy("""Commands:

Google Search -- Open powertoys and type "-{search query}"
Youtube Search -- Open powertoys and type "youtube {search query}"
Google Images Search -- Open powertoys and type "images {search query}"
Translate -- Available Languages: French, Arabic, English | Open powertoys and type "to{language name} {query}"
Sarcasm -- Changes case of letters to be alternate (like this: hElLo) | Open powertoys and type "sarcasm {query}"
Spacer -- Adds a space in between each letter (like this: h e l l o) | Open powertoys and type "spacer {query}"
SpoilerSpam -- (Intended for discord only) Adds a ||x|| on each letter to turn it into a spoiler | Open powertoys and type "spoilerspam {query}"
Copypaste -- Copies characters that are annoying/difficult to find. Available characters: éÉàèùÀÈÙâêîôûÂÊÎÔÛëïüËÏÜçÇㅤ²³ | Open powertoys and type "copypaste {query}"
Discord Commands -- These may not work on your pc and they are intended for me, if you would like to use them, either look in the source code or too bad.
    """)
    sleep(0.50)
    hotkey("ctrl", "v")


def googlesearch():
    contents = "+".join(argv[1:])
    hotkey("esc")
    sleep(0.50)
    open_new_tab(f'https://www.google.com/search?q={contents[1:]}')


def youtubesearch():
    contents = "+".join(argv[1:])
    hotkey("esc")
    sleep(0.50)
    open_new_tab(f'https://www.youtube.com/results?search_query={contents[8:]}')

def imagesearch():
    contents = "+".join(argv[1:])
    hotkey("esc")
    sleep(0.50)
    open_new_tab(f'https://www.google.com/search?q={contents[7:]}&safe=strict&tbm=isch&sxsrf=ALeKk029ouHDkHfq3RFVc8WpFzOvZZ8s4g%3A1624376552976&source=hp&biw=1536&bih=763&ei=6ATSYIOrOduJhbIPzda7yAs&oq=hello&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyBQgAELEDMgUIABCxAzICCAA6BwgjEOoCECc6BAgjECc6CAgAELEDEIMBUNIGWKcJYLELaABwAHgAgAGPAogByAqSAQUwLjEuNZgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img&ved=0ahUKEwiDv62byqvxAhXbREEAHU3rDrkQ4dUDCAc&uact=5')


def toenglish():
    contents = "%20".join(argv[2:])
    hotkey("esc")
    sleep(0.50)
    open_new_tab(f'https://translate.google.com/?sl=auto&tl=en&text={contents}&op=translate')


def tofrench():
    contents = "%20".join(argv[1:])
    hotkey("esc")
    sleep(0.50)
    open_new_tab(f'https://translate.google.com/?sl=en&tl=fr&text={contents[11:]}&op=translate')


def toarabic():
    contents = "%20".join(argv[1:])
    hotkey("esc")
    sleep(0.50)
    open_new_tab(f'https://translate.google.com/?sl=en&tl=ar&text={contents[11:]}&op=translate')


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

    hotkey("esc")
    sleep(0.50)
    pypercopy("".join(contents_list))


def spacer():
    contents = " ".join(argv[2:])
    hotkey("esc")
    sleep(0.50)
    pypercopy(" ".join(contents))


def spoilerspam():
    base_var = " ".join(argv[2:])
    contents = []
    for i in base_var:
        contents.append(f'||{i}')
    
    hotkey("esc")
    sleep(0.50)
    pypercopy(f'{"||".join(contents)}||')


def copypaste():
    copypaste_dict = {
        'aigu e': 'é',
        'aigu E': 'É',
        'grave a': 'à',
        'grave e': 'è',
        'grave u': 'ù',
        'grave A': 'À',
        'grave E': 'È',
        'grave U': 'Ù',
        'chapeau a': 'â',
        'chapeau e': 'ê',
        'chapeau i': 'î',
        'chapeau o': 'ô',
        'chapeau u': 'û',
        'chapeau A': 'Â',
        'chapeau E': 'Ê',
        'chapeau I': 'Î',
        'chapeau O': 'Ô',
        'chapeau U': 'Û',
        'trema e': 'ë',
        'trema i': 'ï',
        'trema u': 'ü',
        'trema E': 'Ë',
        'trema I': 'Ï',
        'trema U': 'Ü',
        'cedille c': 'ç',
        'cedille C': 'Ç',
        '3164': 'ㅤ',
        'hangul filler': 'ㅤ',
        'square': '²',
        'cube': '³',
        'divison': '÷',
        'multi': '×',
        '!=': '≠'
    }
    for i in copypaste_dict:
        if " ".join(argv[2:]) in i:
            pypercopy(copypaste_dict[i])
            sleep(0.50)
            hotkey("esc")


def goingidle():
    sleep(0.50)
    system("start C:\Items\Code\powertoys-utilities\supplementary-ahks\goingidle.ahk")
    


def imback():
    system("start C:\Items\Code\powertoys-utilities\supplementary-ahks\imback.ahk")


def discord():
    options = {
        'going idle': goingidle,
        'im back': imback
    }

    for i in options:
        if " ".join(argv[2:]) in i:
            hotkey("esc")
            sleep(0.50)
            options[i]()

def emojify():
    converted = []
    special_char = {
        ' ': ':black_large_square:',
        '?': ':question:',
        '!': ':exclamation:',
        '1': ':one:',
        '2': ':two:',
        '3': ':three:',
        '4': ':four:',
        '5': ':five:',
        '6': ':six:',
        '7': ':seven:',
        '8': ':eight:',
        '9': ':nine:',
        '0': ':zero:'
    }
    for i in " ".join(argv[2:]):
        if 'a' <= i.lower() <= 'z':
            converted.append(f':regional_indicator_{i.lower()}:')
        
        elif i in special_char:
            converted.append(special_char[i])
            
    pypercopy(" ".join(converted))
    sleep(0.25)
    hotkey("esc")