import json
import os
import requests
import datetime as dt

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")

# query = input("Tell me which exercises you did: ")
# debug
query = "Ran 5 km"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_endpoint_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

exercise_endpoint_params = {
    "query": query,
}

response = requests.post(url=exercise_endpoint, headers=exercise_endpoint_headers, json=exercise_endpoint_params)
response.raise_for_status()
exercises = response.json().get("exercises")

for exercise in exercises:
    # Add result to Google Sheet
    sheet_endpoint_url = SHEETY_ENDPOINT

    sheet_endpoint_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
    }

    date_str = dt.datetime.today().strftime("%d/%m/%Y")
    hour_str = dt.datetime.now().strftime("%X")

    sheet_endpoint_params = {
        "workout": {
            "date": date_str,
            "time": hour_str,
            "exercise": exercise.get("name").title(),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories"),
        }
    }

    print(sheet_endpoint_params)
    response = requests.post(url=sheet_endpoint_url, json=sheet_endpoint_params, headers=sheet_endpoint_headers)
    response.raise_for_status()
    print(response.text)
