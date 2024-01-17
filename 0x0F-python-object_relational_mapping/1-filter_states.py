#!/usr/bin/python3
"""modules"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cu = db.cursor()
    cu.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    ro = cu.fetchall()
    for i in ro:
        print(i)
    cu.close()
    db.close()
