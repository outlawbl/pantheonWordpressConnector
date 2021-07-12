from connections import wcapi

import json
import requests
import pprint

def get_digiteh_data():
    solditems = requests.get('https://digiteh.com/api/6886ba16-29b8-4a32-a909-7f3c2731a39c/data') # (your url)
    data = solditems.json()
    with open('digitehData.json', 'w') as f:
        json.dump(data, f)

with open('digitehData.json', 'r') as f:
    data = json.load(f)

#
# PROIZVODI
#

products = []
for product in data['products']:
    products.append(product)

#
# KATEGORIJE
#

categories = []
for category in data['categories']:
    categories.append(category)

#
# BRENDOVI
#

brands = []
for brand in data['products']:
    brands.append(brand)

#
# PROIZVODJACI
#

manufacturers = []
for manufacturer in data['manufacturers']:
    products.append(manufacturer)

for product in products:
    product['manage_stock'] = 'true'
    del product['id']
    product['name'] = product['title']
    del product['title']
    product['sku'] = f"8{product['pantheonKey']}"
    del product['pantheonKey']
    product['price'] = str(product['anRTPrice'])
    product['regular_price'] = str(product['anRTPrice'])
    del product['anRTPrice']
    # product['images'] = []
    # image = {}
    # image['src'] = product['productPicture']
    # product['images'].append(image)
    del product['productPicture']
    del product['brand']
    del product['brandId']
    del product['categoryTitle']
    del product['categoryPath']
    del product['categoryIdPath']
    del product['categoryId']
    del product['acName']
    product['stock_quantity'] = str(product['anStock'])
    del product['anStock']
    product['short_description'] = product['description']
    del product['acDescr']
    del product['description']
    del product['manufacturerPantheonKey']
    del product['manufacturerId']



    print(product)

    print(wcapi.post("products", product).json())