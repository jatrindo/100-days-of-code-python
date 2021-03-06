import os
import requests

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_SHEET_URL = os.environ.get("SHEETY_SHEET_URL")


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_rows(self):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        response = requests.get(SHEETY_SHEET_URL, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_row(self, row_id, city, iata_code, lowest_price):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
        }

        body = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": lowest_price
            }
        }

        response = requests.put(f"{SHEETY_SHEET_URL}/{row_id}", headers=headers, json=body)
        response.raise_for_status()
