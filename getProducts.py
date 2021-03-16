from woocommerce import API
import pprint

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
svi_artikli = []
while page < 50:
    artikli = wcapi.get("products", params={"per_page": 100, 'page':page}).json()
    svi_artikli.append(artikli)
    page+=1

id_woocommerce_artikala = []
for artikli in svi_artikli:
    for artikal in artikli:
        id_woocommerce_artikala.append(artikal['sku'])

print(id_woocommerce_artikala)
print(len(id_woocommerce_artikala))