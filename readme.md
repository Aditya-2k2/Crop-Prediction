
---

# Crop Prediction Web Application

This project is a web application that uses machine learning to predict the best crop to grow based on various soil and environmental parameters. The application leverages a trained Random Forest model to make predictions and provides a user-friendly interface for data input.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Data Input Details](#data-input-details)
- [Sample Input and Output](#sample-input-and-output)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

## Overview
The Crop Prediction web application allows users to input soil and environmental data and predicts the optimal crop to grow. It is designed to assist farmers and agriculturists in making informed decisions based on scientific data.

## Features
- **User-Friendly Interface**: A clean and simple form for entering soil and environmental details.
- **Machine Learning Model**: Uses a pre-trained Random Forest model for crop prediction.
- **Output Display**: Shows the recommended crop based on the input data.
- **Clear Button**: Users can reset the form and clear the output for new predictions.
- **Responsive Design**: The app is styled to be responsive and user-friendly.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Machine Learning**: scikit-learn
- **Data Handling**: Pandas, NumPy

## Installation
Follow these steps to set up and run the project on your local machine:

1. Clone this repository:
   ```
   git clone https://github.com/your-username/crop-prediction-app.git
   ```

2. Navigate to the project directory:
   ```
   cd crop-prediction-app
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000/` to use the app.

## How to Use
1. Enter the required soil and environmental parameters into the form:
   - Zinc (Zn %)
   - Iron (Fe %)
   - Copper (Cu %)
   - Manganese (Mn %)
   - Boron (B %)
   - Rainfall (mm)
   - Humidity (%)
   - Temperature (°C)
   - pH Level
   - Sulfur (S %)
   - Area (hectares)
   - Yield

2. Click the **Predict Crop** button to see the recommended crop.

3. Use the **Clear** button to reset the form and clear the output.

## Data Input Details
- **Zn %, Fe %, Cu %, Mn %, B %, S %**: Nutrient content in the soil.
- **Rainfall (mm)**: Average rainfall received in millimeters.
- **Humidity (%)**: Relative humidity as a percentage.
- **Temperature (°C)**: Temperature in degrees Celsius.
- **pH Level**: Acidity or alkalinity of the soil.
- **Area (hectares)**: Land area available for cultivation.
- **Yield**: Expected yield of the crop.

## Sample Input and Output
### Sample Input
```
Zn %: 1.2
Fe %: 3.4
Cu %: 0.8
Mn %: 2.5
B %: 0.5
Rainfall: 200
Humidity: 70
Temperature: 25
pH Level: 6.5
S %: 1.1
Area: 5.0
Yield: 3.0
```

### Expected Output
```
The recommended crop to grow is: Rice
```

## Project Structure
```
crop-prediction-app/
│
├── app.py                  # Flask backend code
├── crop_prediction_model.pkl  # Trained ML model
├── label_encoder.pkl       # Label encoder for crop labels
├── templates/
│   └── index.html          # Frontend HTML template
├── static/
│   ├── styles.css          # CSS for styling
│   └── scripts.js          # JavaScript for responsiveness
├── requirements.txt        # Python dependencies
└── README.md               # Project documentations
```

## Future Enhancements
- **Additional Parameters**: Integrate more environmental or geographical factors for better accuracy.
- **Database Integration**: Store user inputs and predictions in a database for future analysis.
- **Advanced Modeling**: Experiment with more sophisticated machine learning or deep learning models.
- **Mobile App**: Develop a mobile version of the app for better accessibility.

## Acknowledgments
- Thanks to the open-source community for the libraries and frameworks used in this project.
- Special thanks to my mentors and collaborators who helped in the development process.

---
