from flask import Flask, request
from backend.userManagement.passwordRestore import PasswordRestart
import backend.userManagement.restartCodeCache as restartCodeCache
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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
