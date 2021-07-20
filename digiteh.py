from connections import wcapi

import json
import requests
import pprint
from wcArtikliTxt import *

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
for brand in data['brands']:
    brands.append(brand)

#
# PROIZVODJACI
#

manufacturers = []
for manufacturer in data['manufacturers']:
    products.append(manufacturer)

proizvodi_za_wc = []

try:
    for product in products:
        product['status'] = 'publish'
        product['manage_stock'] = 'true'
        del product['id']
        product['name'] = product['title']
        del product['title']
        product['sku'] = f"8{product['pantheonKey']}"
        del product['pantheonKey']
        product['price'] = str(product['anRTPrice'])
        product['regular_price'] = str(product['anRTPrice'])
        del product['anRTPrice']
        product['images'] = []
        image = {}
        if product['productPicture']:
            image['src'] = product['productPicture'] + '.jpg'
            product['images'].append(image)
        product['description'] = product['acDescr']
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
        del product['acDescr']
        del product['manufacturerPantheonKey']
        del product['manufacturerId']
        proizvodi_za_wc.append(product)
        print(product)
except KeyError:
    print('Artikal nije ispravan')



    
# for d_proizvod in proizvodi_za_wc:
#     for grupa in wcArtikli:
#         for wc_proizvod in grupa:
#             if d_proizvod['sku'] == wc_proizvod['sku']:
#                 print('ima vec na shopu')
#             else:
#                 print('nema na shopu')
#                 # print(wcapi.post("products", d_proizvod).json())

wc_artikli = []
for grupa in wcArtikli:
    for artikal in grupa:
        wc_artikli.append(artikal)

# for artikal in wc_artikli:
#     for proizvod in proizvodi_za_wc:
#         if artikal['sku'] == proizvod['sku']:
#             print('ima ga na shopu')
#         else:
#             print(wcapi.post("products", proizvod).json())
for proizvod in proizvodi_za_wc:
    for artikal in wc_artikli:
        if artikal['sku'] in proizvod['sku']:
            print('postoji')
        else:
            print(wcapi.post("products", proizvod).json())