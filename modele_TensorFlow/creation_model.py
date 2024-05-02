import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Chargement des données
file_path = '../data/comptages_separer.csv'
data = pd.read_csv(file_path, sep=';')

# Transformation de 'Heure' en valeurs cycliques pour capturer la cyclicité du temps
data['Heure'] = pd.to_datetime(data['Heure'], format='%H:%M:%S').dt.hour
data['Heure_sin'] = np.sin(data['Heure'] * (2 * np.pi / 24))
data['Heure_cos'] = np.cos(data['Heure'] * (2 * np.pi / 24))

# Sélection des features et du label
features = ['Heure_sin', 'Heure_cos', 'Debit horaire', 'Taux d\'occupation']
X = data[features]
y = data['Etat trafic']

# Encodage des labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Normalisation des features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Construction du modèle de réseau de neurones
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(64, activation='relu'),
    Dense(np.unique(y_encoded).shape[0], activation='softmax')
])

# Compilation du modèle
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(X_train_scaled, y_train, epochs=10, validation_split=0.1)

# Évaluation du modèle
evaluation = model.evaluate(X_test_scaled, y_test)
print("Test loss, Test accuracy:", evaluation)

# Sauvegarde de LabelEncoder
encoder_save_path = '../modele/label_encoder.pkl'
with open(encoder_save_path, 'wb') as file:
    pickle.dump(label_encoder, file)

# Sauvegarde du scaler
scaler_save_path = '../modele/scaler.pkl'
with open(scaler_save_path, 'wb') as file:
    pickle.dump(scaler, file)

# Enregistrement du modèle
model_save_path = '../modele/traffic_model.h5'
model.save(model_save_path)
