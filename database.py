import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="offlineguru"
)

cursor = db.cursor()