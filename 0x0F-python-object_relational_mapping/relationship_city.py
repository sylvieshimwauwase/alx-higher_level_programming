#!/usr/bin/python3
"""
Module that contains class definition of a city
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class State(Base):
    """
    city class definition
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id =Column(Integer, ForeignKey('states.id'), nullable=False)
~                                                         
