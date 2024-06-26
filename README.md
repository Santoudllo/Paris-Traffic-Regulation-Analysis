# Paris-Traffic-Regulation-Analysis
Analyse de l'efficacité des mesures de régulation du trafic à Paris à l'aide de données de comptage routier sur 13 mois, visant à identifier les forces et les faiblesses des dispositifs actuels et à formuler des recommandations d'amélioration.

## Project Setup locally

Clone github repository
```
git clone git@github.com:Santoudllo/Paris-Traffic-Regulation-Analysis.git 

### Installation des Dépendances

Pour installer les dépendances nécessaires, vous pouvez exécuter la commande suivante dans votre terminal :

```bash
pip install -r requirements.txt

```

## Structure du Projet

### Répertoire des Données

- **data/:** Contient les jeux de données bruts et traités utilisés pour l'analyse.
  - **Output_data.csv/:** Données brutes comptage routier-issues des capteurs permanant -recuperées à l'aide de L'API.
  - **data_nettoyer.csv/:** Données Propres apres le Preprocessing.
  - **comptages-routiers.csv/:** Données Exportées.
  - **Ce jeu de données est sous licence : Open Database License (ODbL)/:** 
### Notebook Jupyter

- **preprocessing.ipynb:** Notebook pour le prétraitement des données.

### Scripts

- **PostgreSQL_config.py:** Script pour configuerer la base de données PostgreSQL.
- **recuperation_données_API.py:** Script pour réaliser des appels API.
- **visualisation_Streamlit.py:** Script pour la visualisation des resultats d'analyses avec Streamlit.

## modele_Tensorflow

- **creation_model.py:** Script pour créer et entrainer le modele  .
- **preprocessing.py:** Script pour réaliser le preprocessing avant la creation du modele.

## modele

- **label_encoder:** sauvegardé qui encode les étiquettes textuelles de l'état du trafic en valeurs numériques, nécessaire pour traiter les prédictions du modèle.
- **scaler.pk:** sauvegardé utilisé pour normaliser les données d'entrée, garantissant que les features sont à une échelle appropriée pour le modèle.
- **traffic_model.h5:** Modèle de réseau de neurones entraîné enregistré, contenant l'architecture complète et les poids, utilisé pour prédire l'état du trafic.

### Résultats d'Entraînement du modele:

- **Précision d'Entraînement:** 99.51%
- **Perte d'Entraînement:** 0.0140

### Résultats de Validation :

- **Précision de Validation:** 99.38%
- **Perte de Validation:** 0.0111

### Résultats de Test :

- **Précision de Test:** 99.21%
- **Perte de Test:** 0.0168

## MAP

**visualisation_streamlit_MAP.py**: Script pour créer une interface utilisateur permettant de saisir les informations et obtenir le résultat de la prédiction. Réalisé avec Streamlit.



### Documentation


### Documentation

- **Liens.md:** Contient le lien pour accéder l'API.


## Interface Streamlit 
Permet de visualiser la distance qui existe entre deux adresses saisies par l'utilisateur
 ![alt text](image.png)
visualiser les predictions
![alt text](image-1.png)
## Contributeurs

- Alimou DIALLO (@santou): Data engineer
