#!/usr/bin/python3
"""
A script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
