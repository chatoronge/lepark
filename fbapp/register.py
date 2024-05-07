from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuration de la connexion à la base de données
conn = mysql.connector.connect(
    host='ananthavong.ing2024@€saip.org',  # Remplacez par l'hôte de votre base de données Alwaysdata
    user='frigo@2a00:b6e0:1:210:1::1',  # Remplacez par votre nom d'utilisateur
    password='BfF3tHS2m',  # Remplacez par votre mot de passe
    database='frigo_lepark'  # Remplacez par le nom de votre base de données
)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Récupérer les données envoyées par le formulaire
        username = request.form["username"]
        password = request.form["password"]

        # Créer un curseur pour interagir avec la base de données
        cursor = conn.cursor()

        # Insertion des données dans la base de données
        query = "INSERT INTO clients (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))

        # Valider la transaction
        conn.commit()

        # Fermer le curseur
        cursor.close()

        # Rediriger l'utilisateur après l'inscription
        return redirect(url_for("some_other_page"))  

    # Afficher la page d'inscription si la requête est GET
    return render_template("register.html")

if __name__ == "__main__":
    app.run()
