from flask import Flask
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


if __name__ == '__main__':
    app.run()
