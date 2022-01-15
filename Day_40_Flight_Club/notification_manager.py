import os
import smtplib
import twilio.rest

TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_PHONE = os.environ.get("TWILIO_FROM_PHONE")
SMTP_SERVER_URL = "smtp.mail.yahoo.com"
SMTP_SENDER_EMAIL = os.environ.get("SMTP_SENDER_EMAIL")
SMTP_SENDER_PASSWORD = os.environ.get("SMTP_SENDER_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_sms_message(self, message, to_phone):
        client = twilio.rest.Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_FROM_PHONE,
            to=to_phone
        )

    def send_emails(self, recipient_emails, message):
        for recipient_email in recipient_emails:
            with smtplib.SMTP(SMTP_SERVER_URL) as connection:
                connection.starttls()
                connection.login(user=SMTP_SENDER_EMAIL, password=SMTP_SENDER_PASSWORD)
                connection.sendmail(
                    from_addr=SMTP_SENDER_EMAIL,
                    to_addrs=recipient_email,
                    msg=message.encode("utf-8")
            )
