import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
counted_fur_color = data["Primary Fur Color"].value_counts()
counted_fur_color.to_csv("squirrel_count.csv")