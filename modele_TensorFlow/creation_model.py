import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pickle

# Chemin du dataset
file_path = '../data/donnees_propres.csv'

# Charger les données
data = pd.read_csv(file_path, sep=',')

# Supprimer les lignes avec des valeurs non numériques
data = data.dropna()

# Sélectionner les colonnes 'Date' et 'Taux d\'occupation' comme features
X = data[['Taux d\'occupation']]

# Encoder les labels 'Etat trafic' en valeurs numériques
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['Etat trafic'])

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normaliser les features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Création du modèle
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(128, activation='relu'),
    Dense(np.unique(y).shape[0], activation='softmax')  
])

# Compilation du modèle
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(X_train_scaled, y_train, epochs=10, validation_split=0.1)

# Sauvegarde du modèle au format .keras
model_path = '../modele_TensorFlow/model_traffic.keras'
model.save(model_path)

# Sauvegarde de l'encoder
encoder_path = '../modele_TensorFlow/encoder.pkl'
with open(encoder_path, 'wb') as f:
    pickle.dump(label_encoder, f)
