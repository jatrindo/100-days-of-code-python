import requests
import os
import datetime as dt

user_endpoint = "https://pixe.la/v1/users"
TOKEN = os.environ.get('PIXELA_TOKEN')
USERNAME = os.environ.get('PIXELA_USERNAME')

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=user_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_params = {
    'id': graph_id,
    'name': 'Test Graph',
    'unit': 'Minutes',
    'type': 'int',
    'color': 'momiji',
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)


add_pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{graph_id}"

date = dt.datetime(year=2021, month=12, day=16).strftime("%Y%m%d")
print(f"date: {date}")

add_pixel_params = {
    'date': date,
    'quantity': '5',
}

add_pixel_headers = {
   "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=add_pixel_headers)
# print(response.text)

# TODO: Update yesterday's pixel to a different value