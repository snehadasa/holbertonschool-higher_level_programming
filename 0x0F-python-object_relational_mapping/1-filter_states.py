#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sqlalchemy
from sys import argv


if __name__=='__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
