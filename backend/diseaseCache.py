
user_msg = []
matching = {}


def addToMsgCache(msg):
    user_msg.append(msg)


def addToMatchingCache(msg, tag):
    value = matching.get(tag)
    if value is not None:
        value += [msg]
        matching[tag] = value
    else:
        matching[tag] = [msg]


def getMatchingWithTag(tag):
    result = matching.get(tag)
    if result is None:
        return []
    return result