import streamlit as st
import numpy as np
import pickle
import tensorflow as tf  

# Charger le modèle et l'encodeur
model_path = '../modele_TensorFlow/model_traffic.keras'
encoder_path = '../modele_TensorFlow/encoder.pkl'

with open(encoder_path, 'rb') as f:
    label_encoder = pickle.load(f)

model = tf.keras.models.load_model(model_path)

# Mapping des niveaux d'occupation vers les valeurs numériques
occupancy_mapping = {'Faible': 0, 'Moyen': 1, 'Élevé': 2}

# Interface utilisateur Streamlit
st.title('Prédiction de l\'état du trafic')

# Saisie utilisateur
occupancy_level = st.selectbox('Taux d\'occupation:', ['Faible', 'Moyen', 'Élevé'])

# Ajout du bouton "Prédire" avec vérification si le taux d'occupation est sélectionné
if occupancy_level:
    if st.button('Prédire'):
        # Convertir la saisie utilisateur en une valeur numérique en utilisant le mapping
        occupancy_level_encoded = occupancy_mapping.get(occupancy_level)

        # Prédiction
        prediction = model.predict(np.array([[occupancy_level_encoded]]))

        # Décodage de la prédiction
        predicted_traffic_state = label_encoder.inverse_transform([np.argmax(prediction)])

        # Afficher la prédiction
        st.write(f'État du trafic prédit: {predicted_traffic_state[0]}')
