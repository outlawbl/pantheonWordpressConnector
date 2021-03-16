import pyodbc as pyodbc
import json
import psycopg2
from configparser import ConfigParser

#################################################################################################################
#                                            SQL DATABASE CONNECT                                               #
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
#                                            SQL DATABASE QUERIES                                               #
#################################################################################################################

select_nesinhronizovano = "SELECT * FROM ao_wms_artikal"
update_sinhronizovano = "UPDATE ao_wms_artikal SET sinhronizovano = 'false' where erp_identifikator = '09140001'"

select_pantheon_artikli = "SELECT * FROM _ARTKLI_WEB where acFieldSF = 'da' or acFieldSF = 'DA'" 

def query_db(query, args=(), one=False):
  cur.execute(query, args)
  r = [dict((cur.description[i][0], value) \
            for i, value in enumerate(row)) for row in cur.fetchall()]
  return (r[0] if r else None) if one else r

# nesinhronizovani_artikli = query_db(select_nesinhronizovano)
# nesinhronizovani_artikli_json = json.dumps(nesinhronizovani_artikli)

cur.execute(select_pantheon_artikli)
pantheon_artikli = query_db(select_pantheon_artikli)

# cur.execute(update_sinhronizovano)
# db.commit()

print(select_pantheon_artikli)
print(cur.rowcount, "record(s) affected")