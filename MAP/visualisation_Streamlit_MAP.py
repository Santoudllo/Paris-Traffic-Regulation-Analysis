import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle

# Chemin de votre fichier CSV
file_path = "../data/comptages-routiers_MAP.csv"

# Charger le modèle, le scaler et l'encoder
model_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/model_traffic.h5'
scaler_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/scaler.pkl'
encoder_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/encoder.pkl'

model = load_model(model_path)
scaler = pickle.load(open(scaler_path, 'rb'))
encoder = pickle.load(open(encoder_path, 'rb'))

# Fonction pour préparer les données de l'utilisateur
def prepare_input(date, libelle, taux_occupation):
    date_time = pd.to_datetime(date)
    day_of_week = date_time.dayofweek
    hour = date_time.hour
    libelle_encoded = encoder.transform([[libelle]])[0]  # Supposons que l'encoder était un OneHotEncoder
    features = np.array([[day_of_week, hour, *libelle_encoded, taux_occupation]])
    features_scaled = scaler.transform(features)
    return features_scaled

# Fonction pour prédire l'état du trafic
def predict_traffic(date, libelle, taux_occupation):
    features = prepare_input(date, libelle, taux_occupation)
    prediction = model.predict(features)
    traffic_state = encoder.inverse_transform(prediction)[0]
    return traffic_state

# Affichage des métriques de performance
def display_model_performance():
    test_data = pd.read_csv(file_path)
    test_data['heure'] = pd.to_datetime(test_data['Date et heure de comptage']).dt.hour
    test_data['jour_semaine'] = pd.to_datetime(test_data['Date et heure de comptage']).dt.dayofweek
    test_data['libelle_encoded'] = encoder.transform(test_data[['Libelle']])
    test_features = scaler.transform(test_data[['jour_semaine', 'heure', 'libelle_encoded', 'Taux d\'occupation']])
    test_labels = encoder.transform(test_data['Etat trafic'].values.reshape(-1, 1))
    loss, accuracy = model.evaluate(test_features, test_labels, verbose=0)
    return f"Accuracy: {accuracy*100:.2f}%, Loss: {loss:.2f}"

# Créer l'interface Streamlit
st.title('Prédiction de l\'état du trafic')
date = st.text_input("Entrez la date et l'heure (format YYYY-MM-DD HH:MM:SS):")
libelle = st.text_input("Entrez le libellé:")
taux_occupation = st.number_input("Entrez le taux d'occupation:", format="%.2f")

if st.button('Prédire l\'état du trafic'):
    result = predict_traffic(date, libelle, taux_occupation)
    st.success(f"L'état prédit du trafic est : {result}")
    performance = display_model_performance()
    st.write(performance)
