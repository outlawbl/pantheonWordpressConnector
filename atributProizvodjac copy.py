from connections import wcapi
# from woocommerceArtikli import woocommerce_artikli
from aoWebShopArtikli import aoWebShopArtikli
from wcAtributiTxt import stari_shop_atributi
from wcAtributiTermsTxt import stari_shop_atributi_terms
import pprint

def novi_shop_atributi():
    global novi_shop_atributi
    novi_shop_atributi = wcapi.get("products/attributes").json()
    print('Novi shop ima:', len(novi_shop_atributi), 'atributa')

novi_shop_atributi()

print('Stari shop ima:', len(stari_shop_atributi), 'atributa')

print('Stari shop ima:', len(stari_shop_atributi_terms), 'termsa')

def convert_lat(string):
    string_fixed = string.replace('č', 'c').replace('ć', 'c').replace('ć', 'c').replace('š', 's').replace('ž', 'z').replace('đ', 'd').replace(' ','-').replace('.','-')
    print('Konvertovani string:', string_fixed.lower())
    return str(string_fixed).lower()


def svi_nazivi_atributa():
    global svi_nazivi_atributa_lst
    svi_nazivi_atributa_lst = []
    
    for atribut in stari_shop_atributi:
        if atribut['name'] not in svi_nazivi_atributa_lst:
            svi_nazivi_atributa_lst.append(atribut['name'])
    
    print('Nazivi svih atributa:', svi_nazivi_atributa_lst)
    print('Broj naziva svih atributa:',len(svi_nazivi_atributa_lst))

svi_nazivi_atributa()

def kreiranje_novog_atributa(naziv_atributa):
    atribut_naziv = naziv_atributa
    naziv_atributa = convert_lat(naziv_atributa)
    print(f'Kreiranje novog "{naziv_atributa}" atributa...')

    data = {
        "name": atribut_naziv,
        "slug": f"333_{naziv_atributa}",
        "type": "select",
        "order_by": "menu_order",
        "has_archives": True
    }
    novi_atribut = wcapi.post("products/attributes", data).json()
    if 'id' in novi_atribut:
        novi_atribut_id = novi_atribut['id']
        novi_atribut_slug = novi_atribut['slug']
        print('Kreiran je atribut:', novi_atribut, 'ID:', novi_atribut_id)

        svi_terms_nazivi = []
        for term in stari_shop_atributi_terms:
            if term['attr_slug_2'] == f'{novi_atribut_slug}':
                term_naziv = term['name']
                if term_naziv not in svi_terms_nazivi:
                    svi_terms_nazivi.append(term_naziv)

        print('Nazivi termsa za atribut',svi_terms_nazivi)

        for term in svi_terms_nazivi:
            data = {"name": term}
            print(wcapi.post(f"products/attributes/{novi_atribut_id}/terms", data).json())

    else:
        print('Atribut', data['name'], data['slug'],'vec postoji.')
    
    
    

def izmjena_artikala(atribut_naziv):
    for grupa_artikala in aoWebShopArtikli:
        for artikal in grupa_artikala:
            artikal_id = artikal['id']
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
                if atribut['name'] == atribut_naziv:
                    atribut['id'] = 407
            pprint.pprint(wcapi.post("products", artikal).json())
            # print(artikal)

# izmjena_artikala('Proizvođač')


for atribut in svi_nazivi_atributa_lst:
    kreiranje_novog_atributa(atribut)

