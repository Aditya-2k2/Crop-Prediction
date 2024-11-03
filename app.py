from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model and label encoder
model_path = 'crop_prediction_model.pkl'
label_encoder_path = 'label_encoder.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(label_encoder_path, 'rb') as le_file:
    label_encoder = pickle.load(le_file)

@app.route('/')
def home():
    return render_template('index.html', prediction="")

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    try:
        zn = float(request.form['zn'])
        fe = float(request.form['fe'])
        cu = float(request.form['cu'])
        mn = float(request.form['mn'])
        b = float(request.form['b'])
        rainfall = float(request.form['rainfall'])
        humidity = float(request.form['humidity'])
        temperature = float(request.form['temperature'])
        ph = float(request.form['ph'])
        s = float(request.form['s'])
        area = float(request.form['area'])
        yield_value = float(request.form['yield'])

        # Prepare the input data as a DataFrame with feature names
        feature_names = ['zn %', 'fe%', 'cu %', 'mn %', 'b %', 'rainfall', 'humidity', 'temperature', 'ph', 's %', 'area', 'yield']
        input_data = pd.DataFrame([[zn, fe, cu, mn, b, rainfall, humidity, temperature, ph, s, area, yield_value]], columns=feature_names)

        # Make the prediction
        predicted_label = model.predict(input_data)
        predicted_crop = label_encoder.inverse_transform(predicted_label)

        # Pass the prediction result to the template
        return render_template('index.html', prediction=f"The recommended crop to grow is: {predicted_crop[0]}")
    except ValueError:
        return render_template('index.html', prediction="Please enter valid input values.")

if __name__ == "__main__":
    app.run(debug=True)
