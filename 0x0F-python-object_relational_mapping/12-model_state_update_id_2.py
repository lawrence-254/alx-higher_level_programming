#!/usr/bin/python3
"""
A script that changes the name of a State object in the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id 2 not found")
    session.close()
