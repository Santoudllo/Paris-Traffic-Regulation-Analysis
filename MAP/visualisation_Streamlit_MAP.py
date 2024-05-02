import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Charger le modèle, le label encoder et le scaler
model_path = '../modele/traffic_model.h5'
encoder_path = '../modele/label_encoder.pkl'
scaler_path = '../modele/scaler.pkl'

model = load_model(model_path)
with open(encoder_path, 'rb') as f:
    label_encoder = pickle.load(f)
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

# Définir la fonction de prédiction
def predict_traffic(heure, debit_horaire, taux_occupation):
    heure = pd.to_datetime(heure, format='%H:%M:%S').hour
    heure_sin = np.sin(heure * (2 * np.pi / 24))
    heure_cos = np.cos(heure * (2 * np.pi / 24))

    features = np.array([[heure_sin, heure_cos, debit_horaire, taux_occupation]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])
    return predicted_class

# Interface utilisateur Streamlit
st.title('Prédiction de l\'état du trafic')
heure = st.time_input("Heure de la mesure (HH:MM:SS)")
debit_horaire = st.number_input("Débit horaire", min_value=0.0, format="%.2f")
taux_occupation = st.number_input("Taux d'occupation", min_value=0.0, max_value=100.0, format="%.2f")

if st.button('Prédire'):
    result = predict_traffic(heure.strftime('%H:%M:%S'), debit_horaire, taux_occupation)
    st.success(f"L'état prévu du trafic est : {result[0]}")
