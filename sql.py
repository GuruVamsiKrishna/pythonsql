import mysql.connector
import os


host = os.environ.get('host_name')
user = os.environ.get('user_name')
pswd = os.environ.get('pass_name')
database = os.environ.get('data_name')
print(host, user, pswd, database)

mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=pswd,
  database=database
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cats")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

