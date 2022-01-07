# This file will need to use the DataManager, FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import os
import datetime as dt
import sys

from data_manager import DataManager
from city_search import CitySearch
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Globals
# Data management
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_SHEET_URL = os.environ.get("SHEETY_SHEET_URL")

# Flight search
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_SEARCH_ENDPOINT = f"{TEQUILA_API_ENDPOINT}/v2/search"
FLY_FROM_CITY_IATA = os.environ.get("FLY_FROM_CITY_IATA")

# SMS messaging
TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID ")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN ")
TWILIO_FROM_PHONE = os.environ.get("TWILIO_FROM_PHONE ")
TWILIO_TO_PHONE = os.environ.get("TWILIO_TO_PHONE ")


# Initialize Objects
data_sheet = DataManager(SHEETY_SHEET_URL, SHEETY_TOKEN)
city_search = CitySearch(TEQUILA_SEARCH_ENDPOINT, TEQUILA_API_KEY)
flight_search = FlightSearch(TEQUILA_SEARCH_ENDPOINT, TEQUILA_API_KEY)
sms_notifier = NotificationManager(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_PHONE)

# Get city rows from sheet
# cities = data_sheet.get_rows().get("prices")
cities = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]

# For each city that's missing an IATA code, search for them and update the sheet accordingly
for i, city in enumerate(cities):
    pass
    # TODO: If an IATA code is missing, update the sheet
    # if not city.get("iataCode"):
    #     # Use TEQUILA Location API to get city IATA codes
    #     city_iata_code = city_search.get_city_code(city.get("name"))
    #     # Update the city object with the iata code
    #     city["iataCode"] = city_iata_code
    #     # Use the updated city object to update the sheet row
    #     data_sheet.update_rows()

print(cities)

# Search for cheapest flights from tomorrow to 6 months later for each city
# Note: We estimate 6 months after as 6 * 4 = 24 weeks
tomorrow = (dt.datetime.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
six_months_after = (dt.datetime.today() + dt.timedelta(weeks=24)).strftime("%d/%m/%Y")

# Begin searching for flights
search_results = []
for city in cities:
    if not city.get("iataCode"):
        continue

    print(f"Searching flights to {city.get('city')} cheaper than {city.get('lowestPrice')}...")
    result = flight_search.search_flights_cheaper_than(
        FLY_FROM_CITY_IATA,
        city.get("iataCode"),
        tomorrow,
        six_months_after,
        city.get("lowestPrice")
    )

    if result:
        search_results.append(result)

print(search_results)

# For each search result, if the price of the city is lower than the
# price listed in the Google sheet, send an SMS
# TODO: Figure out looping (zip?)
