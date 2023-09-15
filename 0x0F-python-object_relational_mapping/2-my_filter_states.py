#!/usr/bin/python3
"""
script to list all states from database
where name matches the argument
from the database 'hbtn_0e_0_usa'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    from database get states where name is searched
    """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3]
            )

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
            .format(argv[4])
            )

    states = cursor.fetchall()

    for state in states:
        print(state)
