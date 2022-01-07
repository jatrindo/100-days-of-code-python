import requests

from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, search_endpoint_url, api_key):
        self.search_endpoint_url = search_endpoint_url
        self.api_key = api_key

    def search_flights_cheaper_than(self, fly_from, fly_to, date_from, date_to, price):
        headers = {
            "apikey": self.api_key
        }

        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "price_from": 0,
            "price_to": price
        }

        response = requests.get(self.search_endpoint_url, params=params, headers=headers)
        response.raise_for_status()
        json_data = response.json()

        # print(json_data)
        itineraries = json_data.get("data")

        # For each itinerary present in the response, create a FlightData
        # object
        return [FlightData(itinerary) for itinerary in itineraries]
