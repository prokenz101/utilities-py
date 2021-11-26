def copypaste(words=None, notif=True, copy=True):
    from .basicfunctions import (
        argv,
        indextest,
        copycheck,
        notification,
        notifcheck,
    )

    words = words or " ".join(argv[2:])
    indextest(
        [
            "Huh.",
            """It seems that you did not input a valid key.
If you do not know how to use this command, try running 'help cp'.""",
            5,
        ]
    )
    copypaste_dict = {
        # fmt: off
        "aigu e": "é", "aigu E": "É", "grave a": "à",
        "grave e": "è", "grave u": "ù", "grave A": "À",
        "grave E": "È", "grave U": "Ù", "chapeau a": "â",
        "chapeau e": "ê", "chapeau i": "î", "chapeau o": "ô",
        "chapeau u": "û", "chapeau A": "Â", "chapeau E": "Ê",
        "chapeau I": "Î", "chapeau O": "Ô", "chapeau U": "Û",
        "trema e": "ë", "trema i": "ï", "trema u": "ü", "bullet": "•",
        "trema E": "Ë", "trema I": "Ï", "trema U": "Ü",
        "cedille c": "ç", "cedille C": "Ç", "3164": "ㅤ",
        "hangul filler": "ㅤ", "divison": "÷", "divide": "÷", "multi": "×",
        "!=": "≠", "congruence": "≅", "greater than or equal to": "≥",
        ">=": "≥", "lesser than or equal to": "≤", "<=": "≤",
        "shrug": R"¯\_(ツ)_/¯", "trademark": "™️", "copyright": "©️",
        "music": "♩♪♫♬", "therefore": "∴", "x": "𝑥", "y": "𝑦", "csprint": """using System;

namespace Code
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("");
        }
    }
}"""
        # fmt: on
    }
    i = copypaste_dict.get(words)
    if i:
        copycheck(copy, i)
    else:
        notification(
            "Welp.",
            "It seems that utilities could not understand what word you were trying to copypaste.",
            3,
        )
        return

    notifcheck(notif, ["Success!", "Message copied to clipboard.", 2])
    return i
