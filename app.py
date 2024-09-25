# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('Dragon.joblib')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Make prediction
    prediction = model.predict(final_features)
    
    # Render the result
    return render_template('index.html', prediction_text=f'Predicted House Price: ${round(prediction[0] * 1000, 2)}')

if __name__ == "__main__":
    app.run(debug=True)
