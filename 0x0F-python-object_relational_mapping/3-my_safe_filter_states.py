#!/usr/bin/python3
"""
script to list all states from database
where name matches the argument
from the database 'hbtn_0e_0_usa'
and it is safe from MySQL injection
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    from database get states
    """

    db = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3]
            )

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY \
                    id ASC", {'name': argv[4]}
            )

    states = cursor.fetchall()

    for state in states:
        print(state)
