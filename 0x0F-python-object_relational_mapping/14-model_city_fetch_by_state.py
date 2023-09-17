#!/usr/bin/python3
"""
script to print all city objects
from database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    """
    main script to print all city objects
    """

    db_engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_engine)
    session = sessionmaker(bind=engine)()

    city_states = session.query(City, State).join(State)

    for city, state in city_states.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
