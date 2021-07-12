from aoWebShopArtikli import aoWebShopArtikli
from wcAtributiNoviTxt import wcNoviAtributi
from newWcCategories import new_shop_categories
from connections import wcapi
import pprint


for grupa_artikala in aoWebShopArtikli:
    for artikal in grupa_artikala:
        artikal['backorders'] = 'no'
        del artikal['permalink']
        del artikal['date_created']
        del artikal['date_created_gmt']
        del artikal['date_modified']
        del artikal['date_modified_gmt']
        for image in artikal['images']:
            del image['id']
        del artikal['id']
        for atribut in artikal['attributes']:
            for novi_atribut in wcNoviAtributi:
                if atribut['name'] == novi_atribut['name']:
                    atribut['id'] = novi_atribut['id']
        for kategorija in artikal['categories']:
            for nova_kategorija in new_shop_categories:
                if kategorija['name'] == nova_kategorija['name']:
                    kategorija['id'] = nova_kategorija['id']
        
        pprint.pprint(wcapi.post("products", artikal).json())
        # print(artikal)