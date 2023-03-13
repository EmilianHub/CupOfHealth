from flask import Blueprint, request
from backend.userManagement.userService import UserService

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

@user.post("/sign_in")
def SignIn():
    args = request.get_json()
    email = args.get("email")
    password = args.get("password")
    return userService.login(email, password)
