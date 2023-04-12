from functools import wraps

from flask import Blueprint, request, jsonify

import jwtService
from userService import UserService

user = Blueprint("user", __name__)

userService = UserService()

@user.post("/send_code")
def sendRestartCode():
    args = jwtService.decodeRequest(request.get_data())
    email = args.get("email")
    return userService.sendRestartCodeToEmail(email)


@user.post("/verify_code")
def verifyRestartCode():
    args = jwtService.decodeRequest(request.get_data())
    email = args.get("email")
    code = args.get("code")
    return userService.verifyRestartCode(email, code)


@user.post("/new_password")
def updatePassword():
    args = jwtService.decodeRequest(request.get_data())
    email = args.get("email")
    password = args.get("password")
    return userService.updatePassword(email, password)


@user.post("/edit_email")
def edit_email():
    args = request.get_json()
    email = args.get("email")
    newemail = args.get("newemail")
    return userService.editemail(email,newemail)

@user.post('/loca')
def loca():
    args = request.get_json()
    woj = args.get("lat")
    miasto = args.get("long")
    choroba = args.get("choroba")
    email = args.get("email")
    return userService.saveLocalization(woj, miasto, choroba, email)

@user.post("/register")
def register():
    args = jwtService.decodeRequest(request.get_data())
    email = args.get("email")
    password = args.get("password")
    return userService.register(email, password)


@user.post("/sign_in")
def login():
    req = jwtService.decodeRequest(request.get_data())
    email = req.get('email')
    password = req.get('password')
    return userService.tryLogin(email, password)



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
        except BaseException as e:
            print(e)
            return jsonify({'error': 'Nieprawidłowy token'}), 401
        return f(*args)
    return decorated

@user.get('/protected')
@token_required
def protected():
    return jsonify({'message': 'Token JWT czuwa.'}), 200
