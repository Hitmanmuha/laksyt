import mysql.connector

yhteys = mysql.connector.connect(
    unix_socket='/opt/local/var/run/mariadb-10.11/mysqld.sock',
    user='mohamed',
    password='koulu',
    database='flight_game',
    autocommit=True
    )
import mysql.connector

def yhdista():
    return mysql.connector.connect(
        unix_socket='/opt/local/var/run/mariadb-10.11/mysqld.sock',
        user='mohamed',
        password='koulu',
        database='flight_game',
        autocommit=True
    )

def hae_lentokentta(icao_koodi):
    conn = yhdista()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, municipality FROM airport WHERE ident = %s",
        (icao_koodi,)
    )
    tulos = cursor.fetchone()
    cursor.close()
    conn.close()
    return tulos

def main():
    icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
    tulos = hae_lentokentta(icao)
    if tulos:
        nimi, kunta = tulos
        print(f"Lentokentän nimi: {nimi}")
        print(f"Sijaintikunta: {kunta}")
    else:
        print("Lentokenttää ei löytynyt annetulla koodilla.")

if __name__ == "__main__":
    main()