#!/usr/bin/python3
"""
Script will display states started with capital N
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(stateName))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == stateName:
            print(row)
    cursor.close()
    db.close()
