import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("data.csv")
data["weather"] = data["weather"].map({
    "Sunny": 0,
    "Rainy": 1,
    "Cloudy": 2
})
if data.isnull().any().any():
    raise ValueError("Please check data.csv for missing or invalid values.")
X = data[["weather", "temperature"]]
y = data["activity"]
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)
weather = input(
    "Enter weather (Sunny/Rainy/Cloudy): "
).strip().title()

try:
    temperature = float(
        input("Enter temperature: ")
    )
    codes = {
        "Sunny": 0,
        "Rainy": 1,
        "Cloudy": 2
    }
    if weather in codes:
        result = model.predict([[
            codes[weather],
            temperature
        ]])

        print("Predicted Activity:", result[0])

    else:
        print("Invalid weather!")
except ValueError:
    print("Please enter a valid temperature.")

