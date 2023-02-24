import mysql.connector
import os

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "ransom"
)

hostname = os.getenv("COMPUTERNAME")

mycursor = mydb.cursor()
  
mycursor.execute(f"SELECT dec_key FROM `ransom_info` WHERE sys_name = '{hostname}'")
  
result = mycursor.fetchone()

for keys in result:
   print(keys)




