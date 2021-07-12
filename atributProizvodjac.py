from connections import wcapi2, wcapi
# from woocommerceArtikli import woocommerce_artikli
from aoWebShopArtikli import aoWebShopArtikli
import pprint

def novi_shop_atributi():
    global novi_shop_atributi
    novi_shop_atributi = wcapi.get("products/attributes").json()
    print('Novi shop ima:', len(novi_shop_atributi), 'atributa')

novi_shop_atributi()

def stari_shop_atributi_fn():
    global stari_shop_atributi
    stari_shop_atributi = (wcapi2.get("products/attributes").json())
    print('Stari shop ima:', len(stari_shop_atributi), 'atributa')

stari_shop_atributi_fn()

def stari_shop_atributi_terms_fn():
    print('Pronalazenje svih termsa sa starog shopa')
    global stari_shop_atributi_terms
    stari_shop_atributi_terms = []
    for atribut in stari_shop_atributi:
        terms = wcapi.get(f"products/attributes/{atribut['id']}/terms").json()
        stari_shop_atributi_terms.append(terms)
    print('Stari shop ima:', len(stari_shop_atributi_terms), 'termsa')

stari_shop_atributi_terms_fn()

def convert_lat(string):
    string_fixed = string.replace('č', 'c').replace('ć', 'c').replace('ć', 'c').replace('š', 's').replace('ž', 'z').replace('đ', 'd')
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
    novi_atribut_id = novi_atribut['id']
    print('Kreiran je atribut:', novi_atribut, 'ID:', novi_atribut_id)
    
    # for atribut in novi_shop_atributi:
    #     if atribut['slug'] == f"pa_333_{naziv_atributa}":
    #         atribut_id = atribut['id']
    #         print('ID novog atributa je:', atribut_id)
    #     else:
    #         print('Atribut nije pronadjen')
    
    svi_terms = stari_shop_atributi_terms

    # for grupa_artikala in aoWebShopArtikli:
    #     for artikal in grupa_artikala:
    #         for atribut in artikal['attributes']:
    #             if atribut['name'] == atribut_naziv:
    #                 id_attr = atribut['id']
    #                 terms = wcapi2.get(f"products/attributes/{id_attr}/terms").json()
    #                 # wcapi2.get(f"products/attributes/{id_attr}/terms").json()

    #                 if terms not in svi_terms:
    #                     svi_terms.append(terms)
    #                     print(len(svi_terms))

    svi_terms_nazivi = []
    for term in svi_terms:
        term_naziv = term['name']
        if term_naziv not in svi_terms_nazivi:
            svi_terms_nazivi.append(term_naziv)

    print(svi_terms_nazivi)

    
    for term in svi_terms_nazivi:
        data = {"name": term}
        print(wcapi.post(f"products/attributes/{novi_atribut_id}/terms", data).json())

# kreiranje_novog_atributa('Proizvođač')



# izmjena_artikala('Proizvođač')


for atribut in svi_nazivi_atributa_lst:
    kreiranje_novog_atributa(atribut)

