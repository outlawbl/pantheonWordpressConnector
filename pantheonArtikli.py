import os
import pprint
from configparser import ConfigParser
import pyodbc as pyodbc
import schedule
import time
from woocommerce import API
from decimal import *
import json

#################################################################################################################
# SQL DATABASE CONNECT                                                                                          #
#################################################################################################################

data_file = 'config.ini'
config = ConfigParser()
config.read(data_file)

driver = config['db_config']['driver']
server = config['db_config']['server']
database = config['db_config']['database']
username = config['db_config']['username']
password = config['db_config']['password']

db = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password)
cur = db.cursor()

#################################################################################################################
# SQL - select artikala iz Pantheona                                                                            #
#################################################################################################################

# select_test_artikal = "SELECT * FROM ao_wms_artikal where sinhronizovano = 'shop'"
# select_nesinhronizovano = "SELECT * FROM ao_wms_artikal where sinhronizovano = 'false'"
# update_sinhronizovano = "UPDATE ao_wms_artikal SET sinhronizovano = 'true' where sinhronizovano = 'shop'"

select_pantheon_artikli = "SELECT * FROM _ARTKLI_CIJENA_WS2016 where acFieldSF = 'da'" 


def query_db(query, args=(), one=False):
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
            for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r


# nesinhronizovani_artikli = query_db(select_nesinhronizovano)
# nesinhronizovani_artikli_json = json.dumps(nesinhronizovani_artikli)
#
# cur.execute(update_sinhronizovano)
#
# db.commit()
#
# print(nesinhronizovani_artikli_json)
# print(cur.rowcount, "record(s) affected")

# cur.execute(select_test_artikal)
# test_artikli = query_db(select_test_artikal)

cur.execute(select_pantheon_artikli)
pantheon_artikli = query_db(select_pantheon_artikli)

# pprint.pprint(pantheon_artikli)

#################################################################################################################
# Mijenjanje stringa - priprema za WC                                                                           #
#################################################################################################################

for artikal in pantheon_artikli:
    # status
    artikal['status'] = 'draft'
    # pantheon sifra
    artikal['sku'] = str(artikal['acIdent']).strip()
    # naziv artikla
    artikal['name'] = artikal['acName']
    # cijena
    artikal['regular_price'] = str(round(artikal['anSalePrice'], 2))
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
    # brisanje starih naziva
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
    id_pantheon_artikala.append(artikal['sku'])

# print(pantheon_artikli)
# print('Pantheon artikala ima: ', len(id_pantheon_artikala))