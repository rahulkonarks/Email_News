import smtplib
import ssl

# Definition of important variables
PORT = 465
HOST = "smtp.gmail.com"
with open("/home/konarkguatam/App_Password.txt", 'r') as file:
    PASSWORD = file.read().strip('\n')
with open("/home/konarkguatam/Email.txt", 'r') as file:
    EMAIL = file.read().strip('\n')
CONTEXT = ssl.create_default_context()


def send_email(message):
    with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, EMAIL, message)