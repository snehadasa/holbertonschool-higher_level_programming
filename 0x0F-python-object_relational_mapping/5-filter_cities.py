#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sqlalchemy
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM states
                JOIN cities
                ON cities.state_id = states.id
                WHERE states.name = %s;""", (argv[4],))
    states = cur.fetchall()
    for length, state in enumerate(states):
        if length < len(states) - 1:
            print(state[0], end=", ")
        else:
            print(state[0])
    cur.close()
    db.close()
