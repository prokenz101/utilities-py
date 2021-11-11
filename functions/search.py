from .basicfunctions import argv, open_new_tab


class Search:
    @staticmethod
    def googlesearch() -> None:
        contents = "+".join(argv[1:])
        open_new_tab(f"https://www.google.com/search?q={contents[1:]}")

    @staticmethod
    def youtubesearch() -> None:
        contents = "+".join(argv[2:])
        open_new_tab(f"https://www.youtube.com/results?search_query={contents[0:]}")

    @staticmethod
    def imagesearch() -> None:
        contents = "+".join(argv[2:])
        open_new_tab(
            f"https://www.google.com/search?q={contents[0:]}&safe=strict&tbm=isch&sxsrf=ALeKk029ouHDkHfq3RFVc8WpFzOvZZ8s4g%3A1624376552976&source=hp&biw=1536&bih=763&ei=6ATSYIOrOduJhbIPzda7yAs&oq=hello&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyBQgAELEDMgUIABCxAzICCAA6BwgjEOoCECc6BAgjECc6CAgAELEDEIMBUNIGWKcJYLELaABwAHgAgAGPAogByAqSAQUwLjEuNZgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img&ved=0ahUKEwiDv62byqvxAhXbREEAHU3rDrkQ4dUDCAc&uact=5"
        )
