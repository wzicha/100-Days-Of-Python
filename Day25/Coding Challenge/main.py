# data = []
# with open("weather_data.csv") as information:
#     data = information.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = next(data)
#     temperatures = []
#     for row in data:
#      temperature = row[1]
#      temperatures.append(temperature)
# print(temperatures)

import pandas
import pandas as pd

#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# y = data["temp"].idxmax()
# x = data.loc[y]
# print(x.to_string(index=False))

# Find out how many of the three different types of squirrels there are (sort Primary Fur Color)
with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as data_file:
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    y = (data.value_counts("Primary Fur Color"))
    y.to_csv('squirrel_count.csv')

# Take the data, then build a new data frame from it then build a new CSV file using Pandas
