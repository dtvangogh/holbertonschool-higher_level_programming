#!/usr/bin/python3
"""
Script that adds a State object to a db
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    """why sometimes you need and sometimes you don't need?"""

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()
    for item in states:
    	if 'a' in item.name:
	    	session.delete(item)
		
    session.commit()
    session.close()
