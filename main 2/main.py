from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'  # Assurez-vous de définir une clé secrète pour la session

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Implémentez la logique de votre fonction ici
    # Par exemple, récupérer les données du panier du client et ajouter les articles
    data = request.get_json()  # Récupère les données JSON envoyées par le client

    # Vérifiez si la session existe, sinon, créez une session vide
    if 'cart' not in session:
        session['cart'] = []

    # Ajoutez les articles dans la session du panier
    session['cart'].append(data)
    
    # Retournez une réponse de succès
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)

cursor = conn.cursor()
cursor.execute("SELECT stock FROM produit WHERE id = %s", ('id',))
result = cursor.fetchone()
stock = result[0] if result else None

cursor.close()
conn.close()

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_stock/<int:product_id>')
def get_stock(product_id):
    conn = mysql.connector.connect(
        host='ananthavong.ing2024@esaip.org',
        user='frigo',
        password='BfF3tHS2m',
        database='frigo_lepark'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT stock FROM produit WHERE id = %s", (product_id,))
    result = cursor.fetchone()
    stock = result[0] if result else None
    cursor.close()
    conn.close()
    return jsonify({'stock': stock})

if __name__ == '__main__':
    app.run()

