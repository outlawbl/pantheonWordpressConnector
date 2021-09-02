from connections import wcapi
from woocommerceArtikli import woocommerce_artikli
from pantheonArtikli import pantheon_artikli
import sys
import os

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

# updateSpecsMeta()

def updateManageStock(): # Postavice na sve artikle "manage_stock": "true"
    for artikli in woocommerce_artikli:
        for artikal in artikli:
            id = artikal['id']
            i = {
            "manage_stock": "true"
            }
            print(wcapi.put(f"products/{id}", i).json())

# updateManageStock()

def updateProductStyleMeta(): # Update-uje stil artikla na shopu na normal (da bi radili tabovi specifikacije i opis)
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

def updateBackorders(): # Dozvoljava Backorder na sve artikle
    for artikli in woocommerce_artikli:
        for artikal in artikli:
            id = artikal['id']
            i = {
            "backorders": 'yes'
            }
            print(wcapi.put(f"products/{id}", i).json())

# updateBackorders()

def updateStatusForDraft(): # Artikli koji su u draftu a na stanju su
    for artikli in woocommerce_artikli:
        for artikal in artikli:
            if artikal['stock_quantity'] != None:
                if artikal['stock_quantity'] > 0 and artikal['status'] == 'draft' and artikal['categories'][0]['name'] != 'Uncategorized' :
                    id = artikal['id']
                    i = {
                    "status": 'publish'
                    }
                    print(wcapi.put(f"products/{id}", i).json())

# updateStatusForDraft()

 # slike sa servera
def updateImages():
    for artikal in pantheon_artikli:
        slike_artikala = []
        for i in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
            slike_artikala.append(i)

        artikal['images'] = []

        if artikal['sku'] in slike_artikala:
            artikal_images = []
            folder = artikal['sku']
            for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\{folder}'):
                artikal_single_image = {}
                kljuc = "src"
                putanja_slike = f"https://shop.aporia.app/wp-content/uploads/product_images/{folder}/{slika}"
                artikal_single_image[kljuc] = putanja_slike
                artikal_images.append(artikal_single_image)
            slike = artikal_images
            data = {
                "images":tuple(slike)
                    }
            sku = artikal['sku']
            for artikli in woocommerce_artikli:
                for wcartikal in artikli:
                    if wcartikal['sku'] == sku:
                        id = wcartikal['id']
                        print(wcapi.put(f"products/{id}", data).json())

# updateImages()