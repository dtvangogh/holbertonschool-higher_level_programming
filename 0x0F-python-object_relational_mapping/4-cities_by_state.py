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

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cursor = db.cursor()
    selection = "SELECT cities.id, cities.name, states.name \
              FROM cities LEFT JOIN states \
              ON cities.state_id = states.id \
              ORDER BY id ASC;"
    cursor.execute(selection)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
