from datetime import datetime, timedelta

import jwt
from flask import request

SECRET_KEY = 'secret'


def generateToken(email):
    # generowanie tokena JWT
    return jwt.encode({'email': email,
                       "exp": datetime.now() + timedelta(minutes=30)},
                      SECRET_KEY,
                      algorithm='HS256')


def decodeAuthorizationHeaderToken():
    token = request.headers.get('Authorization')
    if token:
        return decodeRequest(token)
    return None


def decodeLocationHeader():
    location = request.headers.get("Location")
    if location:
        return decodeRequest(location)
    return None


def decodeRequest(token):
    return jwt.decode(token, SECRET_KEY, algorithms='HS256')


def encodeResponse(json):
    return jwt.encode(json, SECRET_KEY, algorithm="HS256")
