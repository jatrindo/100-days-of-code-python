import os
import requests

from flight_data import FlightData

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")

TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_LOCATION_SEARCH_ENDPOINT = f"{TEQUILA_API_ENDPOINT}/locations/query"
TEQUILA_FLIGHT_SEARCH_ENDPOINT = f"{TEQUILA_API_ENDPOINT}/v2/search"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_city_code(self, city_name):
        # Retrieve the CITY IATA code
        headers = {
            "apikey": TEQUILA_API_KEY,
        }

        params = {
            "term": city_name
        }

        response = requests.get(TEQUILA_LOCATION_SEARCH_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        location = json_data.get("locations")[0]

        return location.get("code")

    def search_flights_cheaper_than(self, fly_from, fly_to, date_from, date_to, price):
        headers = {
            "apikey": TEQUILA_API_KEY
        }

        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "price_from": 0,
            "price_to": price,
            "curr": "USD"
        }

        response = requests.get(TEQUILA_FLIGHT_SEARCH_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        json_data = response.json()

        itineraries = json_data.get("data")

        if itineraries:
            # For each itinerary present in the response, create a FlightData
            # object
            return [FlightData(itinerary) for itinerary in itineraries]

        # If a flight is not found, check to see if there are flights with 1 stop
        max_stopovers = 1
        params["max_stopovers"] = max_stopovers

        print(f"No direct flights found. Searching again but for flights with "
              f"at most {max_stopovers} stopover(s)...")
        response = requests.get(TEQUILA_FLIGHT_SEARCH_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        json_data = response.json()

        itineraries = json_data.get("data")
        if not itineraries:
            print("Still no flights found!")
            return []

        return [
            FlightData(
                itinerary,
                stop_overs=max_stopovers,
                via_city=itinerary.get("route")[0].get("cityTo")
            )
            for itinerary in itineraries
        ]
