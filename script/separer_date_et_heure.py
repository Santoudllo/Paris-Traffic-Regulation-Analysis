import pandas as pd
import re

# Chemin vers votre fichier CSV
file_path = '../data/comptages-routiers_MAP.csv'

# Charger les données
data = pd.read_csv(file_path)

# Supprimer le décalage de fuseau horaire
data['Date et heure de comptage'] = data['Date et heure de comptage'].apply(lambda x: re.sub(r'\+\d{2}:\d{2}$', '', x))

# Convertir en datetime
data['Date et heure de comptage'] = pd.to_datetime(data['Date et heure de comptage'], format='%Y-%m-%dT%H:%M:%S')

# Extraire la date (jour, mois, année) sans l'heure
data['Date'] = data['Date et heure de comptage'].dt.date

# Extraire l'heure
data['Heure'] = data['Date et heure de comptage'].dt.time

# Renommer la colonne
data.rename(columns={'Date et heure de comptage': 'Date_heure'}, inplace=True)

# Afficher les premières lignes du DataFrame
print(data.head())

# Sauvegarder le DataFrame dans un nouveau fichier CSV
data.to_csv('../data/comptages_separer.csv', index=False)
