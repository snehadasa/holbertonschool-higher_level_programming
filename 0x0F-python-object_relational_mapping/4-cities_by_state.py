#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sqlalchemy
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM states
                JOIN cities
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
