# This file will need to use the DataManager, FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import datetime as dt
import os

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Globals
FROM_CITY_IATA = os.environ.get("FROM_CITY_IATA")
TO_PHONE = os.environ.get("TO_PHONE")

# Our search range is from tomorrow to 6 months later for each city
# Note: We estimate 6 months as 6 * 30 = 180 days
search_start_date = (dt.datetime.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
search_end_date = (dt.datetime.today() + dt.timedelta(days=180)).strftime("%d/%m/%Y")
msg_limit_per_city = 1

# Initialize Objects
data_sheet = DataManager()
flight_search = FlightSearch()
notifier = NotificationManager()


def resolve_missing_iata_codes(rows):
    for row in rows:
        # If an IATA code is missing, search and update the sheet
        if not row.get("iataCode"):
            print(f"Row for {row.get('city')} is missing an IATA code. Fetching...")

            # Use TEQUILA Location API to get city IATA codes
            city_iata_code = flight_search.get_city_code(row.get("city"))
            print(f"Fetched! IATA code is: {city_iata_code}")

            # Use the updated city object to update the sheet row
            data_sheet.update_row(row.get("id"), row.get("city"), city_iata_code, row.get("lowestPrice"))


def send_sms_for_flights(flights):
    for flight in flights:
        message = (
            f"Low price alert! "
            f"Only ${flight.price} to fly from "
            f"{flight.city_from}-{flight.fly_from_iata} to "
            f"{flight.city_to}-{flight.fly_to_iata}, from "
            f"{flight.start_date} to {flight.end_date}"
        )

        if flight.stop_overs > 0:
            message += (
                f"\n\nFlight has {flight.stop_overs} stop over, "
                f"via {flight.via_city}"
            )

        notifier.send_sms_message(message, TO_PHONE)


def send_emails_for_flights(flights):
    for flight in flights:
        message = (
            f"Subject:Low Price Flight Alert! (to {flight.city_to})\n\n"
            f"Only ${flight.price} to fly from "
            f"{flight.city_from}-{flight.fly_from_iata} to "
            f"{flight.city_to}-{flight.fly_to_iata}, from "
            f"{flight.start_date} to {flight.end_date}"
        )

        if flight.stop_overs > 0:
            message += (
                f"\n\nFlight has {flight.stop_overs} stop over, "
                f"via {flight.via_city}"
            )

        message += (
            f"\n\nGoogle Flight Link: "
            f"https://www.google.co.uk/flights?hl=en#"
            f"flt={flight.fly_from_iata}.{flight.fly_to_iata}.{flight.start_date}*"
            f"{flight.fly_to_iata}.{flight.fly_from_iata}.{flight.end_date}"
        )

        # Send the alert to each customer email
        customer_data = data_sheet.get_customers()
        customer_emails = [user.get("email") for user in customer_data.get("users")]
        notifier.send_emails(customer_emails, message)


def find_deals_and_notify():
    # Get city rows from sheet
    rows = data_sheet.get_rows().get("prices")
    print(f"Got {len(rows)} cities from sheet")

    # For each city that's missing an IATA code, search for the code and update
    # the sheet accordingly
    resolve_missing_iata_codes(rows)

    # Search for cheap flights and send a message if any are found
    for row in rows:
        if not row.get("iataCode"):
            print(f"City ({row.get('city')}') missing an IATA code. Skipping...")
            continue

        print(f"\nSearching flights to {row.get('city')} cheaper than ${row.get('lowestPrice')}...")
        available_flights = flight_search.search_flights_cheaper_than(
            FROM_CITY_IATA,
            row.get("iataCode"),
            search_start_date,
            search_end_date,
            row.get("lowestPrice")
        )

        print(f"{len(available_flights)} cheap flights available to {row.get('city')}")
        if available_flights:
            print(f"Sending messages for first {msg_limit_per_city} cheap flight(s)")
            # send_sms_for_flights(available_flights[:msg_limit_per_city])
            send_emails_for_flights(available_flights[:msg_limit_per_city])


find_deals_and_notify()
