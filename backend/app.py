from flask import Flask, request
from database.dbConnection import db

app = Flask(__name__)


@app.get('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.post('/<name>')
def create_user(name: str):
    collection = db.get_collection("User")
    collection.insert_one({"name": name})
    return "User added"


@app.post("/sign_in")
def sign_in(email: str):
    query_args = request.args
    email = query_args.get("email")
    password = query_args.get("password")
    return "Logged in"


if __name__ == '__main__':
    app.run()
