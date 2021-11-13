def exponent(words=None, notif=True, copy=True) -> str:
    from .basicfunctions import argv, indextest, copycheck, notifcheck

    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help exponent'.""",
            5,
        ]
    )
    converted = []
    superscript_char = {
        # fmt: off
        "-": "⁻", "=": "⁼", "+": "⁺",
        "1": "¹", "2": "²", "3": "³",
        "4": "⁴", "5": "⁵", "6": "⁶",
        "7": "⁷", "8": "⁸", "9": "⁹", "0": "⁰",
        "a": "ᵃ", "b": "ᵇ", "c": 'ᶜ', "d": "ᵈ", "e": "ᵉ",
        "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ",
        "k": "ᵏ", "l": "ˡ", 'm': "ᵐ", 'n': "ⁿ", 'o': "ᵒ",
        'p': "ᵖ", 'r': "ʳ", 's': "ˢ", 't': "ᵗ",'u': "ᵘ",
        'v': "ᵛ", 'w': "ʷ", 'x': "ˣ", 'y': "ʸ", 'z': "ᶻ",
        "(": "⁽", ")": "⁾", " ": " "
        # fmt: on
    }
    for i in words:
        if i in superscript_char:
            converted.append(superscript_char[i])
        else:
            converted.append(i)

    copycheck(copy, "".join(converted))
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return "".join(converted)
