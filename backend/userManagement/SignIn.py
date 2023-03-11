
from flask import Flask, request, jsonify
from select import select
from backend.jpa.userJPA import User
from backend.database.dbConnection import db_session

app = Flask(__name__)


@app.route('/sign_in', methods=['POST','OPTIONS'])
class SignIn:
    def login(self,email: str, password: str):

        data = request.json
        email = data['email']
        password = data['password']

        try:
            query=select(User).select_from(User).where(User.email == email).where(User.password == password)
            result =  db_session.execute(query).one()
            return result.count !=0

        except(Exception) as error:
            # if user is None:
            return jsonify({'error': 'Nieprawidłowy login lub hasło'}), 401
            print("Nieprawidłowe dane",error)


        token = generate_jwt_token(user['id'])
        return jsonify({'token': token.decode('UTF-8')})