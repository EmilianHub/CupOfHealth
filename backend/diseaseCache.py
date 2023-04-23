user_msg = set()
matching = {}
previousResponseId = 0


def addToMsgCache(msg):
    user_msg.add(msg)


def addToMatchingCache(msg, tag):
    value = matching.get(tag)
    if value is not None:
        value.add(msg)
    else:
        matching[tag] = {msg}


def getMatchingWithTag(tag):
    result = matching.get(tag)
    if result is None:
        return []
    return result


def calculateOccurrences():
    if matching is not None and len(matching) > 0:
        occurrences = {}
        for k, v in matching.items():
            occurrences[k] = len(v)

        return occurrences
    return None

def assignReponseMessageId(id):
    global previousResponseId
    previousResponseId = id

def clearCache():
    global user_msg, matching
    user_msg = set()
    matching = {}
