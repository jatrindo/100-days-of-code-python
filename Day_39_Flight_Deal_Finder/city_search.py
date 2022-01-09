import requests


class CitySearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, search_endpoint_url, api_key):
        self.search_endpoint_url = search_endpoint_url
        self.api_key = api_key

    def get_city_code(self, city_name):
        # Retrieve the CITY IATA code
        headers = {
            "apikey": self.api_key,
        }

        params = {
            "term": city_name
        }

        response = requests.get(self.search_endpoint_url, params=params, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        location = json_data.get("locations")[0]

        return location.get("code")
