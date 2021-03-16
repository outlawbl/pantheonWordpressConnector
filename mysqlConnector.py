import mysql.connector

conn = mysql.connector.connect(user='alfom', password='banjaluka2018',
                              host='95.217.191.201',
                              database='shop', auth_plugin='mysql_native_password')

cursor = cnx.cursor()

query = ("SELECT * FROM )

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()                              
conn.close()