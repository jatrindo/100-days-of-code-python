from datetime import datetime
import os
import requests
import smtplib
import time


MY_EMAIL = "testingstuff4096@currently.com"
MY_PASSWORD = os.environ.get("YAHOO_PASS")
DEST_EMAIL = "testingstuff4096@gmail.com"
SMTP_SERVER_URL = "smtp.mail.yahoo.com"

MY_LAT = float(os.environ.get("MY_LAT"))       # Your latitude
MY_LONG = float(os.environ.get("MY_LONG"))     # Your longitude


def send_email(sender_email, sender_password, sender_smtp_server_url, recipient_email, msg):
    with smtplib.SMTP(sender_smtp_server_url) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=msg
        )


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS Lat: {iss_latitude}")
    print(f"ISS Long: {iss_longitude}")

    return abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5


def is_dark_outside():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_hour = datetime.now().hour

    return time_now_hour < sunrise_hour or time_now_hour > sunset_hour


# If the ISS is close to my current position and it is currently dark
print(f"My Lat: {MY_LAT}")
print(f"My Long: {MY_LONG}")

while True:
    if is_iss_overhead() and is_dark_outside():
        print(f"Sending email to {DEST_EMAIL}....", end='')
        # Then send me an email to tell me to look up.
        message = f"Subject:Look up! ISS Overhead\n\nGet out there and take a gander!"
        send_email(MY_EMAIL, MY_PASSWORD, SMTP_SERVER_URL, DEST_EMAIL, message)

        print("Sent!")


    # BONUS: run the code every 60 seconds.
    time.sleep(60)
