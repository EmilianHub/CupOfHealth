import random
from backend.database.dbConnection import conn
import smtplib
import os
from enum import Enum
from dotenv import load_dotenv
from email.mime.text import MIMEText
import backend.userManagement.restartCodeCache as restartCodeCache

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SUBJECT = "Your CupOfHealth account password restart code"

class PasswordRestart:
    def tryRestartPassword(self, email: str):
        code = random.randint(1000, 9999)
        isExist = self.__isUserExist(email)
        if isExist:
            isSent = self.__sendEmailWithRestartCode(email, code)
            if isSent:
                restartCodeCache.add(email, code)
                return "Message has been send to given email"

            return "Something gone wrong, message has not been sent"

        return "User with given email doesn't exist"

    def __isUserExist(self, email: str):
        try:
            query = "select count(*) from public.user where lower(email) = %s"
            cursor = conn.cursor()
            cursor.execute(query, (email.lower(),))
            result = cursor.fetchone()
            cursor.close()

            return result[0] != 0
        except(Exception) as error:
            print("Error occurred while looking for user: ", error)

        return False

    def __sendEmailWithRestartCode(self, email: str, code: int):
        body = self.__prepareMessageBody(code)
        msg = MIMEText(body, "html")
        msg['Subject'] = SUBJECT
        msg['FROM'] = SENDER_EMAIL
        msg['To'] = email

        try:
            server = self.__prepareServerProperties()
            server.sendmail(SENDER_EMAIL, email, msg.as_string())
            server.quit()
            return MessageEnum.HAS_BEEN_SENT.value
        except(Exception) as error:
            print("Something gone wrong while sending email: ", error)

        return MessageEnum.NOT_SENT.value

    def __prepareMessageBody(self, code: int):
        return f"""
        <html>
            <body>
                <font size = 5>Your verification code to restart password:</font><br>
                <font size = 10><b>{code}<b></font><br>
                If you have received this by mistake ignore this massage.<br>
                <font size = 4>Greetings,<br>CupOfHealth team.</font>
            </body>
        </html>
        """

    def __prepareServerProperties(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        return server


class MessageEnum(Enum):
    HAS_BEEN_SENT = True
    NOT_SENT = False
