from flask import Blueprint, render_template, request, redirect, url_for, flash

# Crée un blueprint pour les vues
views_bp = Blueprint('views', __name__)

# Exemple de vue pour la page d'accueil
@views_bp.route('/')
def index():
    return render_template('lepark.html')

# Exemple de vue pour la page d'inscription
@views_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Récupère les données du formulaire
        username = request.form['username']
        password = request.form['password']
        
        # Traite l'inscription de l'utilisateur
        # Par exemple, enregistre les données dans la base de données
        # Ajoutez ici votre logique de traitement
        
        flash('Inscription réussie!', 'success')
        return redirect(url_for('views.index'))
    
    return render_template('register.html')

# Exemple de vue pour une page produit
@views_bp.route('/product/<int:product_id>')
def product(product_id):
    # Récupère les détails du produit à partir de la base de données
    # Ajoutez ici votre logique de traitement
    
    # Renvoie la page HTML avec les détails du produit
    return render_template('product.html', product=product_details)
