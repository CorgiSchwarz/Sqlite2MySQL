import sqlite3
import sys


def table_getter(db_address: str):
    db = sqlite3.connect(db_address)
    cursor = db.cursor()
    tables = cursor.execute("select name from sqlite_master where type='table'").fetchall()
    fo = open('./tables.txt', 'w+')

    for table in tables:
        fo.write(table[0] + '\n')


if __name__ == "__main__":
    table_getter(sys.argv[1])
