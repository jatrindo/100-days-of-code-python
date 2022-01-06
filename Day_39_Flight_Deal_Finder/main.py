# This file will need to use the DataManager, FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import os

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
TEQUILA_API_ENDPOINT = "tequila-api.kiwi.com/"
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
cities = data_sheet.get_rows()

# For each city that's missing an IATA code, search for them and update the sheet accordingly
for i, city in enumerate(cities):
    # For now if we don't have a city IATA code, just remove it from our list
    if not city.get("IATA Code"):
        cities.remove(city)

    # TODO: Finish up the following
    # if not city.get("IATA Code"):
    #     # Use TEQUILA Location API to get city IATA codes
    #     city_iata_code = city_search.get_city_code(city.get("name"))
    #     # Update the city object with the iata code
    #     city["IATA Code"] = city_iata_code
    #     # Use the updated city object to update the sheet row
    #     data_sheet.update_rows()

# Search for cheapest flights from tomorrow to 6 months later for each city
# TODO: Get date string in dd/mm/yyy format
tomorrow = None
# TODO: Get date string in dd/mm/yyy format
six_months_after = None

search_results = []
for city in cities:
    flightData = FlightData(FLY_FROM_CITY_IATA, city.get("IATA Code"),
                            tomorrow, six_months_after)
    search_results.append(flight_search.search_flight(flightData))


# For each search result, if the price of the city is lower than the
# price listed in the Google sheet, send an SMS
# TODO: Figure out looping (zip?)
