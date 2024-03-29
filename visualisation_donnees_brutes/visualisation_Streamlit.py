import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
@st.cache_data
def load_data(file_path):
    # Chargez vos données ici
    data = pd.read_csv(file_path)
    return data

# Chemin vers le fichier CSV
file_path = "/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/visualisation_donnees_brutes/output_data.csv"

# Chargement des données
data = load_data(file_path)

# Affichage des données
if not data.empty:
    st.write("Cette dataviz donne à voir la donnée brute telle qu'elle est publiée, ce n'est en aucun cas un tableau de bord caractérisant la circulation à Paris.")
    st.write(data)
    
    # Affichage de la carte avec les colonnes de latitude et de longitude renommées
    if 'geo_point_2d.lon' in data.columns and 'geo_point_2d.lat' in data.columns:
        map_data = data[['geo_point_2d.lat', 'geo_point_2d.lon']]
        map_data = map_data.dropna()  # Supprimer les lignes avec des valeurs manquantes
        m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)  # Coordonnées de Paris
        for _, row in map_data.iterrows():
            folium.Marker(location=[row['geo_point_2d.lat'], row['geo_point_2d.lon']]).add_to(m)
        folium_static(m)
    else:
        st.error("Les données ne contiennent pas les colonnes de latitude et de longitude nécessaires.")
    
    # Visualisation du débit
    st.write("Visualisation du débit :")
    fig, ax = plt.subplots()
    sns.histplot(data['q'], bins=30, kde=True, ax=ax)
    ax.set_xlabel('Débit')
    ax.set_ylabel('Fréquence')
    st.pyplot(fig)
    
    # Visualisation du taux d'occupation
    st.write("Visualisation du taux d'occupation :")
    fig, ax = plt.subplots()
    sns.histplot(data['k'], bins=30, kde=True, ax=ax)
    ax.set_xlabel('Taux d\'occupation')
    ax.set_ylabel('Fréquence')
    st.pyplot(fig)

else:
    st.error("Aucune donnée n'est disponible.")