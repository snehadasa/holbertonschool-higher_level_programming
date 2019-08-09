import MySQLdb
import sqlalchemy
import sys


if __name__=='__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    numrows = cur.execute("SELECT * FROM states")

