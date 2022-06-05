from http import server
import sqlite3
import psycopg2
import os


def client(db, **args):
    conn = db.connect(**args)

    cursor = conn.cursor()  # factory method

    # Create table
    cursor.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    cursor.execute(
        "INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

    for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def cleanup(database):
    if os.path.exists(database):
        os.remove(database)


def test_sqlite_client():
    server_params = {'database': 'example.db'}
    client(sqlite3, **server_params)
    cleanup(**server_params)


def test_postgresql_client():
    server_params = {'database': 'mydb',
                     'host': 'localhost', 'port': '5432',
                     'user': 'postgres', 'password': 'postgres'}

    client(psycopg2, **server_params)


if __name__ == "__main__":
    test_sqlite_client()
    # test_postgresql_client()
