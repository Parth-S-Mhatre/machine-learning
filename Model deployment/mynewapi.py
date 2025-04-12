import os
from flask import Flask, request, jsonify
import joblib
import pandas as pd 

# CREATE FLASK APP
app = Flask(__name__)

# Load my model and load column names
model_path = "C:/Users/parth/OneDrive/Desktop/parth/Machine-learning(Practical & coding)/Model deployment/final_model.pkl"
col_names_path = "C:/Users/parth/OneDrive/Desktop/parth/Machine-learning(Practical & coding)/Model deployment/col_names.pk1"

model = joblib.load(model_path)
col_names = joblib.load(col_names_path)

# CONNECT POST API CALL ---> predict() Function http://localhost:5000/predict
@app.route('/predict', methods=['POST'])
def predict():
    # GET JSON REQUEST
    feature_data = request.json
    df = pd.DataFrame(feature_data)
    df = df.reindex(columns=col_names)
   
    prediction = list(model.predict(df))

    return jsonify({'prediction': str(prediction)})  # Prediction

# Run the app
if __name__ == '__main__':
    app.run(debug=True)