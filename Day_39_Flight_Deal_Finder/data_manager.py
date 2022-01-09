import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_url, token=None):
        self.sheet_url = sheet_url
        self.token = token

    def get_rows(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(self.sheet_url, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_row(self, row_id, city, iata_code, lowest_price):
        headers = {
            "Authorization": f"Bearer {self.token}",
        }

        body = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": lowest_price
            }
        }

        response = requests.put(f"{self.sheet_url}/{row_id}", headers=headers, json=body)
        response.raise_for_status()
