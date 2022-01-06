class CitySearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, search_endpoint_url, api_key):
        self.search_endpoint_url = search_endpoint_url
        self.api_key = api_key

    def get_city_code(self, city_name):
        # TODO: Make Tequila API call and retrieve the CITY IATA code
        pass
