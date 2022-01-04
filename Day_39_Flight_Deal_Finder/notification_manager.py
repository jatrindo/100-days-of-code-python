import twilio.rest


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, account_sid, auth_token, from_phone):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_phone = from_phone

    def send_sms_message(self, message, to_phone):
        client = twilio.rest.Client(self.account_sid, self.auth_token)
        client.messages.create(
            body=message,
            from_=self.from_phone,
            to=to_phone
        )
