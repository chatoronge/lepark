from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurez la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'D:\Users\Documents\Travail 2023-2024\Projet site sécu\main'  # Utilisez SQLite pour cet exemple
db = SQLAlchemy(app)

# Définissez les modèles de base de données
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(100))

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    prix = db.Column(db.Float)
    description = db.Column(db.String(200))

# Route pour afficher les articles
@app.route('/')
def index():
    articles = Article.query.all()  # Récupérer tous les articles
    return render_template('lepark.html', articles=articles)

# Lancer l'application
if __name__ == '__main__':
    app.run()
