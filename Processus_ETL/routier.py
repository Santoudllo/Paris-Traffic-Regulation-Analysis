import requests
import pandas as pd

url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/comptages-routiers-permanents/records?limit=100"
response = requests.get(url)

if response.status_code == 200:
   
    data = response.json()
    df = pd.json_normalize(data['results'])
    
   
    output_file = "/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/data/output_data.csv"
    
    
    df.to_csv(output_file, index=False)
    
    print("Les données ont été exportées avec succès vers:", output_file)
else:
    print("Erreur lors de la récupération des données:", response.status_code)
