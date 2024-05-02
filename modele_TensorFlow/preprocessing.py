import pandas as pd

# Chemin vers votre fichier CSV
file_path = '../data/comptages_separer.csv'

# Charger les données
data = pd.read_csv(file_path, sep=';')

# Vérifier le type de données de chaque colonne
print("Types de données avant correction :")
print(data.dtypes)

# Vérifier s'il y a des valeurs non numériques dans les colonnes numériques
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_columns:
    non_numeric_values = data[col].apply(lambda x: not isinstance(x, (int, float)))
    if non_numeric_values.any():
        print(f"Colonnes avec des valeurs non numériques dans '{col}':")
        print(data.loc[non_numeric_values, col])
  
        # les supprimer complètement
        data = data.loc[~non_numeric_values]

# Convertir les colonnes numériques en type float
data[numeric_columns] = data[numeric_columns].astype(float)

# Convertir la colonne de date en type datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Vérifier les types de données après correction
print("\nTypes de données après correction :")
print(data.dtypes)

# Enregistrer les données corrigées dans un nouveau fichier CSV si nécessaire
data.to_csv('../data/donnees_propres.csv', index=False)
