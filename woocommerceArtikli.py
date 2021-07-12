from connections import wcapi
import pprint

#
# Woocommerce artikli
#

ukupno_stranica_artikala = wcapi.get("products?per_page=100").headers['X-WP-TotalPages']

page = 1
woocommerce_artikli = []
while page < int(ukupno_stranica_artikala)+1:
    artikli = wcapi.get("products", params={"per_page": 100, 'page':page}).json()
    woocommerce_artikli.append(artikli)
    page+=1
# pprint.pprint(woocommerce_artikli)

#
# ID Woocommerce artikala
#

id_woocommerce_artikala = []
for artikli in woocommerce_artikli:
    for artikal in artikli:
        id_woocommerce_artikala.append(artikal['sku'])

#
# Sredjeni Woocommerce artikli
#

kljucevi = ['id', 'status', 'name', 'sku', 'regular_price', 'description', 'short_description', 'stock_quantity', 'manage_stock', 'images', 'categories', 'attributes']
wc_artikli_za_poredjenje = []

for artikal in woocommerce_artikli:
    for x in artikal:
        newdict = {k: x[k] for k in kljucevi}
        wc_artikli_za_poredjenje.append(newdict)

pprint.pprint(wc_artikli_za_poredjenje)
# print('woocommerce artikala ima: ',len(id_woocommerce_artikala))

