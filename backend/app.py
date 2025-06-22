from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

iso = joblib.load('model/iso_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = pd.DataFrame([data['features']], columns=[
        'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
        'V11','V12','V13','V14','V15','V16','V17','V18','V19','V20',
        'V21','V22','V23','V24','V25','V26','V27','V28','Amount'])
    features[['Time','Amount']] = scaler.transform(features[['Time','Amount']])

    score = iso.decision_function(features)[0]
    prediction = iso.predict(features)[0]
    is_fraud = int(prediction == -1)

    return jsonify({'fraud_score': float(score), 'is_fraud': is_fraud})

if __name__ == '__main__':
    app.run(debug=True)