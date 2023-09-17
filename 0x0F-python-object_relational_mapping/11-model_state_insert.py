#!/usr/bin/python3
"""
script to list state objects with name passed as argument
from database
where name matches the argument
from the database 'hbtn_0e_4_usa'
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    """
    lists state objects
    """

    db_engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_engine)
    session = sessionmaker(bind=engine)()

    state = State(name="Louisiana")

    session.add(state)

    session.commit()

    print(state.id)
    session.close()
