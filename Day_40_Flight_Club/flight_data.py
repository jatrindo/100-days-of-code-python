from dateutil import parser


class FlightData:
    # This class is responsible for structuring the data of the flight
    # itineraries we could follow
    def __init__(self, data, stop_overs=0, via_city=""):
        self.data = data

        self.price = data.get('price')

        self.fly_from_iata = data.get('flyFrom')
        self.fly_to_iata = data.get('flyTo')

        self.city_from_iata = data.get('cityCodeFrom')
        self.city_to_iata = data.get('cityCodeTo')
        self.city_from = data.get('cityFrom')
        self.city_to = data.get('cityTo')

        self.start_date = parser.parse(data.get('local_departure')).date()
        self.end_date = parser.parse(data.get('local_arrival')).date()

        self.stop_overs = stop_overs
        self.via_city = via_city

        self.route = data.get('route')
