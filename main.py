import os
import pprint
from configparser import ConfigParser
import pyodbc as pyodbc
import schedule
import time
from woocommerce import API
from decimal import *
import json
from pantheonArtikli import pantheon_artikli, id_pantheon_artikala
from woocommerceArtikli import wc_artikli_za_poredjenje, id_woocommerce_artikala
from test import razlika

start_time = time.time()

wcapi = API(
    url="https://shop.aporia.app",
    consumer_key="ck_b60aa7be8132d949e8c32dc0f9a80187b4a5f155",
    consumer_secret="cs_d0a6868e24896fdc20ab4dad590f20d0bb26b51e",
    version="wc/v3",
    wp_api=True,
    query_string_auth=True
)

# ################################################################################################################
# artikli koji imaju u pantheonu a nemaju na shopu, znaci treba ih dodati
# ################################################################################################################

id_za_insert = list(set(id_pantheon_artikala) - set(id_woocommerce_artikala))
print(id_za_insert)
print(len(id_za_insert))

artikli_za_insert = []
for ident in id_za_insert:
    for artikal in pantheon_artikli:
        if artikal['sku'] == ident:
            artikli_za_insert.append(artikal)

print(artikli_za_insert)
print('Insertovano je: ', len(artikli_za_insert), ' artikala.')

#################################################################################################################
# Artikli koje treba update-ovati                                                                               #
#################################################################################################################
def chunks(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]
chunks_za_update = list(chunks(razlika, 50))

#################################################################################################################
# Postavljanje artikala na Woocommerce                                                                          #
#################################################################################################################

def postToWc():
    for artikal in artikli_za_insert:
        wcapi.post("products", artikal).json()

postToWc()

#################################################################################################################
# Batch update artikala na Woocommerce                                                                          #
#################################################################################################################
for lista in chunks_za_update:
    artikli_za_batch_update = {
        'create': artikli_za_insert,
        'update': lista,
        'delete': []
        
    }

    def BatchPostToWc():
            wcapi.post("products/batch", artikli_za_batch_update).json()

    BatchPostToWc()
    print(wcapi.post("products/batch", artikli_za_batch_update).json())
    print(len(i))

brojac = 1

for i in razlika:
    id = i['id']
    wcapi.put(f"products/{id}", i).json()
    print(f'artikal update: {brojac}')
    brojac += 1


print("--- %s seconds ---" % (time.time() - start_time))