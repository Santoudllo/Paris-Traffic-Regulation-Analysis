import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium

@st.cache_data
def load_data(file_path):

    data = pd.read_csv(file_path)
    return data

file_path = "/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/visualisation_donnees_brutes/output_data.csv"

data = load_data(file_path)


if not data.empty:
    st.write("Aperçu des données :")
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
else:
    st.error("Aucune donnée n'est disponible.")
