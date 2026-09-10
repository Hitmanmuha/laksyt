import mysql.connector

yhteys = mysql.connector.connect(
    unix_socket='/opt/local/var/run/mariadb-10.11/mysqld.sock',
    user='mohamed',
    password='koulu',
    database='flight_game',
    autocommit=True
    )
import mysql.connector

import mysql.connector

def yhdista():
    return mysql.connector.connect(
        unix_socket='/opt/local/var/run/mariadb-10.11/mysqld.sock',
        user='mohamed',
        password='koulu',
        database='flight_game',
        autocommit=True
    )

def hae_lentokentat_tyypeittain(maakoodi):
    conn = yhdista()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT type, COUNT(*)
        FROM airport
        WHERE iso_country = %s
        GROUP BY type
        ORDER BY COUNT(*) DESC
        """,
        (maakoodi,)
    )
    tulokset = cursor.fetchall()
    cursor.close()
    conn.close()
    return tulokset

def main():
    maakoodi = input("Anna maakoodi (esim. FI): ").strip().upper()
    tulokset = hae_lentokentat_tyypeittain(maakoodi)
    if tulokset:
        print(f"Lentokentät maassa {maakoodi}:")
        for tyyppi, lkm in tulokset:
            print(f"{tyyppi}: {lkm} kpl")
    else:
        print("Annetulla maakoodilla ei löytynyt lentokenttiä.")

if __name__ == "__main__":
    main()