import mysql.connector

cnx = mysql.connector.connect(user='alfom', password='banjaluka2018',
                              host='95.217.191.201',
                              database='shop', auth_plugin='mysql_native_password')
cnx.close()