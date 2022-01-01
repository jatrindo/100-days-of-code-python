import os
import requests

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

query = input("Tell me which exercises you did: ")

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
print(response.text)
