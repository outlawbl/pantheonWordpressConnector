from os import walk
import os
import pprint
from pantheonArtikli import pantheon_artikli

slike_artikala = []
for i in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
    slike_artikala.append(i)

for artikal in pantheon_artikli:
    artikal['images'] = ''
    if artikal['sku'] in slike_artikala:
        artikal_images = []
        folder = artikal['sku']
        for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\{folder}'):
            artikal_single_image = {}
            kljuc = 'src:'
            putanja_slike = f'http://shop.aporia.app/wp-content/uploads/product_images/{folder}/{slika}'
            artikal_single_image[kljuc] = putanja_slike
            artikal_images.append(artikal_single_image)
        artikal['images'] = artikal_images
        pprint.pprint(artikal)

# sku = 'RD011598_B'
# for folder in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
# for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\RD011598_B'):
#     print(slika)

# slike_artikala = []
# for i in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
#     slike_artikala.append(i)

# print(slike_artikala)

