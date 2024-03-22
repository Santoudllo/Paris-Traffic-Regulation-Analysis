import requests

def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        for result in data.get('results', []):  
            print(result)
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la récupération des données:", e)

url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/comptages-routiers-permanents/records?limit=20"
get_api_data(url)
