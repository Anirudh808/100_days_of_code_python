# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# monday = data[data.day == "Monday"]
# print(monday.temp.tolist()[0] * 9/5 + 32)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_counts = data["Primary Fur Color"].value_counts()
color_counts_df = color_counts.reset_index()
color_counts_df.columns = ["Primary Fur Color", "Count"]
color_counts_df.to_csv("squirrel_color_counts.csv", index=False)

