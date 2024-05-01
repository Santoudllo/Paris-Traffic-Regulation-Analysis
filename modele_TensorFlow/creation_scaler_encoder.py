import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle

# Chemin de votre fichier CSV
file_path = '../data/comptages-routiers_MAP.csv'

# Charger les données
data = pd.read_csv(file_path)

# Si nécessaire, convertissez la date et l'heure en caractéristiques utilisables
data['Date et heure de comptage'] = pd.to_datetime(data['Date et heure de comptage'], utc=True)
data['heure'] = data['Date et heure de comptage'].dt.hour
data['jour_semaine'] = data['Date et heure de comptage'].dt.dayofweek

# Supposons que vous avez besoin d'encoder le libellé
encoder = OneHotEncoder(sparse_output=False)
encoded_features = encoder.fit_transform(data[['Libelle']])

# Préparation des features pour le scaler
features = data[['heure', 'jour_semaine', 'Taux d\'occupation']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Sauvegarde de l'encoder et du scaler
scaler_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/scaler.pkl'
encoder_path = '/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/modele_TensorFlow/encoder.pkl'

with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

with open(encoder_path, 'wb') as f:
    pickle.dump(encoder, f)
