import email

import flash as flash
import password as password

from flask import Flask, render_template, jsonify, request, url_for, redirect, session

from userService import UserService
from userResource import user
from locationResource import location
from flask_cors import CORS
import processor
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash
from flask_login import login_required
from userJPA import User

import jwt
from flask import Flask, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps



app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(location, url_prefix="/location")
CORS(app)
SECRET_KEY = 'secret'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })

if __name__ == '__main__':
    app.run(debug=True, port=5000)


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

@app.route('/sign_in', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            token = generate_token(user.username)
            return jsonify({'token': token.decode('UTF-8')})
        else:
            return jsonify({'error': 'Nieprawidłowe dane logowania'}), 401
    else:
        if 'Zalogowany' in session:
            return redirect(url_for('/'))
        else:
            return render_template('/sign_in')

@app.route('/')
@login_required
def index():
    return 'Witaj, {}!'.format(current_user.username)

def generate_token(username):
    # generowanie tokena JWT
    token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
    return token

@app.route('/protected')
#@token_required
def protected():
    return jsonify({'message': 'Token JWT czuwa.'}), 200

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Brak tokenu'}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except:
            return jsonify({'error': 'Nieprawidłowy token'}), 401
        return f(*args)