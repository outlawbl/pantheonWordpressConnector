from os import walk
import os
import pprint

# for artikal in main.test_artikli:

#     artikal_images = []
#     artikal_single_image = {}
#     folder = artikal['sku']
#     for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\{folder}'):
#         kljuc = 'src:'
#         putanja_slike = f'D:\Documents\Alf-om\Alf-omwebshop\product_images\{folder}\{slika}'
#         artikal_single_image[kljuc] = putanja_slike
#         artikal_images.append()

#     # artikal['images'] = artikal_images

# pprint.pprint(main.test_artikli)


# sku = 'RD011598_B'
# for folder in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
# for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\RD011598_B'):
#     print(slika)

slike_artikala = []
for i in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
    slike_artikala.append(i)

print(slike_artikala)