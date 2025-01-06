import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass",
        database="test"
    )

def yenitablo():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            numara INT AUTO_INCREMENT PRIMARY KEY,
            isim VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_user(isim, email):
    conn = connect_to_db()
    cursor = conn.cursor()
    sql = "INSERT INTO users (isim, email) VALUES (%s, %s)"
    val = (isim, email)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()

def get_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()

def update_user(numara, isim, email):
    conn = connect_to_db()
    cursor = conn.cursor()
    sql = "UPDATE users SET isim = %s, email = %s WHERE numara = %s"
    val = (isim, email, numara)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(numara):
    conn = connect_to_db()
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE numara = %s"
    val = (numara,)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()

yenitablo()


print("Kullanıcılar:")
insert_user("ugur","ugur@hotmail.com")
get_users()

