import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle

# Chemin de votre fichier CSV
file_path = '../data/comptages_separer.csv'

# Charger les données
data = pd.read_csv(file_path, sep=';')

# Convertir la date en caractéristiques numériques (si nécessaire)
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
data['Heure'] = pd.to_datetime(data['Heure'], format='%H:%M:%S')
data['heure'] = data['Heure'].dt.hour

# Supposons que vous avez besoin d'encoder le libellé
encoder = OneHotEncoder(sparse_output=False)
encoded_libelle = encoder.fit_transform(data[['Libelle']])

# Préparation des features pour le scaler
features = data[['heure', 'Taux d\'occupation']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Sauvegarde de l'encoder et du scaler
scaler_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/scaler.pkl'
encoder_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/encoder.pkl'

with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

with open(encoder_path, 'wb') as f:
    pickle.dump(encoder, f)
