from flask import Flask, request
from backend.userManagement.passwordRestore import PasswordRestart

app = Flask(__name__)


@app.get('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post("/")
def create_user():
    args = request.get_json()
    name = args.get("name")
    password = args.get("password")
    return f"{name} and {password}"


@app.post("/password/restart")
def restartUserPassword():
    passwordRestart = PasswordRestart()
    args = request.get_json()
    email = args.get("email")
    return passwordRestart.tryRestartPassword(email)


@app.post("/sign_in")
def sign_in(email: str):
    query_args = request.args
    email = query_args.get("email")
    password = query_args.get("password")
    return "Logged in"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
