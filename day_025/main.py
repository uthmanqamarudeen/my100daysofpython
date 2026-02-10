# with open("weather_data.csv") as weather:
#     data = weather.readlines()


# import csv
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas


# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
#
# temp_list = data["temp"].to_list()
# temp_average = data["temp"].mean()
# print(temp_average)
#
#
# temp_max = data.temp.max()
#
# print(data[data.temp == temp_max])

# print(data.temp)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_f = (monday_temp * 9/5) + 32
# print(monday_temp_f)

squirrel_data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colour = squirrel_data["Primary Fur Color"]
fur_colour_count = fur_colour.value_counts()
gray = fur_colour_count.Gray
cinnamon = fur_colour_count.Cinnamon
black = fur_colour_count.Black

fur_colour_dict = {
    "Fur Colour": ["grey", "cinnamon", "black"],
    "Count": [gray, cinnamon, black]
}

squirrel_data_file = pandas.DataFrame(fur_colour_dict)
squirrel_data_file.to_csv("squirrel_count.csv")