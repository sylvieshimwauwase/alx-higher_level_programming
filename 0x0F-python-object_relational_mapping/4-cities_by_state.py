#!/usr/bin/python3
"""
script to list all cities from database
where name matches the argument
from the database 'hbtn_0e_4_usa'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    from database get cities
    """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3]
            )

    cursor = db.cursor()

    cursor.execute(
            "SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.state_id \
                    = states.id ORDER BY cities.id ASC"
            )

    cities = cursor.fetchall()

    if cities is not None:
        for city in cities:
            print(city)
