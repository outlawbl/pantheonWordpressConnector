from connections import wcapi
import pprint

ukupno_stranica_kategorija = wcapi.get("products/categories?per_page=100").headers['X-WP-TotalPages']

page = 1
woocommerce_kat = []
while page < int(ukupno_stranica_kategorija)+1:
    kategorija = wcapi.get("products/categories", params={"per_page": 100, 'page':page}).json()
    woocommerce_kat.append(kategorija)
    page+=1

woocommerce_kategorije = []

for grupa_kat in woocommerce_kat:
    for kategorija in grupa_kat:
        woocommerce_kategorije.append(kategorija)

for kat in woocommerce_kategorije:
    if kat['count'] == 0:
        pprint.pprint(kat['name'])


# delete categories

def delete_categories():
    for kat in woocommerce_kategorije:
        if kat['count'] == 0:
            print(wcapi.delete(f"products/categories/{kat['id']}", params={"force": True}).json())
            wcapi.delete(f"products/categories/{kat['id']}", params={"force": True}).json()

delete_categories()

