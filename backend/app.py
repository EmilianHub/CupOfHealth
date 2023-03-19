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
    return User(1, 'test@example.com', 'pbkdf2:sha256:150000$z2QbohmE$48d9f3f58484f01ec62e51785f29e1d24b1b7f2a0a69d7c9ac1283f052c7530f')



@app.route('/sign_in', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        user_jpa = User()
        user_service = UserService(user_jpa)
        user = user_service.find_user_by_username(user)
        if verify_user(email, password):
            token = generate_token(email)
            return jsonify({'token': token.decode('UTF-8')})
        else:
            return jsonify({'error': 'Nieprawidłowe dane logowania'}), 401
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('/'))
            flash('Nieprawidłowy adres e-mail lub hasło')
        else:

            session['Zalogowany'] = True
            session['username'] = user
            return redirect(url_for('index'))
    else:
        if 'Zalogowany' in session:

            return redirect(url_for('index'))
        else:
            return render_template('/sign_in')

@app.before_request
def check_user_logged_in():
    # sprawdź, czy użytkownik jest zalogowany
    if request.endpoint != 'login' and not session.get('Zalogowany'):
        return redirect(url_for('login'))

def generate_token(username):
    # generowanie tokena JWT
    token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
    return token

@app.route('/')
def index():
    # strona główna aplikacji, którą może zobaczyć tylko zalogowany użytkownik
    return 'Witaj, {}!'.format(session['username'])

@app.route('/user', methods=['GET'])
@login_required
def uuu():

    return render_template('/user')


@app.route('/logout')
@login_required
def logout():
    return redirect(url_for("/"))

def verify_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return True
    else:
        return False

def generate_token(username):
    # generowanie tokena JWT
    token = jwt.encode({'username': email}, SECRET_KEY, algorithm='HS256')
    return token

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
        return f(*args, **kwargs)
    return decorated

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'Token JWT czuwa.'})