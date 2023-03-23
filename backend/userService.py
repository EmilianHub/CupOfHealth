import datetime
import hashlib
import random
from userDiseaseHistoryJPA import UserDiseaseHistory
from dbConnection import db_session
import re

import jwt
from flask import redirect, url_for
from flask_login import logout_user
from sqlalchemy import select, update, func

import restartCodeCache as restartCodeCache
from dbConnection import db_session
from emailService import EmailService
import re
import rsaEncryption
from chorobyJPA import Diseases
from userJPA import User

emailService = EmailService()
passwordRegex = re.compile("^(?=.*[0-9!@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{8,}$")
SECRET_KEY = 'secret'

class UserService:
    # That makes the class Singleton
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(UserService, cls).__new__(cls)
        return cls.__instance

    def sendRestartCodeToEmail(self, email: str):
        code = random.randint(1000, 9999)
        isExist = self.__isUserExist(email)
        if isExist:
            isSent = emailService.sendEmailWithRestartCode(email, code)
            if isSent:
                restartCodeCache.add(email, code)
                return "Message has been send to given email", 200

            return "Something gone wrong, message has not been sent", 400

        return "User with given email doesn't exist", 404

    def __isUserExist(self, email: str):
        try:
            query = select(func.count("*")).select_from(User).where(User.email == email)
            result = db_session.execute(query).one()
            return result.count != 0
        except(Exception) as error:
            print("Error occurred while looking for user: ", error)

        return False

    def verifyRestartCode(self, email: str, code: int):
        tempCache = restartCodeCache.getWithCode(code)
        if tempCache is not None and tempCache.keys().__contains__(email):
            return "Correct", 200
        return "Incorrect", 400

    def updatePassword(self, email: str, password: str):
        if passwordRegex.match(str(password)):
            try:
                query = update(User).where(User.email == email).values(password=hash)
                result = db_session.execute(query)
                db_session.commit()
                if result.rowcount != 0:
                    return "Password updated", 200
            except(Exception) as error:
                print("Error occurred while updating user: ", error)

            return "Something gone wrong. Password has not been updated", 400

        return "Password should contain at least one uppercase and one special character", 400

    def register (self, email: str, password: str):

        try:
            d = hashlib.sha256(password.encode())
            hash = d.hexdigest()

            newUser=User(email=email, password=hash)
            result = db_session.add(newUser)
            db_session.commit()
            return "zarejestrowano", 200

        except(Exception) as error:
            print(error)

        return 'złe dane do rejestracyji ', 401

    def editemail(self, email: str, newemail: str):

            try:
                query = update(User).where(User.email == email).values(email=newemail)
                result = db_session.execute(query)
                db_session.commit()
                if result.rowcount != 0:
                    return "emial updated", 200
                return "Something gone wrong. emial has not been updated", 400
            except(Exception) as error:
                print("Error occurred while updating user: ", error)

            return "Something gone wrong. email has not been updated", 400

    def login(self, email: str, password: str):
        try:
            query = select(User).where(User.email == email).where(User.password == password)
            result = db_session.execute(query).one()
            if result is not None:
                return 'Zalogowany', 200

            return 'Nieprawidłowy login lub hasło', 401

        except(Exception) as error:
            print(error)

        return 'Nieprawidłowy login lub hasło', 401

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def generate_token(self, email):
        # generowanie tokena JWT
        token = jwt.encode({'email': email, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm='HS256')
        return token

    def decodeToken(self, token):
        data = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        result = self.get_user_by_email(data.get("email"))
        if result is None:
            return False
        return True

    def saveDiseaseHistory(self, userId: int, userSymptoms: [], disease: str):
        try:
            symptoms = ""
            for msg in userSymptoms:
                symptoms += msg

            encryptedSymptoms = rsaEncryption.encrypt(symptoms)
            query = select(Diseases).where(Diseases.choroba == disease)
            diseaseJPA = db_session.scalars(query).one()

            history = UserDiseaseHistory(user_id=userId, user_symptoms=encryptedSymptoms, disease=diseaseJPA)
            db_session.add(history)
            db_session.commit()
            return "History saved", 200

        except(Exception) as error:
            print("Error while saving user history: ", error)

        return "Something gone wrong", 400
