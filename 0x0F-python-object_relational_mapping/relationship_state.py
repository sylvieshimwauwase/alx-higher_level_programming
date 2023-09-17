#!/usr/bin/python3
"""
Module that contains class definition of a State
with a relationship to city
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_city import Base, City

class State(Base):
    """
    state class definition with relationship
    to city
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="a;;, delete-orphan")
