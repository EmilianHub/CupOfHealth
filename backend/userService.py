import random
from dbConnection import db_session
from sqlalchemy import select, update, func
import restartCodeCache as restartCodeCache
from userJPA import User
from emailService import EmailService
import re
from chorobyJPA import Diseases

emailService = EmailService()
passwordRegex = re.compile("^(?=.*[0-9!@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=\\S+$).{8,}$")

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


    def test(self ):
        try:
            query= select(Diseases)
            result = db_session.scalars(query).fetchall()
            print(result)
        except(Exception) as error:
            print("Error")