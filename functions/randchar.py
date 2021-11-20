def randchar():
    from .basicfunctions import argv, indextest, pypercopy, notification

    indextest(
        [
            "Huh.",
            "It seems that you did not input any number of characters. Try 'help randchar' if you don't know what you are doing.",
            5,
        ]
    )
    try:
        num = int(argv[2])
    except ValueError:
        notification(
            "Huh.", "It seems that the number that you inputted was not a number.", 3
        )
        return
    from string import ascii_letters
    from random import choice

    converted = []
    for i in range(num):
        converted.append(choice(ascii_letters))

    pypercopy("".join(converted))
    notification("Success!", "Random characters copied to clipboard.", 2)
    return "".join(converted)
