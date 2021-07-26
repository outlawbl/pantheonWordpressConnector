import os
import pprint
import schedule
import time
from woocommerce import API
import json
from datetime import datetime
from connections import db
# from wcCategories import woocommerce_kategorije
from sabloniAtributa import *
from decimal import Decimal
import sys
import re

# from aoWebShopArtikli import aoWebShopArtikli_za_poredjenje


#################################################################################################################
# Popust                                                                                                        #
#################################################################################################################

popust = 0.05

#################################################################################################################
# SQL - select artikala iz Pantheona - DIREKTNO                                                                 #
#################################################################################################################
cur = db.cursor()

# select_direktno = "select S.acIdent, S.acName, S.acFieldSF, S.acFieldSG, S.acClassif, S.anSubClassif, S.acClassif2, C.acName as acClassif2Name, S.acCode, S.anRTPrice, S.anSalePrice, S.acFieldSA, S.acFieldSE, LTrim(RTrim(S.acTechProcedure)) As acTechProcedure, LTrim(RTrim(S.acDescr)) As acDescr, K.anStock , CONVERT(VARCHAR(24),K.adTimeChg,121) as adTimeChg, CONVERT(VARCHAR(24),K.adTimeIns,121) as adTimeIns from tHE_SetItem S join tHE_Stock K on S.acIdent=K.acIdent join tHE_SetItemCateg C on C.acClassif = S.acClassif2 where K.acWarehouse='Skladište VP1 BL' and Upper(LTrim(RTrim(S.acFieldSF))) = 'DA' and S.acActive = 'T'"
select_direktno = "select S.acIdent, S.acName, S.acFieldSF, S.acFieldSG, S.acClassif, S.anSubClassif, S.acClassif2, C.acName as acClassif2Name, S.acCode, S.anRTPrice, S.anSalePrice, S.acFieldSA, S.acFieldSE, LTrim(RTrim(S.acTechProcedure)) As acTechProcedure, LTrim(RTrim(S.acDescr)) As acDescr, K.anStock , CONVERT(VARCHAR(24),K.adTimeChg,121) as adTimeChg, CONVERT(VARCHAR(24),K.adTimeIns,121) as adTimeIns from tHE_SetItem S join tHE_Stock K on S.acIdent=K.acIdent join tHE_SetItemCateg C on C.acClassif = S.acClassif2 where K.acWarehouse='Skladište VP1 BL' and Upper(LTrim(RTrim(S.acFieldSF))) = 'DA'"

def query_db(query, args=(), one=False):
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
            for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r

cur.execute(select_direktno)
pantheon_artikli = query_db(select_direktno)

original_stdout = sys.stdout

