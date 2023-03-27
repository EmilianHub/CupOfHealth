from datetime import datetime, timedelta

import jwt

SECRET_KEY = 'secret'


def generateToken(email):
    # generowanie tokena JWT
    return jwt.encode({'email': email,
                       "exp": datetime.utcnow() + timedelta(minutes=30)},
                      SECRET_KEY,
                      algorithm='HS256')


def decodeRequest(token):
    return jwt.decode(token, SECRET_KEY, algorithms='HS256')


def encodeResponse(json):
    return jwt.encode(json, SECRET_KEY, algorithm="HS256")
