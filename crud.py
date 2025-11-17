from db import connect

def create_table():
    conn = connect()
    if conn is None:
        return

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
    conn = connect()
    if conn is None:
        return

    cursor = conn.cursor()
    sql = "INSERT INTO users (isim, email) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (isim, email))
        conn.commit()
        print("✔ Kullanıcı başarıyla eklendi.")
    except Exception as e:
        print(f"[HATA] Kullanıcı eklenemedi: {e}")

    cursor.close()
    conn.close()


def get_users():
    conn = connect()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("\n📋 Kullanıcı Listesi")
    print("-" * 30)
    for row in rows:
        print(f"ID: {row[0]}, İsim: {row[1]}, Email: {row[2]}")
    print("-" * 30)

    cursor.close()
    conn.close()


def update_user(numara, isim, email):
    conn = connect()
    if conn is None:
        return

    cursor = conn.cursor()
    sql = "UPDATE users SET isim=%s, email=%s WHERE numara=%s"
    cursor.execute(sql, (isim, email, numara))
    conn.commit()

    print("✔ Kullanıcı güncellendi.")

    cursor.close()
    conn.close()


def delete_user(numara):
    conn = connect()
    if conn is None:
        return

    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE numara=%s"
    cursor.execute(sql, (numara,))
    conn.commit()

    print("✔ Kullanıcı silindi.")

    cursor.close()
    conn.close()
