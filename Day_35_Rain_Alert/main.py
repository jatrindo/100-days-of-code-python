import requests
import os

api_key = os.environ.get("OWM_API_KEY")
endpoint_url = "https://api.openweathermap.org/data/2.5/onecall"
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
        break

