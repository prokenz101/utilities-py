def helpcenter() -> None:
    from .basicfunctions import argv, notification, open_new_tab

    try:
        doubt = " ".join(argv[2:])
        test = argv[2]
    except IndexError:
        open_new_tab(
            "https://github.com/prokenz101/utilities-py/wiki/Utilities-Wiki-(Windows,-C%23-and-Python)"
        )
        return
    aliases = {
        # fmt: off
        "-": "google-search", "youtube": "youtube-search", "yt": "youtube-search",
        "images": "image-search", "cp": "copypaste", "ep": "exponent",
        "bubble": "bubbletext", "cbrt": "cube-root", "gcd": "hcf",
        "dbs": "doublestruck", "fc": "fraction", "randint": "randnum",
        "upside-down": "flip", "superscript": "exponent", "hexa": "hexadecimal",
        "cms": "commaseperator", "upper": "uppercase", "lower": "lowercase"
        # fmt: on
    }
    regularcmds = (
        # fmt: off
        "help", "translate", "sarcasm", "spacer", "spoilerspam", "copypaste",
        "emojify","spam", "autoclick", "tapemouse", "reverse", "exponent",
        "remind", "title", "arrowmouse", "format", "bubble", "cuberoot", "hcf",
        "lcm", "doublestruck", "cursive", "fraction", "randnum", "randint", "flip",
        "factorial", "creepy", "binary", "hexadecimal", "randchar", "commaseperator",
        "uppercase", "lowercase"
        # fmt: on
    )
    if doubt in aliases:
        open_new_tab(
            f"https://github.com/prokenz101/utilities-py/wiki/Utilities-Wiki-(Windows,-C%23-and-Python)#{aliases[doubt]}"
        )
        return
    else:
        if doubt in regularcmds:
            open_new_tab(
                f"https://github.com/prokenz101/utilities-py/wiki/Utilities-Wiki-(Windows,-C%23-and-Python)#{doubt}"
            )
        else:
            open_new_tab(
                "https://github.com/prokenz101/utilities-py/wiki/Utilities-Wiki-(Windows,-C%23-and-Python)"
            )
            notification(
                "Was that what you wanted?",
                f"""Unfortunately, utilities couldn't understand what you meant by '{doubt}'.
Make sure to search for the exact same command that you used normally, like 'help exponent'.""",
                10,
            )
