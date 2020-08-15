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
    state = argv[4]
    cityArray = []

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cursor = db.cursor()
    selection = "SELECT cities.id, cities.name, states.name \
              FROM cities LEFT JOIN states \
              ON cities.state_id = states.id \
          WHERE states.name='{}' \
              ORDER BY id ASC".format(state)
    cursor.execute(selection)
    rows = cursor.fetchall()
    for row in rows:
        cityArray.append(row[1])
    print(', '.join(cityArray))
    cursor.close()
    db.close()
