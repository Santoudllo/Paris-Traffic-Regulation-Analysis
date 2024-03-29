import psycopg2
from psycopg2 import Error

try:
    # Paramètres de connexion
    connection = psycopg2.connect(user="mon_projet",
                                  password="@santou20",
                                  host="localhost",
                                  port="5432",
                                  database="Paris_Traffic_Regulation_Analysis")

    # Création d'un curseur
    cursor = connection.cursor()

    # Exécution d'une requête SQL
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Version de PostgreSQL :", record)

except (Exception, Error) as error:
    print("Erreur lors de la connexion à PostgreSQL :", error)

finally:
    # Fermeture du curseur et de la connexion
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("Connexion à PostgreSQL fermée")