with open('ptArtikliTxt.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(f'pantheon_artikli = {pantheon_artikli}')
    sys.stdout = original_stdout # Reset the standard output to its original value

# pprint.pprint(pantheon_artikli)


#################################################################################################################
# SQL - Pantheon artikli kojima je stanje 0 i nisu ulazili zadnjih 6 mjeseci.                                    #
#################################################################################################################

select_stari_artikli = "select pp.acIdent, SUM(anStock) as kolicina from tHE_SetItem pp left join the_Stock z on pp.acIdent=z.acIdent where pp.acIdent not in (select acIdent from tHE_MoveItem mi join the_Move m on mi.acKey=m.acKey WHERE m.acDocType in ( '1000','1020','1900','1910','11920','3000','3200')and m.adDate > '20210101') and pp.acSetOfItem='200' group by pp.acIdent having SUM(anStock) = 0 order by pp.acIdent"

# def query_db(query, args=(), one=False):
#     cur.execute(query, args)
#     r = [dict((cur.description[i][0], value) \
#             for i, value in enumerate(row)) for row in cur.fetchall()]
#     return (r[0] if r else None) if one else r

cur.execute(select_stari_artikli)
pantheon_stari_artikli = query_db(select_stari_artikli)

# pprint.pprint(pantheon_stari_artikli)
pprint.pprint(len(pantheon_stari_artikli))

pantheon_stari_artikli_ids = []
for artikal in pantheon_stari_artikli:
    pantheon_stari_artikli_ids.append(artikal['acIdent'])


#################################################################################################################
# SQL - Neaktivni Pantheon artikli.                                                                             #
#################################################################################################################

select_neaktivni_artikli = "select S.acIdent, S.acName, S.acFieldSF, S.acFieldSG, S.acClassif, S.anSubClassif, S.acClassif2, C.acName as acClassif2Name, S.acCode, S.anRTPrice, S.anSalePrice, S.acFieldSA, S.acFieldSE, S.acTechProcedure As acTechProcedure, LTrim(RTrim(S.acDescr)) As acDescr, K.anStock , CONVERT(VARCHAR(24),K.adTimeChg,121) as adTimeChg, CONVERT(VARCHAR(24),K.adTimeIns,121) as adTimeIns from tHE_SetItem S join tHE_Stock K on S.acIdent=K.acIdent join tHE_SetItemCateg C on C.acClassif = S.acClassif2 where K.acWarehouse='Skladište VP1 BL' and S.acActive = 'F'"

cur.execute(select_neaktivni_artikli)
pantheon_neaktivni_artikli = query_db(select_neaktivni_artikli)

pprint.pprint(len(pantheon_neaktivni_artikli))

#################################################################################################################
# SQL - select artikala iz Pantheona                                                                            #
#################################################################################################################

# select_test_artikal = "SELECT * FROM ao_wms_artikal where sinhronizovano = 'shop'"
# select_nesinhronizovano = "SELECT * FROM ao_wms_artikal where sinhronizovano = 'false'"
# update_sinhronizovano = "UPDATE ao_wms_artikal SET sinhronizovano = 'true' where sinhronizovano = 'shop'"

# select_pantheon_artikli = "SELECT * FROM _ARTKLI_CIJENA_WS2016 where acFieldSF = 'da'" 


# def query_db(query, args=(), one=False):
#     cur.execute(query, args)
#     r = [dict((cur.description[i][0], value) \
#             for i, value in enumerate(row)) for row in cur.fetchall()]
#     return (r[0] if r else None) if one else r

# cur.execute(select_pantheon_artikli)
# pantheon_artikli = query_db(select_pantheon_artikli)

# pprint.pprint(pantheon_artikli)

#################################################################################################################
# Mijenjanje stringa - priprema za WC                                                                           #
#################################################################################################################

for artikal in pantheon_artikli:
    if artikal['acIdent'] == '01230495':
        # sekundarna klasifikacija
        artikal['sec_class'] = artikal['acClassif2']
        sec_class = 'sec_class_' + artikal['sec_class']
        # status
        artikal['status'] = 'draft'
        # pantheon sifra
        artikal['sku'] = str(artikal['acIdent']).strip()
        # naziv artikla
        artikal['name'] = artikal['acName']
        # cijena
        artikal['regular_price'] = str(round(artikal['anSalePrice'], 2))

        cijena_sa_popustom = artikal['anSalePrice'] * Decimal(1-popust)
        artikal['sale_price'] = str(round(cijena_sa_popustom, 2))
        # opis
        artikal['description'] = str(artikal['acTechProcedure']).splitlines()

        opis = ''
        for red in artikal['description']:
            opis += red
            opis += ' '
        artikal['description'] = opis
        # kratiki opis
        artikal['short_description'] =  str(artikal['acDescr']).splitlines()
        kratki_opis = ''
        for red in artikal['short_description']:
            kratki_opis += ' '
            kratki_opis += red
        artikal['short_description'] = kratki_opis
        # kolicina na stanju
        artikal['stock_quantity'] = int(artikal['anStock'])
        # pracenje stanja
        artikal['manage_stock'] = 'true'
        if artikal['stock_quantity'] > 0:
            artikal['stock_status'] = 'instock'
            artikal['backorders'] = 'no'
        else:
            artikal['backorders'] = 'notify'
            artikal['backordered'] = 'true'
            artikal['backorders_allowed'] = 'true'
            artikal['stock_status'] = 'onbackorder'
        # atributi
        if sec_class in svi_sabloni and artikal['acTechProcedure'] is not None:
            artikal['attributes'] = dodavanje_atributa(eval(sec_class))

            atributi_iz_opisa = []
            for red in artikal['acTechProcedure'].splitlines():
                atribut = {}
                kljuc_atributa = re.findall(r'.+?(?=:)', red)
                vrijednost_atributa = re.findall(r'(?<=:).*', red)
                if len(kljuc_atributa) > 0:
                    atribut['name'] = kljuc_atributa[0].strip()
                    options = []
                    options.append(vrijednost_atributa[0].strip())
                    atribut['options'] = options
                    atributi_iz_opisa.append(atribut)
            for attr in artikal['attributes']:
                for attr2 in atributi_iz_opisa:
                    if attr['name'] == attr2['name']:
                        attr['options'] = attr2['options']   
        
            

            # pprint.pprint(atributi_iz_opisa)
        

        # slike

        # sa servera
        # slike_artikala = []
        # for i in os.listdir('D:\Documents\Alf-om\Alf-om webshop\product_images'):
        #     slike_artikala.append(i)

        # artikal['images'] = []

        # if artikal['sku'] in slike_artikala:
        #     artikal_images = []
        #     folder = artikal['sku']
        #     for slika in os.listdir(f'D:\Documents\Alf-om\Alf-om webshop\product_images\{folder}'):
        #         artikal_single_image = {}
        #         kljuc = 'src'
        #         putanja_slike = f'https://shop.aporia.app/wp-content/uploads/product_images/{folder}/{slika}'
        #         artikal_single_image[kljuc] = putanja_slike
        #         artikal_images.append(artikal_single_image)
        #     artikal['images'] = artikal_images

        # sa starog shopa
        # artikal['images'] = []
        # for aoWebShopArtikal in aoWebShopArtikli_za_poredjenje:
        #     if artikal['sku'] == aoWebShopArtikal['sku']:
        #         slika = {}
        #         brojac = 0
        #         for image in aoWebShopArtikal['images']:
        #             slika['src'] = aoWebShopArtikal['images'][brojac]['src']
        #             artikal['images'].append(slika)
        #             brojac+=1

        # # kategorije NEDOVRSENO
        # artikal['categories'] = []
        # for kat in woocommerce_kategorije:
        #     if artikal['acClassif2Name'] == kat['name']:
        #         kategorija = {}
        #         kategorija['id'] = kat['id']
        #         artikal['categories'].append(kategorija)

        # brisanje starih kljuceva
        del artikal['acIdent']
        del artikal['acName']
        del artikal['anSalePrice']
        del artikal['acTechProcedure']
        del artikal['acDescr']
        del artikal['anStock']
        del artikal['acFieldSG']
        del artikal['acFieldSF']
        del artikal['acClassif']
        del artikal['anSubClassif']
        del artikal['acClassif2']
        del artikal['acClassif2Name']
        del artikal['acCode']
        del artikal['anRTPrice']
        del artikal['acFieldSA']
        del artikal['acFieldSE']
        del artikal['adTimeChg']
        del artikal['adTimeIns']

id_pantheon_artikala = []
for artikal in pantheon_artikli:
    if artikal['sku'] not in pantheon_stari_artikli_ids:
      id_pantheon_artikala.append(artikal['sku'])

# pprint.pprint(pantheon_artikli)
# print('Pantheon artikala ima: ', len(id_pantheon_artikala))