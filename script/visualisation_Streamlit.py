import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

st.set_page_config(layout="wide")

file_path = "../data/comptages-routiers.csv"  # Chemin de votre fichier CSV

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.title("Comptage routier - Données trafic issues des capteurs permanents")

    choice = st.sidebar.selectbox("Menu", ['Charger les données', 'EDA', 'MAP'])

    if choice == 'Charger les données':
        file = st.file_uploader("Chargez vos données")
        separator = st.radio("Si votre dataset ne s'affiche pas correctement, sélectionnez le bon séparateur",
                             [",", ";"])
        if file:
            df = pd.read_csv(file, index_col=None, sep=separator)
            df.to_csv(file_path, index=None)
            if len(df.columns) >= 2:
                st.success("Données chargées correctement, vous pouvez passer à l'analyse")
            else:
                st.error("Il semble que vous avez sélectionné le mauvais séparateur")
            st.dataframe(df)

    elif choice == 'EDA':
        st.header("Rapport d'analyse exploratoire des données")
        st.write(df.describe())  # Afficher les statistiques descriptives
        
        # Afficher un histogramme pour une colonne spécifique
        column_to_plot = st.selectbox("Sélectionnez une colonne pour afficher un histogramme", df.columns)
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column_to_plot], kde=True)
        plt.title(f"Histogramme de la colonne {column_to_plot}")
        plt.xlabel(column_to_plot)
        plt.ylabel("Fréquence")
        st.pyplot(plt)

        # Afficher un diagramme en barres pour une colonne spécifique
        column_to_plot_bar = st.selectbox("Sélectionnez une colonne pour afficher un diagramme en barres", df.columns)
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x=column_to_plot_bar)
        plt.title(f"Diagramme en barres de la colonne {column_to_plot_bar}")
        plt.xlabel(column_to_plot_bar)
        plt.ylabel("Fréquence")
        st.pyplot(plt)

    elif choice == 'MAP':
        st.header("Carte des données géographiques")
        
        # Sélectionnez le service de géocodage
        geocoder = st.selectbox("Sélectionnez un service de géocodage", ["Nominatim"])
        if geocoder == "Nominatim":
            geolocator = Nominatim(user_agent="my_geocoder")
        else:
            st.error("Service de géocodage non pris en charge")
        
        # Entrée des adresses de départ et d'arrivée
        start_address = st.text_input("Adresse de départ")
        end_address = st.text_input("Adresse d'arrivée")
        
        # Sélectionnez la colonne d'état de trafic
        traffic_state_column = st.selectbox("Sélectionnez la colonne d'état de trafic", df.columns)
        
        # Sélectionnez l'état de trafic
        selected_traffic_state = st.selectbox("Sélectionnez l'état de trafic", df[traffic_state_column].unique())
        
        # Si les adresses de départ et d'arrivée sont fournies, géocodez-les
        if start_address and end_address:
            start_location = geolocator.geocode(start_address)
            end_location = geolocator.geocode(end_address)
            
            # Si les emplacements de départ et d'arrivée sont trouvés, affichez-les sur la carte
            if start_location and end_location:
                m = folium.Map(location=[start_location.latitude, start_location.longitude], zoom_start=12)
                folium.Marker([start_location.latitude, start_location.longitude], popup="Départ").add_to(m)
                folium.Marker([end_location.latitude, end_location.longitude], popup="Arrivée").add_to(m)
                
                # Créer une liste de tuples contenant les coordonnées géographiques de départ et d'arrivée
                points = [(start_location.latitude, start_location.longitude), (end_location.latitude, end_location.longitude)]
                
                # Créer une ligne reliant les deux points
                route = folium.PolyLine(points, color='blue').add_to(m)
                
                # Ajouter la ligne à la carte
                m.add_child(route)
                
                # Filtrer les données en fonction de l'état de trafic sélectionné
                filtered_df = df[df[traffic_state_column] == selected_traffic_state]
                
                # Ajouter des marqueurs de couleur différente en fonction de l'état de trafic
                for index, row in filtered_df.iterrows():
                    coordinates = str(row['geo_point_2d']).split(',') if isinstance(row['geo_point_2d'], str) else None
                    if coordinates:
                        if row['Etat trafic'] == "Saturé":
                            color = 'red'
                        elif row['Etat trafic'] == "Fluide":
                            color = 'green'
                        else:
                            color = 'blue'
                        folium.Marker([float(coordinates[0]), float(coordinates[1])], popup=row['Libelle'], icon=folium.Icon(color=color)).add_to(m)
                
                # Afficher la carte dans Streamlit
                folium_static(m)
            else:
                st.error("Impossible de géocoder les adresses fournies")
        
        # Afficher les points géographiques à partir du jeu de données
        st.subheader("Points géographiques à partir du jeu de données")
        m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)  # Coordonnées pour Paris
        
        # Ajoutez des marqueurs pour chaque point géographique dans votre jeu de données
        for index, row in df.iterrows():
            coordinates = str(row['geo_point_2d']).split(',') if isinstance(row['geo_point_2d'], str) else None
            if coordinates:
                folium.Marker([float(coordinates[0]), float(coordinates[1])], popup=row['Libelle']).add_to(m)
            else:
                print(f"Coordonnées manquantes ou invalides pour l'index {index}")
        
        
else:
    st.error("Le chemin spécifié pour le fichier n'existe pas.")
