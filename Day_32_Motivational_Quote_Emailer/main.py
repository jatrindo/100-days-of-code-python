import datetime as dt
import os
import random
import smtplib

MY_EMAIL = "testingstuff4096@currently.com"
MY_PASSWORD = os.environ.get("YAHOO_PASS")

DEST_EMAIL = "testingstuff4096@gmail.com"
SMTP_SERVER_URL = "smtp.mail.yahoo.com"

QUOTES_FILE_PATH = "quotes.txt"
SEND_DAY_OF_WEEK = 0    # 0 = Monday, 6 = Sunday


def get_random_quote():
    with open(QUOTES_FILE_PATH, 'r') as f:
        quote = random.sample(f.readlines(), 1)[0]
    return quote


def send_email(sender_email, sender_password, sender_smtp_server_url, recipient_email, msg):
    with smtplib.SMTP(sender_smtp_server_url) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient_email,
            msg=msg
        )


current_dow = dt.datetime.now().weekday()
if current_dow == SEND_DAY_OF_WEEK:
    message = f"Subject:Motivational Quote of the Week\n\n{get_random_quote()}"
    send_email(MY_EMAIL, MY_PASSWORD, SMTP_SERVER_URL, DEST_EMAIL, message)
