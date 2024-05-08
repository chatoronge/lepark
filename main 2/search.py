from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Liste de produits (en pratique, vous utiliserez une base de données)
products = ['Aixoise', 'Normale', 'Herman Signature', 'planche cool', 'foot fetish']

@app.route('/search', methods=['GET'])
def search():
    # Récupérer le terme de recherche depuis la requête
    query = request.args.get('query')
    
    # Vérifier si le produit recherché est dans la liste des produits
    if query in products:
        # Si le produit existe, rediriger l'utilisateur vers la page du produit
        return redirect(url_for('product', product_name=query))
    else:
        # Si le produit n'existe pas, afficher un message d'erreur ou rediriger vers une page appropriée
        return render_template('leparke.html', query=query)

@app.route('/products/<product_name>')
def product(product_name):
    # Afficher la page du produit en passant le nom du produit au template
    return render_template(f'{product_name}.html', product_name=product_name)

if __name__ == '__main__':
    app.run(debug=True)
