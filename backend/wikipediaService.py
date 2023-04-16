import random

import wikipedia


def findFunFactWithMessage(msg):
    wikipedia.set_lang("pl")
    titles = wikipedia.search(msg, results=3)
    print(titles)
    return wikipedia.summary(random.choice(titles), sentences=2)