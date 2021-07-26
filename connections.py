from woocommerce import API
from configparser import ConfigParser
import pyodbc as pyodbc



wcapi = API(
    url="https://shop.aporia.app",
    consumer_key="ck_eec2ff7cf774af9eca6c49abc613b8a3ab16636b",
    consumer_secret="cs_5c646cc3f344d0896bb035a6e62fcff7bef2b96d",
    version="wc/v3",
    wp_api=True,
    query_string_auth=True,
    timeout=600
)

wcapi2 = API(
    url="https://webshop.alf-om.com",
    consumer_key="ck_0f8aa3304098285bdd0a46d27e7c7c3c5c6a0a9c",
    consumer_secret="cs_a874482ff5822e843c1d0e9529d24437d46ac8d3",
    version="wc/v2",
    wp_api=True,
    query_string_auth=True,
    timeout=600
)

data_file = 'config.ini'
config = ConfigParser()
config.read(data_file)

driver = config['db_config']['driver']
server = config['db_config']['server']
database = config['db_config']['database']
username = config['db_config']['username']
password = config['db_config']['password']

db = pyodbc.connect(driver=driver, server=server, database=database, user=username, password=password, charset='UTF-8')