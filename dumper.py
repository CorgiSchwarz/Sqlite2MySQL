import sqlite3

def dumpSqlite():
    conn = sqlite3.connect("/home/xushizhe/xhs_data.db")
    cursor = conn.cursor()
    cursor.execute(".output test_dump.sql")
    cursor.execute(".dump brand_info")
    cursor.execute(".output test_dump.sql")

dumpSqlite()