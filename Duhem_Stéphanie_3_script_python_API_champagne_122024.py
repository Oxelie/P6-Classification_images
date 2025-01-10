import requests
import csv

# URL de l'API Edamam via RapidAPI
url = 'https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser'

params = {
    'ingr': 'champagne',
}

headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'x-rapidapi-key': "92ceeff3b2msh66443c5e2d05f21p1e25ecjsn57d13b437847",
    'x-rapidapi-host': "edamam-food-and-grocery-database.p.rapidapi.com"
}

# Connexion à l'API
response = requests.get(url, headers=headers, params=params)

# Si connexion ok
if response.status_code == 200:
    data = response.json()
    products = data.get('hints', [])

    # Enregistrer dans un fichier CSV 
    with open('champagne_products_10_premiers.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Food ID', 'Label', 'Category', 'Food Contents Label', 'Image'])

        for product in products[:10]:  # Limiter à 10 produits
            food = product.get('food', {})
            food_id = food.get('foodId', 'NR')
            label = food.get('label', 'NR')
            category = food.get('category', 'NR')
            food_contents_label = food.get('foodContentsLabel', 'NR')
            image = food.get('image', 'NR')
            
            writer.writerow([food_id, label, category, food_contents_label, image])

    print('Les 10 premiers produits à base de champagne ont été enregistrés dans "champagne_products.csv".')
else:
    print(f"Erreur lors de la requête à l'API : {response.status_code}")