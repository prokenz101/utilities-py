class Translate:
    @staticmethod
    def toenglish() -> None:
        from .basicfunctions import argv, open_new_tab

        contents = "%20".join(argv[3:])
        open_new_tab(
            f"https://translate.google.com/?sl=auto&tl=en&text={contents}&op=translate"
        )

    @staticmethod
    def to_other_language(language: str) -> None:
        from .basicfunctions import argv, open_new_tab

        contents = "%20".join(argv[3:])
        open_new_tab(
            f"https://translate.google.com/?sl=en&tl={language}&text={contents}&op=translate"
        )

    @staticmethod
    def translate() -> None:
        from .basicfunctions import argv

        languages = {
            ("tofrench", "french", "f"): "fr",
            ("toarabic", "arabic", "a"): "ar",
            ("tospanish", "spanish", "s"): "es",
            ("todutch", "dutch", "d"): "nl",
            ("tochinese", "chinese", "c"): "zh-TW",
            ("tojapanese", "japanese", "j"): "ja",
        }
        english_dict = {
            "toenglish": Translate.toenglish,
            "e": Translate.toenglish,
            "english": Translate.toenglish,
        }
        if argv[2] in english_dict:
            Translate.toenglish()
        else:
            for i in languages:
                if argv[2] in i:
                    Translate.to_other_language(languages[i])
                    break
