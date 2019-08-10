#!/usr/bin/python3
"""script that lists first state objects from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base
from model_state import State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    sq = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in sq:
        print("{}: {}".format(state.id, state.name))
    session.close()
