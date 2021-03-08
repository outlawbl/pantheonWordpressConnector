import pprint
from configparser import ConfigParser
import pyodbc as pyodbc
import schedule
import time
from woocommerce import API

#################################################################################################################
# SQL DATABASE CONNECT                                               #
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
# SQL DATABASE QUERIES                                               #
#################################################################################################################

select_test_artikal = "SELECT * FROM ao_wms_artikal where sinhronizovano = 'shop'"
select_nesinhronizovano = "SELECT * FROM ao_wms_artikal where sinhronizovano = 'false'"
update_sinhronizovano = "UPDATE ao_wms_artikal SET sinhronizovano = 'true' where sinhronizovano = 'shop'"


def query_db(query, args=(), one=False):
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r


#
# nesinhronizovani_artikli = query_db(select_nesinhronizovano)
# nesinhronizovani_artikli_json = json.dumps(nesinhronizovani_artikli)
#
# cur.execute(update_sinhronizovano)
#
# db.commit()
#
# print(nesinhronizovani_artikli_json)
# print(cur.rowcount, "record(s) affected")

cur.execute(select_test_artikal)
test_artikli = query_db(select_test_artikal)

# pprint.pprint(test_artikli)

#################################################################################################################
# Mijenjanje stringa - priprema za WC
#################################################################################################################
if __name__ == '__main__':
    for artikal in test_artikli:
        artikal['status'] = 'draft'
        artikal['sku'] = artikal['erp_identifikator']
        artikal['name'] = artikal['naziv_artikla']
        artikal['images'] = ''

        del artikal['erp_identifikator']
        del artikal['dodavanje_izmjena']
        del artikal['naziv_artikla']
        del artikal['sinhronizovano']
        del artikal['vrijemeChg']
        del artikal['vrijemeIns']
        del artikal['erp_identifikator_novi']
        del artikal['jedinica_mjere']

    pprint.pprint(test_artikli)

    #################################################################################################################
    # Postavljanje artikala na Woocommerce
    #################################################################################################################

    wcapi = API(
        url="https://shop.aporia.app",
        consumer_key="ck_b60aa7be8132d949e8c32dc0f9a80187b4a5f155",
        consumer_secret="cs_d0a6868e24896fdc20ab4dad590f20d0bb26b51e",
        version="wc/v3",
        wp_api=True,
        query_string_auth=True
    )


    def postToWc():
        for artikal in test_artikli:
            wcapi.post("products", artikal).json()

    postToWc()

    # ################################################################################################################
    # Stavljanje flega da je sinhronizovano
    # ################################################################################################################

    cur.execute(update_sinhronizovano)
    db.commit()
    print(cur.rowcount, "record(s) affected")

    # ################################################################################################################
    # Schedule
    # ################################################################################################################

    schedule.every(2).seconds.do(postToWc)

    while True:
        schedule.run_pending()
        time.sleep(1)
print('testtest')