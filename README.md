# Paris-Traffic-Regulation-Analysis
Analyse de l'efficacité des mesures de régulation du trafic à Paris à l'aide de données de comptage routier sur 13 mois, visant à identifier les forces et les faiblesses des dispositifs actuels et à formuler des recommandations d'amélioration.
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

### Documentation

- **Liens.md:** Contient le lien pour accéder l'API.


## Utilisation

1. Clonez ce dépôt sur votre machine locale.
2. Naviguez dans les répertoires pertinents pour accéder aux jeux de données, carnets, scripts et documentations.
3. Suivez les instructions dans chaque carnet ou script pour réaliser des analyses, du prétraitement ou des tâches de visualisation.

## Contributeurs

- Alimou DIALLO (@santou): Data engineer
