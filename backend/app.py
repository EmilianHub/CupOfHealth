from flask import Flask, request
from database.dbConnection import conn

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
