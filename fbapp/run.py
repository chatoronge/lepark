from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/Lazone'

db = SQLAlchemy(app)

# Modèle de produit
class Produits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modele = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float)
    stock = db.Column(db.Integer)
    reference = db.Column(db.String(100))

# Routes
@app.route('/')
def index():
    products = Produits.query.all()
    return render_template('index.html', products=products)

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    products = Produits.query.filter(Produits.name.ilike(f'%{keyword}%')).all()
    return render_template('search.html', products=products, keyword=keyword)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Logique pour ajouter un produit au panier
    return redirect(url_for('index'))

@app.route('/checkout')
def checkout():
    # Logique pour valider la commande
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logique pour enregistrer un utilisateur
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logique pour authentifier un utilisateur
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Logique pour déconnecter l'utilisateur
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
