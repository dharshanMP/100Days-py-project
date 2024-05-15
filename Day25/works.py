'''import csv

with open("weather_data.csv") as w_data:
    data = csv.reader(w_data)
    temprature = []
    for n in data:
        if n[1] != "temp":
            temprature.append(n[1])
        
    print(temprature)'''

# Acessing dataframes

'''import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"].max())
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
farenheit = (monday_temp *9/5) + 32
print(farenheit)'''


import pandas
#creating dataframes

details = {
    "players" : ["Dhoni", "Kholi", "Rohit"],
    "runs" : [8576, 10789, 8687]
}

data = pandas.DataFrame(details)
print(data)
