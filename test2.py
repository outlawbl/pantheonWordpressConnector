# import time
# import re
# from console_progressbar import ProgressBar
# from connections import wcapi
# from wcArtikliTxt import wcArtikli
# from wcAttributes import wc_atributi_lista

# pb = ProgressBar(total=100,prefix='Here', suffix='Now', decimals=3, length=50, fill='X', zfill='-')
# pb.print_progress_bar(2)
# time.sleep(5)
# pb.print_progress_bar(25)
# time.sleep(5)
# pb.print_progress_bar(50)
# time.sleep(5)
# pb.print_progress_bar(95)
# time.sleep(5)
# pb.print_progress_bar(100)

# data = {
#     "name": "Color",
#     "slug": "pa_color7",
#     "type": "select",
#     "order_by": "menu_order",
#     "has_archives": True
# }

# novi_attr = wcapi.post("products/attributes", data).json()
# print(novi_attr)
# novi_attr_id = novi_attr['id']
# print(novi_attr_id)

# for grupa in wcArtikli:
#     for artikal in grupa:
#         for atribut in wc_atributi_lista:
#         print(artikal['name'])

# for grupa in wcArtikli:
#     for artikal in grupa:
#         atributi = artikal['attributes']
#         for atribut in atributi:
#             print(atribut['name'])

# atributi_slug = []
# for atribut in wc_atributi_lista:
#     slug = atribut['slug']
#     id_333 = atribut['id']
#     attr_slug = re.findall(r'(?<=\d_).*', slug)
#     try:
#        atributi_slug.append(attr_slug[0])
#     except IndexError:
#         pass

# print(atributi_slug)


# for grupa in wcArtikli:
#     for artikal in grupa:
#         id = artikal['id']
#         if artikal['categories'][0]['id'] == 162:           
#             atributi = artikal['attributes']
#             i = {"attributes": []}
#             for atribut in atributi:     
#                 try:                                   # za svaki atribut u artiklu
#                     for attr in wc_atributi_lista:
#                         if attr['name'] == atribut['name']:
#                             atribut['novi_id'] = attr['id']
#                             atribut['novi_slug_puni'] = attr['slug']
#                             atribut['novi_slug'] = re.findall(r'(?<=\d_).*', attr['slug'])
#                     atribut_novi_slug = atribut['novi_slug'][0]
#                     atribut['pa_333_slug'] = f'pa_333_{atribut_novi_slug}'
#                     for attr in wc_atributi_lista:
#                         if attr['slug'] == atribut['pa_333_slug']:
#                             atribut['novi_id'] = attr['id']
#                             atribut['novo_ime'] = attr['name']

#                     try:
#                         i['attributes'].append(
#                             {
#                         "id": f"{atribut['novi_id']}",
#                         "name": f"{atribut['novo_ime']}",
#                         "options": [
#                             f"{atribut['options'][0]}"
#                         ],
#                         "position": 1, 
#                         "visible": 'true'
#                         }
#                         )
#                     except IndexError:
#                         pass    
#                 except:
#                     pass
#             prvih_pet_karaktera_sluga =  re.findall(r'.{5}', attr['slug'])
#             if atribut['novi_slug_puni']:
#                 pass
#             print(wcapi.post(f"products/{id}", i).json())
                    # print(attr_slug[0], attr['id'], atribut['novi_slug'], novi_id, option)
                


                        




# for grupa in wcArtikli:
#     for artikal in grupa:
#         id = artikal['id']
#         if artikal['id'] == 11765:
#             atributi_trenutni = artikal['attributes']
#             for trenutni_atribut in atributi_trenutni: # za svaki atribut u artiklu
#                 for attr in wc_atributi_lista:
#                     if trenutni_atribut['id'] == attr['id']:
#                         trenutni_atribut['slug'] = attr['name']
#                     attr_slug2 = re.findall(r'(?<=\d_).*', attr['slug'])
#                     try:
#                         novi_slug = f'pa_333_{attr_slug2[0]}'
#                         if novi_slug == attr['slug']:
#                             novi_id = attr['id']
#                     except:
#                         pass
#                 kratki_slug_stari = re.findall(r'(?<=\d_).*', trenutni_atribut['slug'])
#         print(artikal)


wc_atributi = [{'id': 25, 'name': '3D funkcija', 'slug': 'pa_333_3d-funkcija', 'type': 'select', 'order_by': 'menu_order', 'has_archives': True, '_links': {'self': [{'href': 'https://shop.aporia.app/wp-json/wc/v3/products/attributes/25'}], 'collection': [{'href': 'https://shop.aporia.app/wp-json/wc/v3/products/attributes'}]}}, {'id': 146, 'name': 'ADU', 'slug': 'pa_333_adu', 'type': 'select', 'order_by': 'menu_order', 'has_archives': True, '_links': {'self': [{'href': 'https://shop.aporia.app/wp-json/wc/v3/products/attributes/146'}], 'collection': [{'href': 'https://shop.aporia.app/wp-json/wc/v3/products/attributes'}]}}]


for i in wc_atributi:
print(wc_atributi[0])