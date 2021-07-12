from connections import wcapi2
import pprint
import sys

page = 1
aoWebShopArtikli = []
while page <= 20:
    artikli = wcapi2.get("products", params={"per_page": 100, 'page':page}).json()
    aoWebShopArtikli.append(artikli)
    page+=1

original_stdout = sys.stdout

# with open('wcArtikliTxt.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print(aoWebShopArtikli)
#     sys.stdout = original_stdout # Reset the standard output to its original value

#
# ID Woocommerce artikala
#

id_woocommerce_artikala = []
for artikli in aoWebShopArtikli:
    for artikal in artikli:
        id_woocommerce_artikala.append(artikal['sku'])

#
# Sredjeni Woocommerce artikli
#

kljucevi = ['id', 'status', 'name', 'sku', 'regular_price', 'description', 'short_description', 'stock_quantity', 'manage_stock', 'images']
aoWebShopArtikli_za_poredjenje = []

for artikal in aoWebShopArtikli:
    for x in artikal:
        newdict = {k: x[k] for k in kljucevi}
        aoWebShopArtikli_za_poredjenje.append(newdict)

# pprint.pprint(aoWebShopArtikli)
# print('woocommerce artikala ima: ',len(id_woocommerce_artikala))

# for a in aoWebShopArtikli:
#     for x in a:
#         brojac = 0
#         pprint.pprint(x['images'][brojac])
#         brojac += 1

# artikal['images'] = []
# for aoWebShopArtikal in aoWebShopArtikli_za_poredjenje:
#     if artikal['sku'] == aoWebShopArtikal['sku']:
#         slika = {}
#         brojac = 0
#         for image in aoWebShopArtikal['images']:
#             slika['src'] = aoWebShopArtikal['images'][brojac]['src']
#             artikal['images'].append(slika)
#             brojac+=1
# pprint.pprint(artikal['images'])