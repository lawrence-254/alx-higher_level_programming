#!/usr/bin/python3
"""
a script that prints the first State object from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username, password, db_name = argv[1], argv[2], argv[3]

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).first()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
