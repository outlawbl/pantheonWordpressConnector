import os
import pprint
from configparser import ConfigParser
import pyodbc as pyodbc
import schedule
import time
from woocommerce import API
import json
from pantheonArtikli import pantheon_artikli, id_pantheon_artikala, pantheon_stari_artikli, pantheon_stari_artikli_ids
from woocommerceArtikli import wc_artikli_za_poredjenje, id_woocommerce_artikala
from poredjenjeArtikala import razlika
from connections import wcapi
from wcArtikliTxt import wcArtikli

start_time = time.time()

# ################################################################################################################
# artikli koji imaju u pantheonu a nemaju na shopu, znaci treba ih dodati
# ################################################################################################################

id_za_insert = list(set(id_pantheon_artikala) - set(id_woocommerce_artikala))
print(id_za_insert)
print('Broj artikala za insert:', len(id_za_insert))

artikli_za_insert = []
for ident in id_za_insert:
    for artikal in pantheon_artikli:
        if artikal['sku'] == ident:
            artikli_za_insert.append(artikal)

# print('Artikli koji su za insert su:', artikli_za_insert)

#################################################################################################################
# Update artikala na Woocommerce                                                                                #
#################################################################################################################
def updateWcArtikli():
    brojac = 1
    for i in razlika:
        if 'id' in i:
            id = i['id']
            sifra_artikla = i['sku']
            print(wcapi.put(f"products/{id}", i).json())
            print(f'{brojac}. Update artikal id: {id}, sifra: {sifra_artikla}')
            brojac += 1

    print('Update-ovano je:', brojac-1,'artikala')

#################################################################################################################
# Dodavanje artikala na Woocommerce                                                                             #
#################################################################################################################

def postToWc():
    for artikal in artikli_za_insert:
        if artikal['sku'] not in pantheon_stari_artikli_ids:
            print(wcapi.post("products", artikal).json())
            print('Insertovan je:', artikal['name'], ', sifra:', artikal['sku'])
        
postToWc()
updateWcArtikli()

#################################################################################################################
# Dodavanje artikala na Woocommerce                                                                             #
#################################################################################################################

def sakrivanjeArtikalaStarijihOd6Mjeseci():
    data = {
        'status' : 'draft'
    }
    for artikal in pantheon_stari_artikli:
        sku = artikal['acIdent']
        for grupa in wcArtikli:
            for a in grupa:
                if a['sku'] == sku and a['status'] == 'publish': 
                    id = a['id']
                    print(wcapi.put(f"products/{id}", data).json())



# sakrivanjeArtikalaStarijihOd6Mjeseci()

print("--- %s seconds ---" % (time.time() - start_time))