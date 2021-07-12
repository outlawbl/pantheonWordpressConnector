from connections import wcapi
from woocommerceArtikli import woocommerce_artikli

def updateSpecsMeta():
    for artikli in woocommerce_artikli:
        for artikal in artikli:
            id = artikal['id']
            i = {
            "meta_data": [
                {
                "key": "_specifications_display_attributes",
                "value": "yes"
                }
                    ]
            }
            print(wcapi.put(f"products/{id}", i).json())

def updateManageStock():
    for artikli in woocommerce_artikli:
        for artikal in artikli:
            id = artikal['id']
            i = {
            "manage_stock": "true"
            }
            print(wcapi.put(f"products/{id}", i).json())

# updateManageStock()

def updateProductStyleMeta():
    for artikli in woocommerce_artikli:
        for artikal in artikli:
            id = artikal['id']
            i = {
            "meta_data": [
                {
                "key": "_product_style",
                "value": "normal"
                }
                    ]
            }
            print(wcapi.put(f"products/{id}", i).json())

# updateProductStyleMeta()