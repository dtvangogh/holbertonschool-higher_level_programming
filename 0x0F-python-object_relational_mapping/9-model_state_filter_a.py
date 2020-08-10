#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    whatWeLookingAt = session.query(State).order_by(State.id.asc()).all() 
    for state in whatWeLookingAt:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
            
        
