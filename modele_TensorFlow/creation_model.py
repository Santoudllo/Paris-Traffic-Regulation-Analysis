import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Chemin du dataset
file_path = '../data/comptages_separer.csv'

# Charger les données
data = pd.read_csv(file_path ,sep=';')

# Convertir la date en caractéristiques numériques (heure)
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
data['Heure'] = pd.to_datetime(data['Heure'], format='%H:%M:%S')
data['heure'] = data['Heure'].dt.hour

# Encodage One-Hot pour le libellé et l'état du trafic
encoder_libelle = OneHotEncoder(sparse_output=False)
encoded_libelle = encoder_libelle.fit_transform(data['Libelle'].values.reshape(-1, 1))

encoder_etat_trafic = OneHotEncoder(sparse_output=False)
encoded_etat_trafic = encoder_etat_trafic.fit_transform(data['Etat trafic'].values.reshape(-1, 1))

# Préparation des features et labels
features = np.hstack((encoded_libelle, data[['heure', 'Taux d\'occupation']].values))
labels = encoded_etat_trafic

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Création du modèle
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(128, activation='relu'),
    Dense(y_train.shape[1], activation='softmax')
])

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(X_train, y_train, epochs=10, validation_split=0.1)

# Sauvegarde du modèle
# Sauvegarde du modèle
model_path = '../modele_TensorFlow/model_traffic.h5'
model.save(model_path)