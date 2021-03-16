from woocommerce import API

wcapi = API(
    url="https://shop.aporia.app",
    consumer_key="ck_b60aa7be8132d949e8c32dc0f9a80187b4a5f155",
    consumer_secret="cs_d0a6868e24896fdc20ab4dad590f20d0bb26b51e",
    version="wc/v3",
    wp_api=True,
    query_string_auth=True
)

page = 1
artikli = []
woocommerce_artikli = []
while page < 30:
    artikli = wcapi.get("products", params={"per_page": 100, 'page':page}).json()
    woocommerce_artikli.append(artikli)
    page+=1

id_woocommerce_artikala = []
for artikli in woocommerce_artikli:
    for artikal in artikli:
        id_woocommerce_artikala.append(artikal['sku'])

kljucevi = ['id', 'status', 'name', 'sku', 'regular_price', 'description', 'short_description', 'stock_quantity', 'manage_stock']
wc_artikli_za_poredjenje = []

for artikal in woocommerce_artikli:
    for x in artikal:
        newdict = {k: x[k] for k in kljucevi}
        wc_artikli_za_poredjenje.append(newdict)

# print(wc_artikli_za_poredjenje)
# print('woocommerce artikala ima: ',len(id_woocommerce_artikala))

