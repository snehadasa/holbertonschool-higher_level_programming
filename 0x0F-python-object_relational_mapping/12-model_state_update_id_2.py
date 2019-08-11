#!/usr/bin/python3
"""script that changes the name of a State object from the
   database hbtn_0e_6_usa to New Mexico id = 2"""

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
    state = session.query(State).filter(State.id == 2).one()
    state.name = 'New Mexico'
    session.flush()
    session.commit()
    session.close()
