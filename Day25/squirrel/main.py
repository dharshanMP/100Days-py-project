import pandas

data = pandas.read_csv("squirrel_data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel)
print(cinnamon_squirrel)
print(black_squirrel)


data_dict = {
    "color" : ["Gray", "Cinnamon", "Black"],
    "count" : [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_counts")