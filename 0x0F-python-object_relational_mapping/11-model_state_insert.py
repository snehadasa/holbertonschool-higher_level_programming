#!/usr/bin/python3
"""script that prints the State object with the name passed as argument
   from the database hbtn_0e_6_usa"""

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
    new_state = State(name = 'Louisiana')
    session.add(new_state)
    session.flush()
    state = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(state.id))
    session.close()
