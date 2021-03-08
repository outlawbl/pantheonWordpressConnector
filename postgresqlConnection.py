#import mysql.connector # connect to our local MySQL instance using connection string
#mydb = mysql.connector.connect(
#  host="10.0.0.63",
#  user="WMS",
#  password="Smw2019*!"
#)
import psycopg2 as psycopg2

mydb = psycopg2.connect(
    host="10.0.0.153",
    database="alfomwms",
    user="postgres",
    password="")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM popis")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
