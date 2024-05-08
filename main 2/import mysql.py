import mysql.connector

conn = mysql.connector.connect(
    host='localhost',  # Remplacez par l'hôte de votre base de données
    user='root',  # Remplacez par votre nom d'utilisateur
    password='root',  # Remplacez par votre mot de passe
    
)

print(conn)

if conn.is_connected():
    print("Connexion Valide")
else:
    print("Connexion non valide")
