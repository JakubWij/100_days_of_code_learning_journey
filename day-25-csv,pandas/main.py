# with open("./weather-data.csv") as data:
#     data_list = data.readlines()
#     print(data_list)

# now we use basic library
#
# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# now with the use of pandas

import pandas
# # dataframe is whole table and series is a column
# data = pandas.read_csv("weather-data.csv")
# # print(type(data["temp"]))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# data["temp"].max()

# # GEt Data in colums
# data["condition"]
# data.condition
#
# # Get data in row
# data[data["day"] == "Monday"]

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
