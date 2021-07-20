from connections import wcapi
import pprint
import sys

#
# Woocommerce artikli
#

ukupno_stranica_artikala = wcapi.get("products?per_page=100").headers['X-WP-TotalPages']

page = 1
woocommerce_artikli = []
while page <= int(ukupno_stranica_artikala):
    artikli = wcapi.get("products", params={"per_page": 100, 'page':page}).json()
    woocommerce_artikli.append(artikli)
    page += 1
# pprint.pprint(woocommerce_artikli)

#
# ID Woocommerce artikala
#

id_woocommerce_artikala = []
for artikli in woocommerce_artikli:
    for artikal in artikli:
        if 'sku' in artikal:
            id_woocommerce_artikala.append(artikal['sku'])

#
# Sredjeni Woocommerce artikli
#

kljucevi = ['status', 'name', 'sku', 'regular_price', 'sale_price', 'description', 'short_description', 'stock_quantity', 'manage_stock', 'images', 'categories', 'attributes', 'status', 'stock_status', 'backorders']

wc_artikli_za_poredjenje = []
for artikal in woocommerce_artikli:
    for x in artikal:
        newdict = {k: x[k] for k in kljucevi}
        wc_artikli_za_poredjenje.append(newdict)

print('woocommerce artikala ima: ',len(id_woocommerce_artikala))

#
# Woocommerce atributi artikala
#

# IDjevi atributa koji se koriste
id_koji_se_koriste = []
for artikal in wc_artikli_za_poredjenje:
    for atribut in artikal['attributes']:
        id_koji_se_koriste.append(atribut['id'])

# print(set(id_koji_se_koriste))

# for artikal in wc_artikli_za_poredjenje:
#     if artikal['sku'] == '01422985':
#         print(artikal)

original_stdout = sys.stdout

with open('wcArtikliTxt.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(f'wcArtikli = {woocommerce_artikli}')
    sys.stdout = original_stdout # Reset the standard output to its original value