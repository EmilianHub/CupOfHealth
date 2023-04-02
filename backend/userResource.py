import hashlib
from functools import wraps

from flask import Blueprint, request, jsonify

import jwtService
from jwtService import generateToken
from userService import UserService

user = Blueprint("user", __name__)

userService = UserService()


@user.post("/send_code")
def sendRestartCode():
    args = request.get_json()
    email = args.get("email")
    return userService.sendRestartCodeToEmail(email)


@user.post("/verify_code")
def verifyRestartCode():
    args = request.get_json()
    email = args.get("email")
    code = args.get("code")
    return userService.verifyRestartCode(email, code)


@user.post("/new_password")
def updatePassword():
    args = request.get_json()
    email = args.get("email")
    password = args.get("password")
    return userService.updatePassword(email, password)


@user.post("/register")
def register():
    args = request.get_json()
    email = args.get("email")
    password = args.get("password")
    return userService.register(email, password)


@user.post("/sign_in")
def login():
    args = request.get_data()
    req = jwtService.decodeRequest(args)
    email = req.get('email')
    password = req.get('password')
    user = userService.findUserWithEmail(email)
    if hashlib.sha256(password.encode('utf-8')).hexdigest() == user.password:
        token = generateToken(user.email)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Nieprawidłowe dane logowania'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Brak tokenu'}), 401
        try:
            isAuthenticated = userService.verifyAuthentication(token)
            if not isAuthenticated:
                return "Invalid Token", 401
        except:
            return jsonify({'error': 'Nieprawidłowy token'}), 401
        return f(*args)
    return decorated

@user.get('/protected')
@token_required
def protected():
    return jsonify({'message': 'Token JWT czuwa.'}), 200
