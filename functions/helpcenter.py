from .basicfunctions import argv, notification, open_new_tab


def helpcenter() -> None:
    try:
        doubt = " ".join(argv[2:])
        test = argv[2]
    except IndexError:
        open_new_tab("https://github.com/prokenz101/utilities/blob/main/helpcenter.md")
        return
    aliases = {
        # fmt: off
        "-": "google-search", "youtube": "youtube-search", "yt": "youtube-search",
        "images": "image-search", "cp": "copypaste", "ep": "exponent",
        "bubble": "bubbletext", "cbrt": "cube-root", "gcd": "hcf",
        "dbs": "doublestruck", "fc": "fraction", "randint": "randnum",
        "upside-down": "flip", "superscript": "exponent",
        # fmt: on
    }
    regularcmds = (
        # fmt: off
        "help", "translate", "sarcasm", "spacer", "spoilerspam", "copypaste",
        "emojify","spam", "autoclick", "tapemouse", "reverse", "exponent",
        "remind", "title", "arrowmouse", "format", "bubble", "cuberoot", "hcf",
        "lcm", "doublestruck", "cursive", "fraction", "randnum", "randint", "flip",
        "factorial", "creepy"
        # fmt: on
    )
    if doubt in aliases:
        open_new_tab(
            f"https://github.com/prokenz101/utilities/blob/main/helpcenter.md#{aliases[doubt]}"
        )
        return
    else:
        if doubt in regularcmds:
            open_new_tab(
                f"https://github.com/prokenz101/utilities/blob/main/helpcenter.md#{doubt}"
            )
        else:
            open_new_tab(
                f"https://github.com/prokenz101/utilities/blob/main/helpcenter.md"
            )
            notification(
                "Was that what you wanted?",
                f"""Unfortunately, utilities couldn't understand what you meant by '{doubt}'.
Make sure to search for the exact same command that you used normally, like 'help exponent'.""",
                10,
            )
