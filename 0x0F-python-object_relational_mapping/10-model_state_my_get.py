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
    arg = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    """why does .first work but .all not work? """
    whatWeLookingAt = session.query(State).filter(State.name == arg).first()
    if whatWeLookingAt is not None:
        print("{}".format(whatWeLookingAt.id))
    else:
        print("Not found")
