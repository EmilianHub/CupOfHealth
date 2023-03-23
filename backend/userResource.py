import hashlib
from functools import wraps

import jwt
from flask import Blueprint, request, redirect, url_for, session, jsonify
from flask_login import current_user, login_required, login_manager

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
@user.post("/edit_email")
def edit_email():
    args = request.get_json()
    email = args.get("email")
    newemail = args.get("newemail")
    return userService.editemail(email,newemail)



@user.post("/sign_in")
def login():
    args = request.get_json()
    email = args.get('email')
    password = args.get('password')
    user = userService.get_user_by_email(email)
    if hashlib.sha256(password.encode('utf-8')).hexdigest() == user.password:
        token = userService.generate_token(user.email)
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
            isAuthenticated = userService.decodeToken(token)
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
