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
GRAPH_ID = "graph1"
graph_params = {
    'id': GRAPH_ID,
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


add_pixel_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

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


# Update a Pixel
today = dt.datetime.today().strftime("%Y%m%d")
update_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantity": input("How many minutes did you read today? ")
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=graph_headers)
response.raise_for_status()
print(response.text)


# Delete a pixel
response = requests.delete(url=update_endpoint, headers=graph_headers)
response.raise_for_status()
print(response.text)