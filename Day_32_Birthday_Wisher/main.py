import datetime as dt
import os
import random
import pandas
import smtplib

##################### Extra Hard Starting Project ######################
BIRTHDAYS_CSV = "birthdays.csv"
LETTER_TEMPLATE_DIR = "letter_templates"
SENDER_EMAIL = "testingstuff4096@currently.com"
SENDER_PASSWORD = os.environ.get("YAHOO_PASS")
SENDING_SMTP_SERVER_URL = "smtp.mail.yahoo.com"


def get_random_letter_template():
    random_template_path = os.path.join(
        LETTER_TEMPLATE_DIR, random.choice(os.listdir(LETTER_TEMPLATE_DIR))
    )

    with open(random_template_path, 'r') as f:
        return f.read()


def send_email(sender_email, sender_password, sending_smtp_server_url, recipient_email, msg):
    with smtplib.SMTP(sending_smtp_server_url) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=msg
        )


# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birthdays_df = pandas.read_csv(BIRTHDAYS_CSV)
todays_birthdays = birthdays_df[birthdays_df.month == now.month][birthdays_df.day == now.day]


# If step 2 is true, pick a random letter from letter templates and replace
# the [NAME] with the person's actual name from birthdays.csv
for index, row in todays_birthdays.iterrows():
    name = row.get('name')
    email = row.get('email')

    # Pick and open a random letter template
    message = get_random_letter_template()

    # Perform the replacement of [NAME]
    message = message.replace('[NAME]', name)
    message = f"Subject:Happy Birthday!\n\n{message}"

    # Send the letter generated in step 3 to that person's email address.
    send_email(SENDER_EMAIL, SENDER_PASSWORD, SENDING_SMTP_SERVER_URL, email, message)
    print(f"Sent email to {name} at {email} as {SENDER_EMAIL}")
