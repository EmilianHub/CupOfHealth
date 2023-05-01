import random

import wikipedia


def findFunFactWithMessage(msg):
    try:
        wikipedia.set_lang("pl")
        titles = wikipedia.search(msg, results=3)
        if len(titles) > 0:
            return wikipedia.summary(random.choice(titles), sentences=2)
    except Exception as error:
        print(error)
    return "Przepraszam nie mam na to odpowiedzi"
