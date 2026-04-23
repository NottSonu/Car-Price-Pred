import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("car data.csv")

df['Car_Age'] = 2025 - df['Year']
df.drop(['Car_Name', 'Year'], axis=1, inplace=True)

df = pd.get_dummies(df, drop_first=True)

X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model.pkl")
joblib.dump(X.columns, "columns.pkl")

print("Model trained and saved!")
