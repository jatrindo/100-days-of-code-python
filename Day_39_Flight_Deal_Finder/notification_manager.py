import os
import twilio.rest

TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_PHONE = os.environ.get("TWILIO_FROM_PHONE")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_sms_message(self, message, to_phone):
        client = twilio.rest.Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_FROM_PHONE,
            to=to_phone
        )
