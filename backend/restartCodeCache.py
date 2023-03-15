restartCodeCache = {}


def add(email: str, code: int):
    restartCodeCache[email] = code


def removeWithCode(code: int):
    for key, val in restartCodeCache.items():
        if val == code:
            restartCodeCache.pop(key)


def removeWithEmail(email: str):
    restartCodeCache.pop(email)


def getWithCode(code: int):
    for key, val in restartCodeCache.items():
        if val == code:
            return {key: restartCodeCache.get(key)}


def getWithEmail(email: str):
    return {email: restartCodeCache.get(email)}
