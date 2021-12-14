import requests
import os
from twilio.rest import Client

api_key = os.environ.get('OWM_API_KEY')
endpoint_url = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
from_phone = os.environ.get('FROM_PHONE')
to_phone = os.environ.get('TO_PHONE')
lat = os.environ.get("LAT")
lon = os.environ.get("LON")

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(endpoint_url, params=params)
response.raise_for_status()

response_json = response.json()

hourly_projections = response_json.get("hourly")[:12]

for projection in hourly_projections:
    main_weather = projection.get('weather')[0]
    if int(main_weather.get('id')) < 700:
        print("Bring an umbrella!")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today! Remember to bring an umbrella!",
            from_=from_phone,
            to=to_phone
        )

        print(message.status)
        break
