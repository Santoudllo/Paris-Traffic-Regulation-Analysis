import streamlit as st
import numpy as np
import pickle
import tensorflow as tf  # Ajout de cette ligne pour importer TensorFlow

# Charger le modèle et l'encodeur
model_path = '../modele_TensorFlow/model_traffic.keras'
encoder_path = '../modele_TensorFlow/encoder.pkl'

with open(encoder_path, 'rb') as f:
    label_encoder = pickle.load(f)

model = tf.keras.models.load_model(model_path)

# Interface utilisateur Streamlit
st.title('Prédiction de l\'état du trafic')

# Saisie utilisateur
occupancy_level = st.selectbox('Taux d\'occupation:', ['Faible', 'Moyen', 'Élevé'])

# Convertir la saisie utilisateur en une valeur numérique
if occupancy_level == 'Faible':
    occupancy_level_encoded = 0
elif occupancy_level == 'Moyen':
    occupancy_level_encoded = 1
else:
    occupancy_level_encoded = 2

# Prédiction
prediction = model.predict(np.array([[occupancy_level_encoded]]))

# Décodage de la prédiction
predicted_traffic_state = label_encoder.inverse_transform([np.argmax(prediction)])

# Afficher la prédiction
st.write(f'État du trafic prédit: {predicted_traffic_state[0]}')
