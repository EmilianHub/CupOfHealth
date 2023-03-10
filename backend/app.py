from flask import Flask
from backend.userManagement.userResource import user

app = Flask(__name__)
app.register_blueprint(user, url_prefix="/user")

@app.get('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
