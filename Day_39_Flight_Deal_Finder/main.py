# This file will need to use the DataManager, FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import os

from data_manager import DataManager
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

# SMS messaging
TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID ")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN ")
TWILIO_FROM_PHONE = os.environ.get("TWILIO_FROM_PHONE ")
TWILIO_TO_PHONE = os.environ.get("TWILIO_TO_PHONE ")


# Initialize Objects
data_sheet = DataManager(SHEETY_SHEET_URL, SHEETY_TOKEN)
search_engine = FlightSearch(TEQUILA_SEARCH_ENDPOINT, TEQUILA_API_KEY)
sms_notifier = NotificationManager(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_PHONE)
