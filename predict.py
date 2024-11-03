import pickle
import numpy as np

def predict_crop():
    # Load the trained model
    model_path = 'crop_prediction_model.pkl'
    label_encoder_path = 'label_encoder.pkl'

    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    
    with open(label_encoder_path, 'rb') as le_file:
        label_encoder = pickle.load(le_file)
    
    # Prompt the user to input values for all parameters
    print("Enter the following soil and agricultural details for crop prediction:")
    zn = float(input("Enter Zinc (Zn %) content in the soil: "))
    fe = float(input("Enter Iron (Fe %) content in the soil: "))
    cu = float(input("Enter Copper (Cu %) content in the soil: "))
    mn = float(input("Enter Manganese (Mn %) content in the soil: "))
    b = float(input("Enter Boron (B %) content in the soil: "))
    rainfall = float(input("Enter Rainfall (mm): "))
    humidity = float(input("Enter Humidity (%): "))
    temperature = float(input("Enter Temperature (°C): "))
    ph = float(input("Enter pH level of the soil: "))
    s = float(input("Enter Sulfur (S %) content in the soil: "))
    area = float(input("Enter cultivated area (in hectares): "))
    yield_value = float(input("Enter expected yield: "))

    # Prepare the input data for prediction
    input_data = np.array([[zn, fe, cu, mn, b, rainfall, humidity, temperature, ph, s, area, yield_value]])
    
    # Make the prediction
    predicted_label = model.predict(input_data)
    predicted_crop = label_encoder.inverse_transform(predicted_label)
    
    print(f"The recommended crop to grow is: {predicted_crop[0]}")

# Run the prediction function
if __name__ == "__main__":
    predict_crop()
