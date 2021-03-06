def formatter() -> str:
    from .basicfunctions import argv, indextest, finditer, copycheck, notifcheck
    from functions import (
        # fmt: off
        bubble, copypaste,
        cuberoot, cursive, doublestruck,
        emojify, exponent, factorial,
        flip, fraction, hcf, lcm,
        randnum, reverse, sarcasm,
        spacer, spoilerspam, titlecase,
        creepy, binary, cms, uppercase,
        lowercase
        # fmt: on
    )

    text = " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input anything at all.
If you do not know how to use this command, try running 'help format'.""",
            5,
        ]
    )
    functions = {
        # fmt: off
        "sarcasm": sarcasm.sarcasm, "spacer": spacer.spacer, "spoilerspam": spoilerspam.spoilerspam,
        "copypaste": copypaste.copypaste, "cp": copypaste.copypaste, "emojify": emojify.emojify,
        "reverse": reverse.reverse, "exponent": exponent.exponent, "ep": exponent.exponent,
        "title": titlecase.titlecase, "bubble": bubble.bubble, "factorial": factorial.factorial_, 
        "cbrt": cuberoot.cuberoot, "cuberoot": cuberoot.cuberoot, "hcf": hcf.hcf, "gcd": hcf.hcf, "lcm": lcm.lcm_,
        "dbs": doublestruck.doublestruck, "doublestruck": doublestruck.doublestruck, "cursive": cursive.cursive,
        "fraction": fraction.fraction, "fc": fraction.fraction, "randnum": randnum.randnum,
        "randint": randnum.randnum, "flip": flip.flipped, "upside-down": flip.flipped, "superscript": exponent.exponent,
        "creepy": creepy.creepy, "binary": binary.binary, "commaseperator": cms.cms, "cms": cms.cms,
        "upper": uppercase.uppercase, "uppercase": uppercase.uppercase, "lower": lowercase.lowercase,
        "lowercase": lowercase.lowercase
        # fmt: on
    }
    formatdict = {}
    formattables = finditer(r"{([^}]+)}", text)
    for i in formattables:
        command = i.groups()[0]
        splitcommand = command.split(" ")
        output = functions[splitcommand[0]](
            " ".join(splitcommand[1:]), copy=False, notif=False
        )
        formatdict[command] = output

    converted = text.format(**formatdict)
    copycheck(True, converted)
    notifcheck(True, ["Success!", "Message copied to clipboard.", 2])
    return converted
