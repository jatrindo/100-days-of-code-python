class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_url, token=None):
        self.sheet_url = sheet_url
        self.token = token
