class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_url, token=None):
        self.sheet_url = sheet_url
        self.token = token

    def get_rows(self):
        # TODO: Make API call to sheet
        pass

    def update_row(self, row_number, row_data):
        # TODO: Make API call to sheet (note that row_data is a dictionary
        # whose keys are column names)
        pass
