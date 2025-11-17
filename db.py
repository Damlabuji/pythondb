import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pass",
            database="test"
        )
        return conn
    except Error as e:
        print(f"[HATA] Veritabanına bağlanırken bir sorun oluştu: {e}")
        return None
