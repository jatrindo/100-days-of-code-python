# This file will need to use the DataManager, FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import os
import datetime as dt
import sys

from data_manager import DataManager
from city_search import CitySearch
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Globals
# Data management
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_SHEET_URL = os.environ.get("SHEETY_SHEET_URL")

# Flight search
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_LOCATION_SEARCH_ENDPOINT = f"{TEQUILA_API_ENDPOINT}/locations/query"
TEQUILA_FLIGHT_SEARCH_ENDPOINT = f"{TEQUILA_API_ENDPOINT}/v2/search"
FLY_FROM_CITY_IATA = os.environ.get("FLY_FROM_CITY_IATA")

# SMS messaging
TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_PHONE = os.environ.get("TWILIO_FROM_PHONE")
TWILIO_TO_PHONE = os.environ.get("TWILIO_TO_PHONE")


# Initialize Objects
data_sheet = DataManager(SHEETY_SHEET_URL, SHEETY_TOKEN)
city_search = CitySearch(TEQUILA_LOCATION_SEARCH_ENDPOINT, TEQUILA_API_KEY)
flight_search = FlightSearch(TEQUILA_FLIGHT_SEARCH_ENDPOINT, TEQUILA_API_KEY)
sms_notifier = NotificationManager(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_PHONE)

# Get city rows from sheet
rows = data_sheet.get_rows().get("prices")

# For each city that's missing an IATA code, search for them and update the sheet accordingly
for row in rows:
    # If an IATA code is missing, update the sheet
    if not row.get("iataCode"):
        print(f"Row for {row.get('city')} is missing an IATA code. Fetching...")

        # Use TEQUILA Location API to get city IATA codes
        city_iata_code = city_search.get_city_code(row.get("city"))
        print(f"Fetched! IATA code is: {city_iata_code}")

        # Use the updated city object to update the sheet row
        data_sheet.update_row(row.get("id"), row.get("city"), city_iata_code, row.get("lowestPrice"))

print(f"Got {len(rows)} cities from sheet")

# Search for cheapest flights from tomorrow to 6 months later for each city
# Note: We estimate 6 months after as 6 * 4 = 24 weeks
tomorrow = (dt.datetime.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
six_months_after = (dt.datetime.today() + dt.timedelta(weeks=24)).strftime("%d/%m/%Y")

# Search for flights and send a message if any are found
message_limit = 1
for row in rows:
    if not row.get("iataCode"):
        continue

    print(f"\nSearching flights to {row.get('city')} cheaper than ${row.get('lowestPrice')}...")
    available_flights = flight_search.search_flights_cheaper_than(
        FLY_FROM_CITY_IATA,
        row.get("iataCode"),
        tomorrow,
        six_months_after,
        row.get("lowestPrice")
    )

    if available_flights:
        print(f"{len(available_flights)} cheap flights available to {row.get('city')}")
        print(f"Sending SMS message for first {message_limit} flight(s)")

        # Send SMS message for only the first couple of cheap flights
        for (i, flight) in enumerate(available_flights):
            if i >= message_limit:
                break

            message = (
                f"Low price alert! "
                f"Only ${flight.price} to fly from "
                f"{flight.city_from}-{flight.fly_from_iata} to "
                f"{flight.city_to}-{flight.fly_to_iata}, from "
                f"{flight.start_date} to {flight.end_date}"
            )

            sms_notifier.send_sms_message(message, TWILIO_TO_PHONE)
    else:
        print(f"No cheap flights found to {row.get('city')}")
