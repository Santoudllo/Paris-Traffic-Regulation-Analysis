import psycopg2

def createConnection(driver):
    try:
        # Récupérer les informations de connexion
        type = driver['type']
        host = driver['host']
        port = driver['port']
        username = driver['username']
        password = driver['password']
        database = driver['database']
        ssl = driver['extra']['ssl']
        
        # Construire la chaîne de connexion
        conn_string = f"dbname='{database}' user='{username}' password='{password}' host='{host}' port={port}"
        
        # Ajouter SSL si nécessaire
        if ssl:
            conn_string += " sslmode=require"
        
        # Se connecter à la base de données
        connection = psycopg2.connect(conn_string)
        print("Connexion à la base de données PostgreSQL réussie.")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à la base de données PostgreSQL:", error)
        return None

# Informations de connexion à la base de données PostgreSQL
driver = {
    "type": "postgres",
    "host": "localhost",
    "port": 5432,
    "username": "myprojet",
    "password": "@Santou20",
    "database": "Paris-Traffic-Regulation-Analysis",
    "extra": {
        "ssl": True
    }
}

# Créer une connexion à la base de données
connection = createConnection(driver)
