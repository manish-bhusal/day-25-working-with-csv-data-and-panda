# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
# print(data_list)
# print(round(sum(data_list)/len(data_list), 2))
# print(data["temp"].mode())
# print(data["temp"].sum())
# print(data["temp"].max())

# Get data in Column
# print(data["condition"])
# Alternative method to get data
# print(data.condition)

# Get data in Row
# print(data[data.condition == "Rain"])

# Get data which has highest temperature in a row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(f"Today's temperature is: {(monday_temp*9/5)+32}F.")

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


import pandas


data = pandas.read_csv("squirrel_data.csv")
# print(data["Primary Fur Color"])
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
