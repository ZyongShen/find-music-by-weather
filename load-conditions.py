import pandas as pd

df = pd.read_csv("weather_conditions.csv")

json_result = {}
for index, row in df.iterrows():
    json_result[row["code"]] = {
        "day":  row["day"],
        "night": row["night"]
    }

print(json_result)