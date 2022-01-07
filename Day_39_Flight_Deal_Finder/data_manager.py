import requests

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_url, token=None):
        self.sheet_url = sheet_url
        self.token = token

    def get_rows(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(self.sheet_url, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_row(self, row_number, row_data):
        # TODO: Make API call to sheet (note that row_data is a dictionary
        # whose keys are column names)
        pass
