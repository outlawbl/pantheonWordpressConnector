from os import walk
import os
import main
import pprint

# for file in filenames:



for artikal in main.test_artikli:

    artikal['status'] = 'draft'
    artikal['sku'] = artikal['erp_identifikator']
    artikal['name'] = artikal['naziv_artikla']


    del artikal['erp_identifikator']
    del artikal['dodavanje_izmjena']
    del artikal['naziv_artikla']
    del artikal['sinhronizovano']
    del artikal['vrijemeChg']
    del artikal['vrijemeIns']
    del artikal['erp_identifikator_novi']
    del artikal['jedinica_mjere']

    artikal_images = []
    folder = artikal['sku']
    for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\{folder}'):
        kljuc = 'src'
        putanja_slike = f'D:\Documents\Alf-om\Alf-omwebshop\product_images\{folder}\{slika}'
        artikal_images.append(putanja_slike)

    artikal['images'] = artikal_images

pprint.pprint(main.test_artikli)

# print(folder)
# print(putanja)

# sku = 'RD011598_B'
# for folder in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
# for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\RD011598_B'):
#     print(slika)

