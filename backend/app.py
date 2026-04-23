from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

@app.route('/')
def home():
    return "Car Price Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    input_df = pd.DataFrame([data])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_df)[0]

    return jsonify({"predicted_price": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
