import mysql.connector

conn = mysql.connector.connect(user='alfom', password='banjaluka2018',
                              host='95.217.191.201',
                              database='shop', auth_plugin='mysql_native_password')

cursor = cnx.cursor()

query = ("SELECT * FROM )

cursor.execute()
cursor.close() 

conn.close()