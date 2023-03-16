import random
from backend.database.dbConnection import db_session
from sqlalchemy import select, update, func
import backend.userManagement.restartCodeCache as restartCodeCache
from backend.jpa.userJPA import User
from backend.email.emailService import EmailService
import re
from flask import Flask, redirect, url_for
from flask_login import LoginManager, logout_user

app = Flask(__name__)

emailService = EmailService()
passwordRegex = re.compile("^(?=.*[0-9!@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{8,}$")

login_manager=LoginManager()
login_manager.init_app(app)

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
                query = update(User).where(User.email == email).values(password=password)
                result = db_session.execute(query)
                db_session.commit()
                if result.rowcount != 0:
                    return "Password updated", 200
                return "Something gone wrong. Password has not been updated", 400
            except(Exception) as error:
                print("Error occurred while updating user: ", error)

            return "Something gone wrong. Password has not been updated", 400

        return "Password should contain at least one uppercase and one special character", 400

    def login(self,email: str, password: str):

        try:
            query=select(User).where(User.email == email).where(User.password == password)
            result =  db_session.execute(query).one()
            if result is not None:
                return 'Zalogowany', 200

            return 'Nieprawidłowy login lub hasło', 401

        except(Exception) as error:
            print(error)

        return 'Nieprawidłowy login lub hasło', 401

    def logout(self):
        logout_user()
        return redirect(url_for('/'))

