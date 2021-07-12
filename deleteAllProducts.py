from connections import wcapi
from woocommerceArtikli import woocommerce_artikli

def delete_all_products():
    for artikal in woocommerce_artikli:
        for x in artikal:
            print(wcapi.delete(f"products/{x['id']}", params={"force": True}).json())
            wcapi.delete(f"products/{x['id']}", params={"force": True}).json()

# wcapi.delete("products/12293", params={"force": True}).json()
# delete_all_products()