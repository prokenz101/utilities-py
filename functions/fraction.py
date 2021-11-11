from .basicfunctions import notification, indextest, argv, copycheck, notifcheck


def fr_e():
    # invalid character error
    notification(
        "Hey!",
        """It seems you tried to input a character that's not supported.
For more information, please view our help center by typing 'help fc'.""",
        3,
    )
    exit()

def fraction(words=None, notif=True, copy=True) -> str:
    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help fraction'.""",
            5,
        ]
    )
    converted = []
    char: dict[str, tuple[str, str]] = {
        # fmt: off
        "0": ("⁰", "₀"), "1": ("¹", "₁"), "2": ("²", "₂"), 
        "3": ("³", "₃"), "4": ("⁴", "₄"), "5": ("⁵", "₅"),
        "6": ("⁶", "₆"), "7": ("⁷", "₇"), 
        "8": ("⁸", "₈"), "9": ("⁹", "₉"),
        "+": ("⁺", "₊"), "-": ("⁻", "₋"), "=": ("⁼", "₌"),
        "(": ("⁽", "₍"), ")": ("⁾", "₎"),
        "a": ("ᵃ", "ₐ"), "b": ("ᵇ", fr_e), "c": ("ᶜ", fr_e),
        "d": ("ᵈ", fr_e), "e": ("ᵉ", "ₑ"), "f": ("ᶠ", fr_e), 
        "g": ("ᵍ", fr_e), "h": ("ʰ", "ₕ"), "i": ("ⁱ", "ᵢ"), "j": ("ʲ", "ⱼ"), 
        "k": ("ᵏ", "ₖ"), "l": ("ˡ", "ₗ"), "m": ("ᵐ", "ₘ"), "n": ("ⁿ", "ₙ"),
        "o": ("ᵒ", "ₒ"), "p": ("ᵖ", "ₚ"), "r": ("ʳ", "ᵣ"), "s": ("ˢ", "ₛ"),
        "t": ("ᵗ", "ₜ"), "u": ("ᵘ", "ᵤ"), "v": ("ᵛ", "ᵥ"), "w": ("ʷ", fr_e),
        "x": ("ˣ", "ₓ"), "y": ("ʸ", fr_e), "z": ("ᶻ", fr_e),
        # fmt: on
    }

    slash_split = words.split("/")
    numerator = slash_split[0]
    denominator = slash_split[1]

    try:
        for x in numerator:
            i = char.get(x)
            if i:
                converted.append(i[0])

        converted.append("⁄")

        for x in denominator:
            i = char.get(x)
            if i:
                converted.append(i[1])

        copycheck(copy, "".join(converted))

    except TypeError:
        fr_e()

    errored = False
    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    if errored == False:
        return "".join(converted)
