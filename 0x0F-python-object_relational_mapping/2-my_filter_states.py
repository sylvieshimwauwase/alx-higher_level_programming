#!/usr/bin/python3
"""
script to list all states from database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    from database get states where name is searched
    """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3], state_name=argv[4]
            )

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
            .format(state_name)
            )

    states = cursor.fetchall()

    for state in states:
        print(state)
