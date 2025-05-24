import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="movie",
        port=3306
    )

try:
    conn = get_connection()
    if conn.is_connected():
        print("ΕΠΙΤΥΧΙΑ")
    else:
        print("ΛΑΘΟΣ")
except mysql.connector.Error as err:
    print(f"ΣΦΑΛΜΑ: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
