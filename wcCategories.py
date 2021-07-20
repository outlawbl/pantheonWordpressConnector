from connections import wcapi
# from ptCategories import pantheon_kategorije
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
    count = kat['count']
    if count == 0:
        print(kat['name'], 'ID:', kat['id'], f'({count})')
    else:
        print(kat['name'], 'ID:', kat['id'], f'({count})')


# delete categories with no products

def delete_categories():
    for kat in woocommerce_kategorije:
        if kat['count'] == 0:
            print(wcapi.delete(f"products/categories/{kat['id']}", params={"force": True}).json())
            wcapi.delete(f"products/categories/{kat['id']}", params={"force": True}).json()

# delete_categories()

# update categories - insert Pantheon ID in description
def update_categories():
    for wc_kat in woocommerce_kategorije:
        for pt_cat in pantheon_kategorije:
            if wc_kat['name'] == pt_cat['naziv']:
                print('Update kategorije:', {wc_kat['name']})
                slug = wc_kat['slug']
                cat_id = pt_cat['id']
                data = [{"description":cat_id}]
                print(wcapi.put(f"products/categories?slug={slug}", data).json())

# update_categories()
       

