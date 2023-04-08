import hashlib
import random
import re
from datetime import datetime, timedelta

from sqlalchemy import select, update

import restartCodeCache as restartCodeCache
import rsaEncryption
from chorobyJPA import Diseases
from dbConnection import db_session
from emailService import EmailService
from jwtService import decodeRequest
from userDiseaseHistoryJPA import UserDiseaseHistory
from userJPA import User

emailService = EmailService()
passwordRegex = re.compile("^(?=.*[0-9!@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{8,}$")
TOKEN_EXPIRATION_OFFSET = 30

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
            result = self.findUserWithEmail(email)
            return result is not None
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

    def register(self, email: str, password: str):

        try:
            d = hashlib.sha256(password.encode())
            hash = d.hexdigest()

            newUser = User(email=email, password=hash)
            db_session.add(newUser)
            db_session.commit()
            return "zarejestrowano", 200

        except(Exception) as error:
            print(error)

        return 'złe dane do rejestracyji ', 401

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

    def findUserWithEmail(self, email):
        return User.query.filter_by(email=email).first()

    def verifyAuthentication(self, token):
        data = decodeRequest(token)
        result = self.findUserWithEmail(data.get("email"))
        if result is None:
            return False
        return True

    def saveDiseaseHistory(self, userSymptoms: [], disease: str, token):
        try:
            symptoms = ""
            for msg in userSymptoms:
                symptoms += msg

            encryptedSymptoms = rsaEncryption.encrypt(symptoms)
            diseaseJPA = self.findDiseaseReferance(disease)
            userJPA = self.findUserWithEmail(token.get("email"))
            self.mergeHistory(encryptedSymptoms, diseaseJPA, userJPA, token)

            return "History saved", 200

        except(Exception) as error:
            print("Error while saving user history: ", error)

        return "Something gone wrong", 400

    def findDiseaseReferance(self, disease: str):
        query = select(Diseases).where(Diseases.choroba == disease)
        return db_session.scalars(query).one()

    def mergeHistory(self, symtoms, diseaseJPA, userJPA, token):
        exp = datetime.fromtimestamp(token.get("exp"))
        query = select(UserDiseaseHistory)\
            .where(UserDiseaseHistory.user_id == userJPA.id)\
            .where(UserDiseaseHistory.created + timedelta(minutes=TOKEN_EXPIRATION_OFFSET) >= exp)
        historyJPA = db_session.scalars(query).one_or_none()
        newHistoryJPA = UserDiseaseHistory(user=userJPA, user_symptoms=symtoms, disease=diseaseJPA)
        if historyJPA:
            newHistoryJPA.id = historyJPA.id

        db_session.merge(newHistoryJPA)
        db_session.commit()
