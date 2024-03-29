import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Chemin vers le fichier CSV
file_path = "/home/santoudllo/Desktop/DEEP_LEARNING/Paris-Traffic-Regulation-Analysis/data/output_data.csv"

data = load_data(file_path)

st.write("<h1 style='text-align:center; font-weight:bold;'>Comptage routier - Données trafic issues des capteurs permanents</h1>", unsafe_allow_html=True)

st.write("<h2 style='text-align:center;'>Visualisation du débit et du taux d'occupation</h2>", unsafe_allow_html=True)

st.write("<p style='text-align:center'><strong>Cette dataviz donne à voir la donnée brute telle qu'elle est publiée, ce n'est en aucun cas un tableau de bord caractérisant la circulation à Paris.</strong></p>", unsafe_allow_html=True)

if not data.empty:
    st.write(data)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
                            # Visualisation du débit
    ax1.set_title("Visualisation du débit")
    sns.histplot(data['q'], bins=30, kde=True, ax=ax1)
    ax1.set_xlabel('Débit')
    ax1.set_ylabel('Fréquence')
    
                           # Visualisation du taux d'occupation
    ax2.set_title("Visualisation du taux d'occupation")
    sns.histplot(data['k'], bins=30, kde=True, ax=ax2)
    ax2.set_xlabel('Taux d\'occupation')
    ax2.set_ylabel('Fréquence')
    
    st.pyplot(fig)

else:
    st.error("Aucune donnée n'est disponible.")
