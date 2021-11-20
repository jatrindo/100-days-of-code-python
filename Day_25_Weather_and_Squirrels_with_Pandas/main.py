"""
    Three Parts to this File:
        - Part 1: Weather Data CSV
        - Part 2: Weather Data CSV with Pandas
        - Part 3: Counting Squirrels Using Pandas
"""


"""Part 1: Weather Data CSV"""
# with open("weather_data.csv") as f:
#     data = f.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


"""Part 2: Weather Data CSV with Pandas"""
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))           # Pandas DataFrame-type (basically a table, 2D)
# print(type(data["temp"]))   # Pandas Series-type (basically a list (row, or column))
# temperatures = data['temp']
# # print(f"Avg Temp: {sum(temperatures) / len(temperatures)}")
# print(temperatures.mean())
# print(temperatures.max())
#
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == 'Monday'])
#
# # Get Row(s) that has the highest temp in the week
# print(data[data.temp == data.temp.max()])   # Filter column by condition
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
# print(monday.temp)
# print((int(monday.temp) * 1.8) + 32)
#
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new-data.csv")

# Goal:
#   1. Find out how many grey, cinnamon, and black squirrels there are
#   2. Take that data and make a new DataFrame with the following format:
#           ,Fur Color, Count
#           0,grey,###
#           1,red,###
#           2,black,###


"""Part 3: Counting Squirrels Using Pandas"""
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# For finding out the unique set of 'Primary Fur Color' values we have
# print(data['Primary Fur Color'].unique())

# Grab all the rows for each Primary Fur Color
grey_rows = data[data['Primary Fur Color'] == 'Gray']
cinnamon_rows = data[data['Primary Fur Color'] == 'Cinnamon']
black_rows = data[data['Primary Fur Color'] == 'Black']

# Create a dictionary with the information
#   - Keys are the column names we want
#   - Values are a list whose element represents a row of data for that column
fur_color_counts = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [len(grey_rows), len(cinnamon_rows), len(black_rows)],
}

fur_color_counts_df = pandas.DataFrame(fur_color_counts)
fur_color_counts_df.to_csv('squirrel_count.csv')
