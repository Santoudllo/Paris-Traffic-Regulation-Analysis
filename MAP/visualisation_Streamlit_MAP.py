import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle

# Define file paths
model_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/model_traffic.h5'
scaler_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/scaler.pkl'
encoder_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/encoder.pkl'
file_path = "../data/comptages-routiers_MAP.csv"  # Ensure this path is correct and accessible

model = load_model(model_path)
scaler = pickle.load(open(scaler_path, 'rb'))
encoder = pickle.load(open(encoder_path, 'rb'))

# Prepare input data
def prepare_input(date, libelle, taux_occupation):
    try:
        date_time = pd.to_datetime(date, format='%Y-%m-%d %H:%M:%S', errors='coerce')
        if date_time is None:
            return None
        day_of_week = date_time.dayofweek
        hour = date_time.hour
        libelle_encoded = encoder.transform([[libelle]])
        features = np.hstack([day_of_week, hour, libelle_encoded[0], taux_occupation])
        features_scaled = scaler.transform([features])
        return features_scaled
    except Exception as e:
        st.error(f"Error in input processing: {str(e)}")
        return None

# Predict traffic state
def predict_traffic(date, libelle, taux_occupation):
    features = prepare_input(date, libelle, taux_occupation)
    if features is not None:
        prediction = model.predict(features)
        predicted_state = encoder.inverse_transform(prediction)[0]
        return predicted_state
    else:
        return "Invalid input. Please check your data."

# Display model performance
def display_model_performance():
    try:
        test_data = pd.read_csv(file_path)
        test_data['heure'] = pd.to_datetime(test_data['Date et heure de comptage']).dt.hour
        test_data['jour_semaine'] = pd.to_datetime(test_data['Date et heure de comptage']).dt.dayofweek
        test_features = scaler.transform(test_data[['jour_semaine', 'heure', 'libelle_encoded', 'Taux d\'occupation']])
        test_labels = encoder.transform(test_data['Etat trafic'].values.reshape(-1, 1))
        loss, accuracy = model.evaluate(test_features, test_labels, verbose=0)
        return f"Accuracy: {accuracy*100:.2f}%, Loss: {loss:.2f}"
    except Exception as e:
        return f"Failed to compute performance metrics: {str(e)}"

# Streamlit UI
st.title('Prediction of Traffic State')
date = st.text_input("Enter the date and time (format YYYY-MM-DD HH:MM:SS):")
libelle = st.text_input("Enter label:")
taux_occupation = st.number_input("Enter occupancy rate:", format="%.2f")

if st.button('Predict Traffic State'):
    result = predict_traffic(date, libelle, taux_occupation)
    if result:
        st.success(f'Predicted Traffic State: {result}')
        performance = display_model_performance()
        st.write(performance)
    else:
        st.error("Error in prediction process. Please check the inputs and try again.")
