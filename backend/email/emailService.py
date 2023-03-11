from email.mime.text import MIMEText
import smtplib
import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SUBJECT = "Your CupOfHealth account password restart code"


class EmailService:
    # That makes the class Singleton
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(EmailService, cls).__new__(cls)
        return cls.__instance

    def sendEmailWithRestartCode(self, email: str, code: int):
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
